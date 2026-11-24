import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs("assets", exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Assam Trade Corridors & Logistics Map Diagram
# -----------------------------------------------------------------------------
def create_assam_corridor_map():
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 7.15, "Assam Strategic Fish-Flow & Border Ingress Corridor Map", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.8, "Physical Inbound Checkpoints, Wholesale Mandis, and Inland Beel Production Clusters", 
            ha='center', va='center', fontsize=9, color='#475569')

    # Stylized River Basin (Brahmaputra)
    brahma_x = [0.8, 2.5, 4.5, 7.0, 9.5, 11.2]
    brahma_y = [4.2, 4.6, 4.3, 4.7, 4.4, 4.8]
    ax.plot(brahma_x, brahma_y, color='#93C5FD', lw=14, alpha=0.45, solid_capstyle='round')
    ax.text(8.2, 4.85, "Brahmaputra River Basin", fontsize=8.5, color='#1D4ED8', fontstyle='italic', fontweight='bold')

    # Stylized Barak River
    ax.plot([7.5, 9.0, 10.5], [1.5, 1.4, 1.6], color='#93C5FD', lw=10, alpha=0.45, solid_capstyle='round')
    ax.text(9.2, 1.15, "Barak River Basin (Southern Assam)", fontsize=8, color='#1D4ED8', fontstyle='italic', fontweight='bold')

    # Nodes on Map
    # 1. Border Gateways (Red)
    gates = [
        {"name": "Srirampur Gate\n[Dhubri/Kokrajhar Border]\nInflow from AP & WB", "x": 1.2, "y": 5.4, "tag": "CHECKPOST 1"},
        {"name": "Boxirhat Gate\n[Western Corridor]\nIced Fish Reefers", "x": 1.2, "y": 3.0, "tag": "CHECKPOST 2"},
        {"name": "Khanapara Gate\n[GS Road Highway]\nInter-District Transit", "x": 5.5, "y": 3.2, "tag": "CHECKPOST 3"}
    ]
    for g in gates:
        ax.add_patch(patches.FancyBboxPatch((g["x"]-0.8, g["y"]-0.5), 2.1, 1.1, boxstyle="round,pad=0.08", fc="#FEE2E2", ec="#EF4444", lw=1.5))
        ax.text(g["x"]+0.25, g["y"]+0.35, g["tag"], fontsize=6.5, fontweight='bold', color="#991B1B", ha='center')
        ax.text(g["x"]+0.25, g["y"]-0.05, g["name"], fontsize=6.8, color="#7F1D1D", ha='center', va='center')

    # 2. Wholesale Mandis (Blue)
    mandis = [
        {"name": "Uzanbazar & Betkuchi Mandis\n[Kamrup Metro]\nGuwahati Major Consumption Hub\n(1,200+ Crates/Day)", "x": 5.0, "y": 5.2, "tag": "MANDI HUB 1"},
        {"name": "Nagaon Sadar Mandi\n[Nagaon Hub]\nBeel & Aquaculture Landing\n(650 Crates/Day)", "x": 7.8, "y": 5.2, "tag": "MANDI HUB 2"},
        {"name": "Silchar Wholesale Yard\n[Cachar District]\nBarak Valley Distribution\n(450 Crates/Day)", "x": 8.8, "y": 2.2, "tag": "MANDI HUB 3"}
    ]
    for m in mandis:
        ax.add_patch(patches.FancyBboxPatch((m["x"]-0.9, m["y"]-0.6), 2.4, 1.25, boxstyle="round,pad=0.08", fc="#E0F2FE", ec="#0284C7", lw=1.6))
        ax.text(m["x"]+0.3, m["y"]+0.42, m["tag"], fontsize=6.5, fontweight='bold', color="#0369A1", ha='center')
        ax.text(m["x"]+0.3, m["y"]-0.05, m["name"], fontsize=6.6, color="#0C4A6E", ha='center', va='center')

    # 3. Native Production Wetland Clusters (Green)
    clusters = [
        {"name": "Nagaon Beel Cluster\n(Samaguri, Raha, Morigaon)\nExtensive Aquaculture Ponds", "x": 7.5, "y": 3.6},
        {"name": "Barpeta Wetland Zone\nRiverine Freshwater Fishery", "x": 3.4, "y": 5.5}
    ]
    for c in clusters:
        ax.add_patch(patches.FancyBboxPatch((c["x"]-0.8, c["y"]-0.45), 2.0, 0.9, boxstyle="round,pad=0.08", fc="#DCFCE7", ec="#16A34A", lw=1.4))
        ax.text(c["x"]+0.2, c["y"]+0.25, "NATIVE PRODUCTION", fontsize=6.0, fontweight='bold', color="#166534", ha='center')
        ax.text(c["x"]+0.2, c["y"]-0.1, c["name"], fontsize=6.5, color="#14532D", ha='center', va='center')

    # Flow Arrows
    # Srirampur -> Uzanbazar
    ax.annotate('', xy=(4.1, 5.2), xytext=(2.6, 5.4),
                arrowprops=dict(facecolor='#DC2626', edgecolor='#DC2626', arrowstyle="->", lw=2.5))
    ax.text(3.35, 5.6, "Inbound Iced Imports (AP/WB)\n[DEDUCTED (-)]", fontsize=6.5, color='#B91C1C', fontweight='bold', ha='center')

    # Nagaon Cluster -> Nagaon Mandi -> Uzanbazar
    ax.annotate('', xy=(7.8, 4.6), xytext=(7.8, 4.1),
                arrowprops=dict(facecolor='#16A34A', edgecolor='#16A34A', arrowstyle="->", lw=2.0))
    ax.annotate('', xy=(6.5, 5.2), xytext=(7.0, 5.2),
                arrowprops=dict(facecolor='#0284C7', edgecolor='#0284C7', arrowstyle="->", lw=2.0))

    # Legend Panel
    leg_box = patches.FancyBboxPatch((0.8, 0.4), 10.4, 0.75, boxstyle="round,pad=0.06", fc='#FFFFFF', ec='#CBD5E1', lw=1.2)
    ax.add_patch(leg_box)
    ax.text(1.2, 0.78, "MAP LEGEND:", fontsize=7.5, fontweight='bold', color='#1E293B')
    
    # Red indicator
    ax.add_patch(patches.Circle((2.5, 0.78), 0.12, fc='#EF4444'))
    ax.text(2.7, 0.78, "Border Gateways (Imports)", fontsize=7.0, color='#334155', va='center')
    
    # Blue indicator
    ax.add_patch(patches.Circle((5.2, 0.78), 0.12, fc='#0284C7'))
    ax.text(5.4, 0.78, "Wholesale Mandis (Disappearance)", fontsize=7.0, color='#334155', va='center')
    
    # Green indicator
    ax.add_patch(patches.Circle((8.3, 0.78), 0.12, fc='#16A34A'))
    ax.text(8.5, 0.78, "Inland Aquaculture & Beel Clusters", fontsize=7.0, color='#334155', va='center')

    plt.tight_layout()
    plt.savefig("assets/assam_corridor_map.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/assam_corridor_map.png")


