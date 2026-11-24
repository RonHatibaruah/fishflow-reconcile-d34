# MatsyaFlow-Assam (`fishflow-reconcile-d34`)

> **NESFIC-D-34: Fish-Flow and Market Data for Independent Validation of Annual Fish Production Estimates**  
> *Sponsoring Department:* Directorate of Fisheries, Government of Assam / Assam Innovation & Startup Foundation (AISF)  
> *Challenge:* North East Seva First Innovation Challenge (NESFIC) 2026  
> *Grant Value:* ₹40.00 Lakhs | *Technical Engineering Team Allocation:* ₹20.00 Lakhs (50.0%)

---

## 📌 Executive Summary
**MatsyaFlow-Assam** is an intelligent, multi-tier Fish-Flow Reconciliation and Independent Production Validation Platform specifically architected for the inland fisheries ecosystem of Assam.

Historically, annual fish production statistics in Assam relied on self-reported farmer returns and periodic localized sample surveys with significant reporting lags (6–9 months). Crucially, **raw wholesale market arrivals cannot be treated as a direct substitute for native production** because major urban centers (such as Guwahati) receive over 1.2 Lakh Metric Tons of iced fish imported from Andhra Pradesh, West Bengal, and Bihar, while remote local catches bypass formal markets entirely.

MatsyaFlow bridges this statistical gap through a **Mass-Balance Bayesian Triangulation Engine**, mathematically reconciling native production by decoupling transit imports from native water-body yield.

---

## 📐 Mathematical Formulation

$$\mathbf{P_{Local} = (D_{Wholesale} + C_{Rural\ Subsistence} + L_{PostHarvest} + E_{Outward}) - I_{Inbound\ Imports}}$$

Where:
- **$P_{Local}$**: Reconciled true native fish production estimate.
- **$D_{Wholesale}$**: Observed daily wholesale market disappearance at major auction hubs (Uzanbazar, Betkuchi, Nagaon Sadar, Silchar).
- **$C_{Rural\ Subsistence}$**: Algorithmic baseline estimation of direct-to-consumer homestead pond and subsistence beel catches (calibrated using Census & NSSO dietary frequency curves).
- **$L_{PostHarvest}$**: Empirically calibrated transport, handling, and spoilage losses (8.5% to 11.5%).
- **$E_{Outward}$**: Recorded outbound bulk dispatches to neighboring states (Meghalaya, Tripura, Nagaland).
- **$I_{Inbound\ Imports}$**: Verified inter-state iced reefer imports logged via digital gate passes at border checkposts (Srirampur, Boxirhat, Khanapara).

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│          LAYER 1: EDGE TELEMETRY & MULTIMODAL INGESTION         │
│  Offline-first PWA • Edge OCR Scanner • Bluetooth Digital Scale │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│           LAYER 2: SECURE API GATEWAY & TIME-SERIES DB          │
│   FastAPI / NestJS Microservices • PostgreSQL 16 + TimescaleDB  │
│              PostGIS Corridor Engine • Redis Streams            │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│          LAYER 3: BAYESIAN RECONCILIATION & ANOMALY CORE        │
│    Bayesian Kalman Filter • Mass-Balance Disappearance Solver   │
│             Isolation Forest • Multiple Imputation              │
└────────────────────────────────┬────────────────────────────────┘
                                 │
┌────────────────────────────────▼────────────────────────────────┐
│         LAYER 4: EXECUTIVE GOVERNANCE & INTEROPERABILITY        │
│   DFO Heatmap Workbench • Automated Discrepancy Alert Tickets   │
│         Open API Standards for PMMSY / NFDB / ASDI / ASDC       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💰 Indicative Budget Allocation (Total Grant: ₹40.00 Lakhs)

| Major Cost Head | Line Item Scope & Manpower Allocation | Allocated Cost | Share (%) |
| :--- | :--- | :---: | :---: |
| **1. Technical Engineering Team** | **Lead Systems Architect** (9 mos @ ₹75k = ₹6.75L)<br/>**Senior Data Scientist / ML Modeler** (9 mos @ ₹75k = ₹6.75L)<br/>**Mobile & Offline-First Edge Engineer** (9 mos @ ₹55.5k = ₹5.00L)<br/>**Technical QA & Security Integration Specialist** (Part-time = ₹1.50L) | **₹20.00 Lakhs** | **50.0%** |
| **2. Field Hardware, Edge Devices & Mandi Setup** | 8 Ruggedized Android tablets for highway checkposts & mandis (₹2.20L); 6 Bluetooth weighing scale bridges (₹1.80L); Handheld OCR waybill barcode scanners (₹1.50L) | **₹5.50 Lakhs** | **13.75%** |
| **3. Field Enumeration & Ground-Truthing** | **Field Operations Lead** (9 mos @ ₹30k = ₹2.70L); **3 Regional Field Enumerators** across Kamrup Metro, Nagaon, and Cachar (6 mos @ ₹15k × 3 = ₹2.70L); Local transit logistics & market survey travel (₹0.60L) | **₹6.00 Lakhs** | **15.0%** |
| **4. Cloud Infrastructure, Hosting & Security** | MeitY-empaneled sovereign cloud hosting (ASDC / AWS GovCloud) & TimescaleDB instances (₹1.60L); Mapbox vector tiles, SMS/WhatsApp API credits (₹0.90L); Third-party CERT-In empaneled VAPT security audit (₹1.00L) | **₹3.50 Lakhs** | **8.75%** |
| **5. Stakeholder Workshops & Training** | 3 District capacity-building workshops for DFDOs/FDOs (₹1.25L); Mandi Commission Agent (Aratdar) onboarding sessions & multilingual user manuals (₹1.25L) | **₹2.50 Lakhs** | **6.25%** |
| **6. Project Management, Compliance & Contingency** | Statutory CA audits, legal filings, administrative overheads, project reporting, and contingency buffer | **₹2.50 Lakhs** | **6.25%** |
| **TOTAL PROJECT COST** | **Comprehensive 9-Month Development & 3-District Pilot Validation** | **₹40.00 Lakhs** | **100.0%** |

---

## 📂 Repository Contents

```
├── PROPOSAL_FORM_TEXT.txt               # Plain-text copy-pasteable blocks for all 12 portal fields
├── PROPOSAL_SUBMISSION.md               # Markdown version of full proposal with word counts
├── index.html                           # Single-page interactive prototype & dev portal
├── output/
│   ├── NESFIC_D34_Proof_of_Work.pdf    # Primary required upload (1.4 MB)
│   └── NESFIC_D34_Additional_Supporting_Material.pdf # Secondary optional upload (252 KB)
├── assets/                              # High-resolution architectural schematics & charts
│   ├── system_architecture.png
│   ├── mass_balance_flow.png
│   ├── wireframes_dashboard.png
│   ├── pilot_simulation_chart.png
│   └── budget_breakdown_chart.png
└── scripts/                             # Generation and verification scripts
    ├── build_proposal_texts.py
    ├── generate_visuals.py
    ├── generate_proof_of_work_pdf.py
    ├── generate_supporting_material_pdf.py
    └── generate_portal_html.py
```

---

## 🚀 Running the Local Dev Server

```bash
# Start the local server
python3 -m http.server 8080

# Open in browser:
# http://localhost:8080
```

---

## ⚖️ License & Intellectual Property
Developed under the **North East Seva First Innovation Challenge (NESFIC) 2026** framework for the **Directorate of Fisheries, Government of Assam** and the **Assam Innovation & Startup Foundation (AISF)**.
