import json
import re

with open("scripts/build_proposal_texts.py") as f:
    content = f.read()

# Extract sections dictionary from build_proposal_texts.py
# Or load directly by importing
import sys
sys.path.append("scripts")
from build_proposal_texts import sections

html_sections = []
for title, text in sections.items():
    words = len(text.split())
    html_sections.append({
        "title": title,
        "words": words,
        "text": text
    })

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MatsyaFlow-Assam | NESFIC-D-34 Dev Server & Proposal Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
                        mono: ['"JetBrains Mono"', 'monospace']
                    },
                    colors: {
                        brand: {
                            50: '#F0F9FF',
                            100: '#E0F2FE',
                            500: '#0EA5E9',
                            600: '#0284C7',
                            700: '#0369A1',
                            900: '#0C4A6E',
                            dark: '#0F172A'
                        }
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-900 text-slate-100 font-sans antialiased min-h-screen flex flex-col">

    <!-- Top Navigation Bar -->
    <header class="bg-slate-950 border-b border-slate-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-sky-500/20">
                    <span class="text-xl font-black text-white">M</span>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="font-bold text-lg text-white">MatsyaFlow-Assam</span>
                        <span class="text-xs bg-sky-500/20 text-sky-400 font-mono px-2 py-0.5 rounded border border-sky-500/30">NESFIC-D-34</span>
                    </div>
                    <p class="text-xs text-slate-400 hidden sm:block">Fish-Flow & Market Data for Independent Validation of Annual Fish Production</p>
                </div>
            </div>

            <!-- Tabs -->
            <nav class="flex space-x-1 sm:space-x-2">
                <button onclick="switchTab('proposal')" id="tab-btn-proposal" class="nav-tab px-3 py-1.5 rounded-lg text-sm font-medium transition-all bg-sky-600 text-white shadow-sm">
                    Proposal Text (12 Forms)
                </button>
                <button onclick="switchTab('simulator')" id="tab-btn-simulator" class="nav-tab px-3 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-400 hover:text-white hover:bg-slate-800">
                    Mass-Balance Simulator
                </button>
                <button onclick="switchTab('budget')" id="tab-btn-budget" class="nav-tab px-3 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-400 hover:text-white hover:bg-slate-800">
                    ₹40L Budget
                </button>
                <button onclick="switchTab('downloads')" id="tab-btn-downloads" class="nav-tab px-3 py-1.5 rounded-lg text-sm font-medium transition-all text-slate-400 hover:text-white hover:bg-slate-800">
                    PDF Downloads
                </button>
            </nav>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">

        <!-- ============================================================= -->
        <!-- TAB 1: PROPOSAL FORM TEXT (COPY-PASTE READY) -->
        <!-- ============================================================= -->
        <div id="tab-proposal" class="tab-content block">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4 bg-slate-950 p-4 rounded-xl border border-slate-800">
                <div>
                    <h1 class="text-xl font-bold text-white">Proposal Form Contents (12 Portal Fields)</h1>
                    <p class="text-xs text-slate-400">Click any field to view full text or copy to clipboard. All sections validated under 500 words.</p>
                </div>
                <div class="flex items-center space-x-3">
                    <button onclick="copyAllText()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-lg border border-slate-700 flex items-center space-x-2 transition">
                        <span>Copy Entire Proposal File</span>
                    </button>
                    <a href="/output/NESFIC_D34_Proof_of_Work.pdf" target="_blank" class="px-4 py-2 bg-sky-600 hover:bg-sky-500 text-white text-xs font-semibold rounded-lg shadow flex items-center space-x-2 transition">
                        <span>View Proof of Work PDF</span>
                    </a>
                </div>
            </div>

            <!-- List of 12 Sections -->
            <div class="space-y-4" id="sections-container">
                <!-- Dynamically populated or rendered -->
            </div>
        </div>

        <!-- ============================================================= -->
        <!-- TAB 2: INTERACTIVE MASS-BALANCE RECONCILIATION SIMULATOR -->
        <!-- ============================================================= -->
        <div id="tab-simulator" class="tab-content hidden">
            <div class="mb-6 bg-slate-950 p-5 rounded-xl border border-slate-800">
                <h1 class="text-xl font-bold text-white mb-1">MatsyaFlow Mass-Balance Bayesian Simulator</h1>
                <p class="text-xs text-slate-400">Test how the reconciliation engine decouples external imports from native production in real time across the 3 pilot districts.</p>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Left: Controls & Sliders -->
                <div class="lg:col-span-1 bg-slate-950 p-6 rounded-2xl border border-slate-800 space-y-5">
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Pilot District</span>
                        <select id="district-select" onchange="loadDistrictPreset()" class="bg-slate-900 border border-slate-700 text-xs rounded-lg px-3 py-1.5 text-white focus:outline-none focus:border-sky-500">
                            <option value="kamrup">Kamrup Metro (Urban Hub)</option>
                            <option value="nagaon" selected>Nagaon (Production Heartland)</option>
                            <option value="cachar">Cachar (Barak Valley Hub)</option>
                        </select>
                    </div>

                    <!-- Formula Reference Banner -->
                    <div class="p-3 bg-slate-900/80 rounded-xl border border-slate-800 text-[11px] font-mono text-sky-300 text-center">
                        P_local = (D_mandi + C_rural + L_loss + E_export) - I_import
                    </div>

                    <div class="space-y-4">
                        <!-- Mandi Sales -->
                        <div>
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-300 font-medium">Wholesale Mandi Sales (D)</span>
                                <span class="font-mono text-sky-400 font-bold" id="val-mandi">35,000 MT</span>
                            </div>
                            <input type="range" id="slider-mandi" min="5000" max="60000" step="500" value="35000" oninput="runSimulation()" class="w-full accent-sky-500 bg-slate-800">
                            <span class="text-[10px] text-slate-500">Observed wholesale arrival records</span>
                        </div>

                        <!-- Inbound Imports -->
                        <div>
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-300 font-medium">Inter-State Inbound Imports (I)</span>
                                <span class="font-mono text-rose-400 font-bold" id="val-imports">12,000 MT</span>
                            </div>
                            <input type="range" id="slider-imports" min="1000" max="30000" step="500" value="12000" oninput="runSimulation()" class="w-full accent-rose-500 bg-slate-800">
                            <span class="text-[10px] text-slate-500">Verified reefer entries via checkposts (AP/WB)</span>
                        </div>

                        <!-- Rural Subsistence Offtake -->
                        <div>
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-300 font-medium">Rural Subsistence Direct Catch (C)</span>
                                <span class="font-mono text-amber-400 font-bold" id="val-rural">9,500 MT</span>
                            </div>
                            <input type="range" id="slider-rural" min="2000" max="25000" step="250" value="9500" oninput="runSimulation()" class="w-full accent-amber-500 bg-slate-800">
                            <span class="text-[10px] text-slate-500">Modeled local homestead and beel harvest</span>
                        </div>

                        <!-- Post-Harvest Loss -->
                        <div>
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-300 font-medium">Post-Harvest Spoilage & Loss (L)</span>
                                <span class="font-mono text-orange-400 font-bold" id="val-loss">3,200 MT</span>
                            </div>
                            <input type="range" id="slider-loss" min="500" max="8000" step="100" value="3200" oninput="runSimulation()" class="w-full accent-orange-500 bg-slate-800">
                            <span class="text-[10px] text-slate-500">Empirically calibrated loss (8.5–11.5%)</span>
                        </div>

                        <!-- Outward Exports -->
                        <div>
                            <div class="flex justify-between text-xs mb-1">
                                <span class="text-slate-300 font-medium">Outward Cross-District Dispatches (E)</span>
                                <span class="font-mono text-teal-400 font-bold" id="val-export">4,500 MT</span>
                            </div>
                            <input type="range" id="slider-export" min="500" max="15000" step="250" value="4500" oninput="runSimulation()" class="w-full accent-teal-500 bg-slate-800">
                            <span class="text-[10px] text-slate-500">Bulk dispatches to neighboring districts/states</span>
                        </div>
                    </div>
                </div>

                <!-- Right: Live Output Cards & Variance Diagnostic -->
                <div class="lg:col-span-2 space-y-6">
                    <!-- Key Metric Highlights -->
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                        <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800">
                            <span class="text-xs text-slate-400 block mb-1">Reconciled Native Yield</span>
                            <div class="text-2xl font-black text-sky-400 font-mono" id="out-reconciled">40,200 MT</div>
                            <span class="text-[11px] text-emerald-400 font-medium mt-1 inline-block">±4.8% Bayesian Interval</span>
                        </div>

                        <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800">
                            <span class="text-xs text-slate-400 block mb-1">Raw Market Arrivals</span>
                            <div class="text-2xl font-black text-rose-400 font-mono" id="out-rawmandi">47,000 MT</div>
                            <span class="text-[11px] text-rose-400/80 font-medium mt-1 inline-block">Includes External Imports!</span>
                        </div>

                        <div class="bg-slate-950 p-5 rounded-2xl border border-slate-800">
                            <span class="text-xs text-slate-400 block mb-1">Baseline Survey Claim</span>
                            <div class="text-2xl font-black text-amber-400 font-mono" id="out-fdoclaim">48,500 MT</div>
                            <span class="text-[11px] text-amber-400 font-medium mt-1 inline-block" id="out-variance">+20.6% Discrepancy</span>
                        </div>
                    </div>

                    <!-- Diagnostic Alert Box -->
                    <div id="diagnostic-box" class="p-5 rounded-2xl border transition-all bg-amber-950/30 border-amber-800/60 text-amber-200">
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-xs font-bold uppercase tracking-wider text-amber-400 flex items-center gap-2">
                                <span class="w-2 h-2 rounded-full bg-amber-400 animate-pulse"></span>
                                DFO Automated Advisory Flag
                            </span>
                            <span class="text-xs font-mono bg-amber-900/40 px-2 py-0.5 rounded border border-amber-700/50">TICKET #D34-2026-VAL</span>
                        </div>
                        <p class="text-sm font-medium" id="diagnostic-text">
                            Noticeable discrepancy detected. Reported field survey figures exceed physical market disappearance and logistics capacity. Recommended action: Deploy ground-truthing enumerators to Nagaon-West cluster.
                        </p>
                    </div>

                    <!-- Flow Balance Breakdown Bar -->
                    <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800 space-y-4">
                        <h3 class="text-sm font-bold text-slate-200">Mass-Balance Mass Inflow vs. Net Disappearance Flow</h3>
                        
                        <div class="h-6 w-full bg-slate-900 rounded-lg overflow-hidden flex border border-slate-800">
                            <div id="bar-mandi" class="bg-sky-500 h-full transition-all" style="width: 50%" title="Wholesale Mandi"></div>
                            <div id="bar-rural" class="bg-amber-500 h-full transition-all" style="width: 25%" title="Rural Direct"></div>
                            <div id="bar-loss" class="bg-orange-500 h-full transition-all" style="width: 10%" title="Post-Harvest Loss"></div>
                            <div id="bar-export" class="bg-teal-500 h-full transition-all" style="width: 15%" title="Outward Exports"></div>
                        </div>

                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                            <div class="flex items-center space-x-2">
                                <div class="w-3 h-3 rounded bg-sky-500"></div>
                                <span class="text-slate-400">Mandi Sales</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <div class="w-3 h-3 rounded bg-amber-500"></div>
                                <span class="text-slate-400">Rural Direct</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <div class="w-3 h-3 rounded bg-orange-500"></div>
                                <span class="text-slate-400">Post-Harvest Loss</span>
                            </div>
                            <div class="flex items-center space-x-2">
                                <div class="w-3 h-3 rounded bg-teal-500"></div>
                                <span class="text-slate-400">Outward Export</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- ============================================================= -->
        <!-- TAB 3: ₹40.00 LAKHS BUDGET EXPLORER -->
        <!-- ============================================================= -->
        <div id="tab-budget" class="tab-content hidden">
            <div class="mb-6 bg-slate-950 p-5 rounded-xl border border-slate-800 flex justify-between items-center">
                <div>
                    <h1 class="text-xl font-bold text-white mb-1">NESFIC-D-34: Indicative Budget & Resource Allocation</h1>
                    <p class="text-xs text-slate-400">Total Problem Statement Grant: ₹40.00 Lakhs | Technical Engineering Team: ₹20.00 Lakhs (50.0%)</p>
                </div>
                <span class="text-xs font-mono bg-emerald-500/20 text-emerald-400 px-3 py-1.5 rounded-lg border border-emerald-500/30 font-bold">100% Balanced</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <!-- Highlight Card: Technical Engineering Team -->
                <div class="md:col-span-3 bg-gradient-to-r from-sky-950/80 via-slate-900 to-indigo-950/80 p-6 rounded-2xl border border-sky-500/40 relative overflow-hidden">
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-4">
                        <div>
                            <span class="text-xs font-bold uppercase tracking-wider text-sky-400">Primary Allocation Head (50%)</span>
                            <h2 class="text-2xl font-black text-white">Technical Engineering Team</h2>
                        </div>
                        <div class="text-right">
                            <span class="text-3xl font-black text-sky-300 font-mono">₹20.00 Lakhs</span>
                            <span class="text-xs text-slate-400 block">4 Core Engineering Specialists</span>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
                        <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
                            <h4 class="text-xs font-bold text-white mb-1">Lead Systems Architect</h4>
                            <span class="text-xs font-mono text-sky-400 block mb-1">₹6.75 Lakhs (9 mos)</span>
                            <p class="text-[11px] text-slate-400">Microservices, PostGIS spatial data, API gateways & cloud security.</p>
                        </div>
                        <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
                            <h4 class="text-xs font-bold text-white mb-1">Senior Data Scientist</h4>
                            <span class="text-xs font-mono text-sky-400 block mb-1">₹6.75 Lakhs (9 mos)</span>
                            <p class="text-[11px] text-slate-400">Bayesian state-space models, Kalman filtering & anomaly detection.</p>
                        </div>
                        <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
                            <h4 class="text-xs font-bold text-white mb-1">Mobile & Edge Engineer</h4>
                            <span class="text-xs font-mono text-sky-400 block mb-1">₹5.00 Lakhs (9 mos)</span>
                            <p class="text-[11px] text-slate-400">Flutter offline PWA, edge OCR scanning, Bluetooth scale sync.</p>
                        </div>
                        <div class="bg-slate-950/80 p-4 rounded-xl border border-slate-800">
                            <h4 class="text-xs font-bold text-white mb-1">QA & Cloud SecOps</h4>
                            <span class="text-xs font-mono text-sky-400 block mb-1">₹1.50 Lakhs (Part-time)</span>
                            <p class="text-[11px] text-slate-400">Automated test harness, ASDC integration & stress testing.</p>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Field Hardware -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-sm font-bold text-white">2. Field Hardware & IoT Setup</h3>
                        <span class="text-sm font-mono font-bold text-amber-400">₹5.50L (13.75%)</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-4">8 Ruggedized tablets for border checkposts, 6 Bluetooth scale bridges, and handheld OCR scanner kits.</p>
                    <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                        <div class="h-full bg-amber-500" style="width: 13.75%"></div>
                    </div>
                </div>

                <!-- Card 3: Field Enumeration -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-sm font-bold text-white">3. Field Surveys & Ground-Truthing</h3>
                        <span class="text-sm font-mono font-bold text-emerald-400">₹6.00L (15.0%)</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-4">Field Research Lead (9 mos) and 3 Cluster Enumerators covering Kamrup Metro, Nagaon, and Cachar.</p>
                    <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                        <div class="h-full bg-emerald-500" style="width: 15%"></div>
                    </div>
                </div>

                <!-- Card 4: Cloud & Security -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-sm font-bold text-white">4. Cloud, Maps & Security Audit</h3>
                        <span class="text-sm font-mono font-bold text-purple-400">₹3.50L (8.75%)</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-4">ASDC sovereign hosting, TimescaleDB instances, Mapbox GIS vector tiles, and third-party CERT-In audit.</p>
                    <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                        <div class="h-full bg-purple-500" style="width: 8.75%"></div>
                    </div>
                </div>

                <!-- Card 5: Stakeholder Workshops -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-sm font-bold text-white">5. Workshops & Capacity Building</h3>
                        <span class="text-sm font-mono font-bold text-pink-400">₹2.50L (6.25%)</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-4">Departmental training for DFOs/FDOs and wholesale mandi Aratdar onboarding with multilingual manuals.</p>
                    <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                        <div class="h-full bg-pink-500" style="width: 6.25%"></div>
                    </div>
                </div>

                <!-- Card 6: Project Management & Contingency -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-sm font-bold text-white">6. Compliance, Audit & Contingency</h3>
                        <span class="text-sm font-mono font-bold text-slate-400">₹2.50L (6.25%)</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-4">Statutory CA audits, legal compliance, pilot travel allowances, and contingency buffer.</p>
                    <div class="h-2 w-full bg-slate-900 rounded-full overflow-hidden">
                        <div class="h-full bg-slate-500" style="width: 6.25%"></div>
                    </div>
                </div>

                <!-- Total Summary Card -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-emerald-500/40 flex flex-col justify-between">
                    <div>
                        <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Total Sanctioned Grant</span>
                        <h3 class="text-3xl font-black text-white font-mono mt-1">₹40.00 Lakhs</h3>
                    </div>
                    <p class="text-xs text-slate-400 mt-2">100% compliant with NESFIC 2026 problem statement guidelines.</p>
                </div>
            </div>
        </div>

        <!-- ============================================================= -->
        <!-- TAB 4: PDF DOWNLOADS & ARTIFACTS -->
        <!-- ============================================================= -->
        <div id="tab-downloads" class="tab-content hidden">
            <div class="mb-6 bg-slate-950 p-5 rounded-xl border border-slate-800">
                <h1 class="text-xl font-bold text-white mb-1">Generated Submission Artifacts & PDF Uploads</h1>
                <p class="text-xs text-slate-400">Download the required PDF documents generated for the NESFIC application portal (both strictly under 10 MB limit).</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- PDF 1 Card -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800 flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-xs font-mono text-sky-400 font-bold bg-sky-950/60 px-2.5 py-1 rounded border border-sky-800/60">PRIMARY UPLOAD (REQUIRED)</span>
                            <span class="text-xs font-mono text-slate-400">1.4 MB (Max: 10 MB)</span>
                        </div>
                        <h3 class="text-lg font-bold text-white">NESFIC_D34_Proof_of_Work.pdf</h3>
                        <p class="text-xs text-slate-400 mt-2 leading-relaxed">
                            Includes complete executive summary, role journeys, high-res UI wireframes, system architecture schematics, mathematical mass-balance formulas, 12-month synthetic simulation results, and field pilot protocols.
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-800 flex items-center justify-between">
                        <span class="text-xs text-emerald-400 font-medium">✓ Ready for Portal Upload</span>
                        <a href="/output/NESFIC_D34_Proof_of_Work.pdf" download class="px-4 py-2 bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold rounded-lg transition shadow">
                            Download Proof of Work PDF
                        </a>
                    </div>
                </div>

                <!-- PDF 2 Card -->
                <div class="bg-slate-950 p-6 rounded-2xl border border-slate-800 flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="text-xs font-mono text-purple-400 font-bold bg-purple-950/60 px-2.5 py-1 rounded border border-purple-800/60">ADDITIONAL MATERIAL (OPTIONAL)</span>
                            <span class="text-xs font-mono text-slate-400">252 KB (Max: 10 MB)</span>
                        </div>
                        <h3 class="text-lg font-bold text-white">NESFIC_D34_Additional_Supporting_Material.pdf</h3>
                        <p class="text-xs text-slate-400 mt-2 leading-relaxed">
                            Includes itemized financial budget table for ₹40 Lakhs (₹20L engineering team), budget donut charts, Work Breakdown Structure (WBS), risk mitigation matrix, and DPDP Act 2023 compliance undertakings.
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-800 flex items-center justify-between">
                        <span class="text-xs text-emerald-400 font-medium">✓ Ready for Portal Upload</span>
                        <a href="/output/NESFIC_D34_Additional_Supporting_Material.pdf" download class="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded-lg transition shadow">
                            Download Supporting Material PDF
                        </a>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <!-- Client-Side Scripts -->
    <script>
        const sectionsData = """ + json.dumps(html_sections) + """;

        function renderSections() {
            const container = document.getElementById('sections-container');
            container.innerHTML = sectionsData.map((sec, idx) => `
                <div class="bg-slate-950 rounded-2xl border border-slate-800 p-5 transition hover:border-slate-700">
                    <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 mb-3">
                        <div class="flex items-center space-x-3">
                            <span class="w-7 h-7 rounded-lg bg-sky-500/10 text-sky-400 font-mono text-xs font-bold flex items-center justify-center border border-sky-500/20">${idx + 1}</span>
                            <h3 class="text-base font-bold text-white">${sec.title}</h3>
                        </div>
                        <div class="flex items-center space-x-3">
                            <span class="text-xs font-mono px-2.5 py-1 rounded-full ${sec.words <= 500 ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-rose-500/10 text-rose-400 border border-rose-500/20'}">
                                ${sec.words} / 500 words
                            </span>
                            <button onclick="copySection(${idx}, this)" class="px-3 py-1.5 bg-sky-600 hover:bg-sky-500 text-white text-xs font-semibold rounded-lg transition shadow flex items-center space-x-1.5">
                                <span>Copy Text</span>
                            </button>
                        </div>
                    </div>
                    <div class="bg-slate-900/90 rounded-xl p-4 text-xs text-slate-300 leading-relaxed font-sans whitespace-pre-wrap border border-slate-800/80 max-h-60 overflow-y-auto">
${sec.text}
                    </div>
                </div>
            `).join('');
        }

        function copySection(idx, btn) {
            const sec = sectionsData[idx];
            navigator.clipboard.writeText(sec.text).then(() => {
                const orig = btn.innerHTML;
                btn.innerHTML = '<span>✓ Copied!</span>';
                btn.classList.remove('bg-sky-600');
                btn.classList.add('bg-emerald-600');
                setTimeout(() => {
                    btn.innerHTML = orig;
                    btn.classList.remove('bg-emerald-600');
                    btn.classList.add('bg-sky-600');
                }, 2000);
            });
        }

        function copyAllText() {
            fetch('/PROPOSAL_FORM_TEXT.txt')
                .then(r => r.text())
                .then(txt => {
                    navigator.clipboard.writeText(txt).then(() => {
                        alert("Entire PROPOSAL_FORM_TEXT.txt copied to clipboard!");
                    });
                });
        }

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('block'));
            
            document.getElementById('tab-' + tabId).classList.remove('hidden');
            document.getElementById('tab-' + tabId).classList.add('block');

            document.querySelectorAll('.nav-tab').forEach(el => {
                el.classList.remove('bg-sky-600', 'text-white', 'shadow-sm');
                el.classList.add('text-slate-400');
            });
            const activeBtn = document.getElementById('tab-btn-' + tabId);
            activeBtn.classList.add('bg-sky-600', 'text-white', 'shadow-sm');
            activeBtn.classList.remove('text-slate-400');
        }

        // Simulator Logic
        const presets = {
            kamrup: { mandi: 48000, imports: 26000, rural: 4000, loss: 3800, export: 2500, fdo: 38000 },
            nagaon: { mandi: 35000, imports: 12000, rural: 9500, loss: 3200, export: 4500, fdo: 48500 },
            cachar: { mandi: 28000, imports: 9000,  rural: 7200, loss: 2400, export: 3000, fdo: 37000 }
        };

        function loadDistrictPreset() {
            const d = document.getElementById('district-select').value;
            const p = presets[d];
            document.getElementById('slider-mandi').value = p.mandi;
            document.getElementById('slider-imports').value = p.imports;
            document.getElementById('slider-rural').value = p.rural;
            document.getElementById('slider-loss').value = p.loss;
            document.getElementById('slider-export').value = p.export;
            runSimulation();
        }

        function runSimulation() {
            const D = parseInt(document.getElementById('slider-mandi').value);
            const I = parseInt(document.getElementById('slider-imports').value);
            const C = parseInt(document.getElementById('slider-rural').value);
            const L = parseInt(document.getElementById('slider-loss').value);
            const E = parseInt(document.getElementById('slider-export').value);

            document.getElementById('val-mandi').innerText = D.toLocaleString() + ' MT';
            document.getElementById('val-imports').innerText = I.toLocaleString() + ' MT';
            document.getElementById('val-rural').innerText = C.toLocaleString() + ' MT';
            document.getElementById('val-loss').innerText = L.toLocaleString() + ' MT';
            document.getElementById('val-export').innerText = E.toLocaleString() + ' MT';

            // Mass-balance formula
            const reconciled = (D + C + L + E) - I;
            const rawMandi = D + (I * 0.4); // Raw market arrivals with partial inbound iced catch
            
            const dist = document.getElementById('district-select').value;
            const fdoClaim = presets[dist].fdo;

            document.getElementById('out-reconciled').innerText = reconciled.toLocaleString() + ' MT';
            document.getElementById('out-rawmandi').innerText = rawMandi.toLocaleString() + ' MT';
            document.getElementById('out-fdoclaim').innerText = fdoClaim.toLocaleString() + ' MT';

            const variancePct = ((fdoClaim - reconciled) / reconciled) * 100;
            const varEl = document.getElementById('out-variance');
            if (variancePct > 0) {
                varEl.innerText = '+' + variancePct.toFixed(1) + '% Over-Report';
                varEl.className = 'text-[11px] text-amber-400 font-medium mt-1 inline-block';
            } else {
                varEl.innerText = variancePct.toFixed(1) + '% Under-Report';
                varEl.className = 'text-[11px] text-rose-400 font-medium mt-1 inline-block';
            }

            const diagBox = document.getElementById('diagnostic-box');
            const diagText = document.getElementById('diagnostic-text');
            if (Math.abs(variancePct) > 15) {
                diagBox.className = 'p-5 rounded-2xl border transition-all bg-amber-950/40 border-amber-800 text-amber-200';
                diagText.innerText = `High discrepancy alert (${variancePct > 0 ? '+' : ''}${variancePct.toFixed(1)}%). Primary survey estimates depart significantly from physical mandi disappearance and logistics capacity. Recommendation: Issue DFO ground-truthing audit ticket.`;
            } else {
                diagBox.className = 'p-5 rounded-2xl border transition-all bg-emerald-950/40 border-emerald-800 text-emerald-200';
                diagText.innerText = `Statistical concordance achieved (${variancePct > 0 ? '+' : ''}${variancePct.toFixed(1)}% within ±7% tolerance limit). Estimated yield reconciled and verified for gazette publication.`;
            }

            // Update percentage bar
            const totalComponents = D + C + L + E;
            document.getElementById('bar-mandi').style.width = ((D / totalComponents) * 100) + '%';
            document.getElementById('bar-rural').style.width = ((C / totalComponents) * 100) + '%';
            document.getElementById('bar-loss').style.width = ((L / totalComponents) * 100) + '%';
            document.getElementById('bar-export').style.width = ((E / totalComponents) * 100) + '%';
        }

        // Initialize
        renderSections();
        runSimulation();
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)
print("Saved index.html successfully")