# -----------------------------------------------------------------------------
# 2. Market Arrival Fallacy Infographic
# -----------------------------------------------------------------------------
def create_market_fallacy_infographic():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6.2), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')

    for ax in [ax1, ax2]:
        ax.set_xlim(0, 6)
        ax.set_ylim(0, 7)
        ax.axis('off')
        ax.set_facecolor('#F8FAFC')

    # Left: The Flawed Traditional Workflow
    box1 = patches.FancyBboxPatch((0.2, 0.3), 5.6, 6.4, boxstyle="round,pad=0.1", fc='#FEF2F2', ec='#F87171', lw=1.8)
    ax1.add_patch(box1)
    ax1.text(3.0, 6.35, "THE STATUS QUO / FLAWED APPROACH", fontsize=10.5, fontweight='bold', color='#991B1B', ha='center')
    ax1.text(3.0, 6.05, "Equating Wholesale Market Arrivals to Native Yield", fontsize=8.0, color='#B91C1C', ha='center')

    # Visual blocks for Status Quo
    sq_steps = [
        {"y": 4.8, "title": "1. Wholesale Mandi Arrival Intake", "desc": "Guwahati receives 10,000 MT fish.\nEnumerator tallies gross volume directly.", "fc": "#FFFFFF", "ec": "#FCA5A5"},
        {"y": 3.4, "title": "2. Failure to Identify Origin", "desc": "6,500 MT of chilled fish from Andhra/WB\nis blended indistinguishably with local catch.", "fc": "#FFFFFF", "ec": "#FCA5A5"},
        {"y": 2.0, "title": "3. The 'Arrival = Yield' Fallacy", "desc": "Total 10,000 MT declared as 'State Production'.\nRural direct subsistence catch ignored.", "fc": "#FFFFFF", "ec": "#FCA5A5"},
        {"y": 0.6, "title": "RESULT: SEVERE DATA DISTORTION", "desc": "Official production overstated by +35% to +45%!\nMisleads state planning & fingerling subsidies.", "fc": "#FEE2E2", "ec": "#EF4444", "tc": "#991B1B"}
    ]
    for s in sq_steps:
        bx = patches.FancyBboxPatch((0.5, s["y"]), 5.0, 1.1, boxstyle="round,pad=0.08", fc=s["fc"], ec=s["ec"], lw=1.2)
        ax1.add_patch(bx)
        ax1.text(0.7, s["y"]+0.85, s["title"], fontsize=8.5, fontweight='bold', color=s.get("tc", "#7F1D1D"))
        ax1.text(0.7, s["y"]+0.48, s["desc"], fontsize=7.2, color='#450A0A')

    # Right: The MatsyaFlow Reconciled Approach
    box2 = patches.FancyBboxPatch((0.2, 0.3), 5.6, 6.4, boxstyle="round,pad=0.1", fc='#F0FDF4', ec='#4ADE80', lw=1.8)
    ax2.add_patch(box2)
    ax2.text(3.0, 6.35, "THE MATSYAFLOW RECONCILED MODEL", fontsize=10.5, fontweight='bold', color='#166534', ha='center')
    ax2.text(3.0, 6.05, "Multi-Parameter Mass-Balance Triangulation", fontsize=8.0, color='#15803D', ha='center')

    mf_steps = [
        {"y": 4.8, "title": "1. Checkpost Inflow Tagging", "desc": "Border reefers logged at Srirampur/Boxirhat.\n6,500 MT tagged as 'Verified Import'.", "fc": "#FFFFFF", "ec": "#86EFAC"},
        {"y": 3.4, "title": "2. Mandi Disappearance Decoupling", "desc": "Wholesale gross (10,000 MT) decoupled:\nImports (6,500 MT) mathematically deducted.", "fc": "#FFFFFF", "ec": "#86EFAC"},
        {"y": 2.0, "title": "3. Mass-Balance Ingestion", "desc": "Adds modeled rural consumption (3,200 MT)\n+ Post-harvest wastage (950 MT) + Outflows.", "fc": "#FFFFFF", "ec": "#86EFAC"},
        {"y": 0.6, "title": "RESULT: AUDITABLE ACCURACY (±5%)", "desc": "True native yield validated at 7,650 MT.\nTamper-evident cryptographic statistical confidence.", "fc": "#DCFCE7", "ec": "#22C55E", "tc": "#14532D"}
    ]
    for s in mf_steps:
        bx = patches.FancyBboxPatch((0.5, s["y"]), 5.0, 1.1, boxstyle="round,pad=0.08", fc=s["fc"], ec=s["ec"], lw=1.2)
        ax2.add_patch(bx)
        ax2.text(0.7, s["y"]+0.85, s["title"], fontsize=8.5, fontweight='bold', color=s.get("tc", "#14532D"))
        ax2.text(0.7, s["y"]+0.48, s["desc"], fontsize=7.2, color='#052E16')

    plt.tight_layout()
    plt.savefig("assets/market_fallacy_infographic.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/market_fallacy_infographic.png")


# -----------------------------------------------------------------------------
# 3. Field Hardware & Edge IoT Kit Blueprint
# -----------------------------------------------------------------------------
def create_hardware_blueprint():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 6.6, "MatsyaFlow Field Hardware & Edge IoT Deployment Blueprint", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.25, "Ruggedized, Low-Maintenance Field Kit Budgeted at ₹5.50 Lakhs for Highway Gates and Wholesale Mandis", 
            ha='center', va='center', fontsize=9, color='#475569')

    devices = [
        {"x": 0.6, "w": 2.5, "title": "1. RUGGED CHECKPOST TABLET", "icon": "[TABLET]",
         "specs": "• IP67 Dust/Waterproof\n• 8-inch Sunlight-readable\n• 4G LTE + Offline SQLite\n• 8,000 mAh Solar Battery\n• Cost: ₹27,500 × 8 Units\n• Allocation: ₹2.20 Lakhs",
         "fc": "#EFF6FF", "ec": "#3B82F6", "tc": "#1D4ED8"},
        
        {"x": 3.4, "w": 2.5, "title": "2. BLUETOOTH SCALE BRIDGE", "icon": "[IOT BRIDGE]",
         "specs": "• RS232-to-BLE Converter\n• Universal Mandi Scale Pairing\n• Streams Crate Lot Weight\n• Zero manual re-entry error\n• Cost: ₹30,000 × 6 Units\n• Allocation: ₹1.80 Lakhs",
         "fc": "#F0FDF4", "ec": "#22C55E", "tc": "#15803D"},

        {"x": 6.2, "w": 2.5, "title": "3. HANDHELD OCR SCANNER", "icon": "[OCR SCANNER]",
         "specs": "• High-speed 2D Barcode/OCR\n• Auto-extracts paper waybills\n• Fast <20s intake per truck\n• Bluetooth 5.2 to Tablet\n• Cost: ₹10,000 × 8 Units\n• Allocation: ₹0.80 Lakhs",
         "fc": "#FEF3C7", "ec": "#F59E0B", "tc": "#B45309"},

        {"x": 9.0, "w": 2.5, "title": "4. THERMAL QR SLIP PRINTER", "icon": "[QR PRINTER]",
         "specs": "• Heavy-duty thermal print\n• Weatherproof slip output\n• Truck driver QR token pass\n• Battery-powered field kit\n• Cost: ₹8,750 × 8 Units\n• Allocation: ₹0.70 Lakhs",
         "fc": "#F3E8FF", "ec": "#A855F7", "tc": "#7E22CE"}
    ]

    for d in devices:
        box = patches.FancyBboxPatch((d["x"], 1.4), d["w"], 4.5, boxstyle="round,pad=0.1", fc=d["fc"], ec=d["ec"], lw=1.6)
        ax.add_patch(box)
        ax.text(d["x"]+d["w"]/2, 5.5, d["title"], fontsize=8.5, fontweight='bold', color=d["tc"], ha='center')
        ax.text(d["x"]+d["w"]/2, 4.9, d["icon"], fontsize=11, fontweight='bold', color='#1E293B', ha='center')
        ax.text(d["x"]+0.2, 4.4, d["specs"], fontsize=7.5, color='#334155', va='top')

    # Bottom Banner
    banner = patches.FancyBboxPatch((0.6, 0.4), 10.9, 0.75, boxstyle="round,pad=0.08", fc="#1E293B", ec="#0F172A")
    ax.add_patch(banner)
    ax.text(6, 0.78, "TOTAL HARDWARE ALLOCATION: ₹5.50 LAKHS (13.75% OF GRANT) — ZERO VENDOR LOCK-IN, OFF-THE-SHELF HARDWARE", 
            ha='center', va='center', fontsize=8.5, fontweight='bold', color="#38BDF8")

    plt.tight_layout()
    plt.savefig("assets/hardware_kit_blueprint.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/hardware_kit_blueprint.png")


# -----------------------------------------------------------------------------
# 4. Implementation Gantt Chart
# -----------------------------------------------------------------------------
def create_implementation_gantt():
    fig, ax = plt.subplots(figsize=(12, 5.6), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#FFFFFF')

    tasks = [
        "Phase 1: Discovery, Corridor Mapping & SRS Finalization",
        "Phase 2.1: Cloud Microservices & TimescaleDB Database",
        "Phase 2.2: Offline-First PWA & Edge OCR Reader",
        "Phase 2.3: Bluetooth Weighing Scale Integration",
        "Phase 3.1: Bayesian Mass-Balance Algorithm Coding",
        "Phase 3.2: DFO Executive GIS Workbench MVP",
        "Phase 4.1: 3-District Live Field Pilot (Kamrup, Nagaon, Cachar)",
        "Phase 4.2: Third-Party CERT-In Security Audit (VAPT)",
        "Phase 4.3: Departmental Training & State Handover"
    ]
    starts = [0, 2, 2.5, 3, 4, 4.5, 6, 7.5, 8]
    durations = [2, 2, 1.5, 1.5, 2, 1.5, 2, 1, 1]
    phase_colors = ['#0284C7', '#6366F1', '#6366F1', '#6366F1', '#D97706', '#D97706', '#16A34A', '#DC2626', '#16A34A']

    y_pos = np.arange(len(tasks))

    for i in range(len(tasks)):
        ax.barh(y_pos[i], durations[i], left=starts[i], height=0.55, align='center', 
                color=phase_colors[i], edgecolor='#0F172A', lw=0.8, alpha=0.9)
        ax.text(starts[i] + durations[i]/2, y_pos[i], f"M{starts[i]+1}–M{starts[i]+durations[i]}", 
                ha='center', va='center', color='#FFFFFF', fontsize=7.2, fontweight='bold')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=8, fontweight='medium', color='#1E293B')
    ax.invert_yaxis()
    ax.set_xlim(0, 9)
    ax.set_xticks(range(10))
    ax.set_xticklabels([f"Month {m}" if m > 0 else "Kickoff" for m in range(10)], fontsize=8, fontweight='bold', color='#0F172A')
    ax.set_title("MatsyaFlow-Assam: 9-Month Implementation Work Breakdown Schedule (WBS)", fontsize=11, fontweight='bold', color='#0F172A', pad=12)
    ax.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("assets/implementation_gantt.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/implementation_gantt.png")


# -----------------------------------------------------------------------------
# 5. Pilot District Profiles
# -----------------------------------------------------------------------------
def create_pilot_district_profiles():
    fig, ax = plt.subplots(figsize=(12, 6.0), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.5)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 6.1, "MatsyaFlow 3-District Live Pilot Validation Ecosystem", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 5.75, "Stratified Selection Covering Urban Consumption, Native Production Heartland, and Valley Distribution", 
            ha='center', va='center', fontsize=9, color='#475569')

    districts = [
        {"x": 0.6, "w": 3.4, "name": "1. KAMRUP METROPOLITAN", "role": "Urban Consumption & Transit Hub",
         "points": "• Epicecenter of state fish sales.\n• Houses Uzanbazar & Betkuchi mandis.\n• Massive iced import intake (AP/WB).\n• Challenge: Severe raw arrival bias.\n• Role in Pilot: Validating import\n  deduction accuracy & urban off-take.",
         "fc": "#EFF6FF", "ec": "#0284C7", "tc": "#0369A1"},

        {"x": 4.3, "w": 3.4, "name": "2. NAGAON DISTRICT", "role": "State Aquaculture & Beel Heartland",
         "points": "• Top producing district in Assam.\n• Vast beel leases (Samaguri, Raha).\n• Thousands of commercial fish ponds.\n• Challenge: Unreported farmer harvests.\n• Role in Pilot: Calibrating native\n  catch mass balance & loss rates.",
         "fc": "#F0FDF4", "ec": "#16A34A", "tc": "#15803D"},

        {"x": 8.0, "w": 3.4, "name": "3. CACHAR (SILCHAR)", "role": "Barak Valley Distribution Gateway",
         "points": "• Distinct geographic & riverine ecology.\n• Central distribution for southern Assam.\n• Transit cross-flows to Tripura/Mizoram.\n• Challenge: Porous inter-district movement.\n• Role in Pilot: Testing corridor\n  re-export accounting & border logs.",
         "fc": "#FEF3C7", "ec": "#D97706", "tc": "#B45309"}
    ]

    for d in districts:
        box = patches.FancyBboxPatch((d["x"], 0.8), d["w"], 4.6, boxstyle="round,pad=0.1", fc=d["fc"], ec=d["ec"], lw=1.8)
        ax.add_patch(box)
        ax.text(d["x"]+d["w"]/2, 5.0, d["name"], fontsize=9.5, fontweight='bold', color=d["tc"], ha='center')
        ax.text(d["x"]+d["w"]/2, 4.6, d["role"], fontsize=7.5, color='#475569', ha='center', fontstyle='italic')
        ax.text(d["x"]+0.25, 4.1, d["points"], fontsize=8.0, color='#1E293B', va='top')

    plt.tight_layout()
    plt.savefig("assets/pilot_district_profiles.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/pilot_district_profiles.png")

if __name__ == "__main__":
    create_assam_corridor_map()
    create_market_fallacy_infographic()
    create_hardware_blueprint()
    create_implementation_gantt()
    create_pilot_district_profiles()
