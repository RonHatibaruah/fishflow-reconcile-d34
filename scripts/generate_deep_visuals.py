import os
os.environ["MPLCONFIGDIR"] = "/tmp/matplotlib"
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs("assets", exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Multilingual Edge Mobile UI Walkthrough & WhatsApp Bot
# -----------------------------------------------------------------------------
def create_vernacular_edge_ui():
    fig, ax = plt.subplots(figsize=(12, 7.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 7.15, "MatsyaFlow Multilingual Edge UI & Conversational Ingestion", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.8, "Grassroots Field Adoption: Assamese, Bengali & English Interfaces + WhatsApp Audio Ingestion", 
            ha='center', va='center', fontsize=9, color='#475569')

    # Screen 1: Assamese Localized Transit Intake
    r1 = patches.FancyBboxPatch((0.6, 0.5), 3.4, 6.0, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#0284C7', lw=1.8)
    ax.add_patch(r1)
    ax.text(2.3, 6.2, "SCREEN 1: CHECKPOST PWA", fontsize=8.5, fontweight='bold', color='#0284C7', ha='center')
    ax.text(2.3, 5.95, "[Assamese Localized Interface]", fontsize=7.2, color='#64748B', ha='center')
    
    # Header bar
    ax.add_patch(patches.Rectangle((0.85, 5.3), 2.9, 0.45, fc='#0284C7', ec='#0369A1'))
    ax.text(2.3, 5.52, "Meen Sanchalak (Govt of Assam)", fontsize=7.2, fontweight='bold', color='#FFFFFF', ha='center')

    # Form Fields
    f1 = [
        ("Baahon No (Vehicle Registration):", "AS-01-EC-4892 (Reefer Truck)"),
        ("Probesh Sthan (Entry Checkpost):", "Srirampur Gate (Dhubri Border)"),
        ("Utsa Raajya (Origin State):", "Andhra Pradesh (Chilled)"),
        ("Maasor Jaat (Fish Variety):", "Borof Diya Rohu/Katla (IMC)"),
        ("Muth Ojon (Net Cargo Weight):", "14.85 Metric Tons (Verified)")
    ]
    for idx, (lbl, val) in enumerate(f1):
        yp = 4.65 - idx * 0.65
        ax.add_patch(patches.Rectangle((0.85, yp), 2.9, 0.52, fc='#F8FAFC', ec='#CBD5E1'))
        ax.text(0.95, yp + 0.34, lbl, fontsize=6.2, color='#475569')
        ax.text(0.95, yp + 0.14, val, fontsize=6.8, fontweight='bold', color='#0F172A')

    ax.add_patch(patches.FancyBboxPatch((1.0, 0.9), 2.6, 0.55, boxstyle="round,pad=0.05", fc='#0284C7', ec='#0369A1'))
    ax.text(2.3, 1.18, "Provesh Patra (Generate Pass)", fontsize=6.8, fontweight='bold', color='#FFFFFF', ha='center')


    # Screen 2: Bengali Localized Mandi Terminal
    r2 = patches.FancyBboxPatch((4.3, 0.5), 3.4, 6.0, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#16A34A', lw=1.8)
    ax.add_patch(r2)
    ax.text(6.0, 6.2, "SCREEN 2: MANDI AUCTION", fontsize=8.5, fontweight='bold', color='#16A34A', ha='center')
    ax.text(6.0, 5.95, "[Bengali Localized - Silchar/Cachar]", fontsize=7.0, color='#64748B', ha='center')

    ax.add_patch(patches.Rectangle((4.55, 5.3), 2.9, 0.45, fc='#16A34A', ec='#15803D'))
    ax.text(6.0, 5.52, "Paikaari Maaser Baajaar (Wholesale)", fontsize=7.2, fontweight='bold', color='#FFFFFF', ha='center')

    # Quick Tag Buttons
    ax.add_patch(patches.Rectangle((4.55, 4.5), 1.4, 0.65, fc='#DCFCE7', ec='#86EFAC'))
    ax.text(5.25, 4.82, "Sthaaniyo Beel\n(Local Catch)", fontsize=6.2, fontweight='bold', color='#166534', ha='center')

    ax.add_patch(patches.Rectangle((6.05, 4.5), 1.4, 0.65, fc='#FEE2E2', ec='#FCA5A5'))
    ax.text(6.75, 4.82, "Bohi-Raajyer Maas\n(Import Chilled)", fontsize=6.2, fontweight='bold', color='#991B1B', ha='center')

    # Bluetooth Scale Status
    ax.add_patch(patches.Rectangle((4.55, 3.7), 2.9, 0.6, fc='#F0FDF4', ec='#86EFAC'))
    ax.text(6.0, 4.08, "[BT SCALE CONNECTED]: 124.5 kg", fontsize=7.0, fontweight='bold', color='#166534', ha='center')
    ax.text(6.0, 3.85, "(Live Terminal Sync: Zero Entry Error)", fontsize=6.0, color='#15803D', ha='center')

    # Species Quick Selector
    species_btns = [("Rohu (Local Pond)", "520 kg"), ("Catla (Local Beel)", "410 kg"), ("Chital (Riverine)", "180 kg"), ("Borali (Riverine)", "240 kg")]
    for idx, (sp, wt) in enumerate(species_btns):
        yp = 3.0 - idx * 0.48
        ax.add_patch(patches.Rectangle((4.55, yp), 2.9, 0.4, fc='#F8FAFC', ec='#E2E8F0'))
        ax.text(4.65, yp + 0.2, sp, fontsize=6.5, color='#1E293B', fontweight='bold')
        ax.text(7.2, yp + 0.2, wt, fontsize=6.5, color='#0284C7', fontweight='bold', ha='right')

    ax.add_patch(patches.FancyBboxPatch((4.7, 0.9), 2.6, 0.55, boxstyle="round,pad=0.05", fc='#16A34A', ec='#15803D'))
    ax.text(6.0, 1.18, "Auction Songrokkhon (Save Lot)", fontsize=6.8, fontweight='bold', color='#FFFFFF', ha='center')


    # Screen 3: WhatsApp Conversational Voice & Text Bot
    r3 = patches.FancyBboxPatch((8.0, 0.5), 3.4, 6.0, boxstyle="round,pad=0.1", fc='#FFFFFF', ec='#25D366', lw=1.8)
    ax.add_patch(r3)
    ax.text(9.7, 6.2, "CHANNEL 3: WHATSAPP BOT", fontsize=8.5, fontweight='bold', color='#128C7E', ha='center')
    ax.text(9.7, 5.95, "[Zero-App Voice & Text Telemetry]", fontsize=7.0, color='#64748B', ha='center')

    ax.add_patch(patches.Rectangle((8.25, 5.3), 2.9, 0.45, fc='#075E54', ec='#054C44'))
    ax.text(9.7, 5.52, "MatsyaFlow Assam Bot (Verified)", fontsize=7.0, fontweight='bold', color='#FFFFFF', ha='center')

    # Chat Bubbles
    # 1. Voice Note from Trader
    ax.add_patch(patches.FancyBboxPatch((8.4, 4.4), 2.6, 0.7, boxstyle="round,pad=0.05", fc='#E7FFDB', ec='#C7F2B4'))
    ax.text(8.5, 4.85, "[AUDIO] Voice Note (0:12s - Assamese):", fontsize=6.0, color='#1E293B', fontweight='bold')
    ax.text(8.5, 4.55, '"Uzanbazar arat, 40 crates local rohu,\n1200 kg from Morigaon beel."', fontsize=5.8, color='#075E54', fontstyle='italic')

    # 2. Bot Auto-Parsed Response
    ax.add_patch(patches.FancyBboxPatch((8.4, 3.2), 2.6, 1.05, boxstyle="round,pad=0.05", fc='#FFFFFF', ec='#CBD5E1'))
    ax.text(8.5, 4.05, "[AI] MatsyaFlow NLP Parser:", fontsize=6.0, color='#0284C7', fontweight='bold')
    ax.text(8.5, 3.82, "• Location: Uzanbazar Guwahati\n• Origin: Local Beel (Morigaon)\n• Variety: IMC Rohu | Crates: 40\n• Weight: 1,200 kg | Status: LOGGED", fontsize=5.8, color='#334155')

    # 3. Confirmation slip
    ax.add_patch(patches.FancyBboxPatch((8.4, 2.1), 2.6, 0.95, boxstyle="round,pad=0.05", fc='#F0FDF4', ec='#86EFAC'))
    ax.text(8.5, 2.85, "[CONFIRMED] Receipt Generated:", fontsize=6.0, color='#16A34A', fontweight='bold')
    ax.text(8.5, 2.58, "Token ID: #UZN-2026-8941\nSigned at: 05:24 AM | Encrypted", fontsize=5.8, color='#15803D')
    ax.text(8.5, 2.25, "[Tap to View Cryptographic Slip]", fontsize=5.5, color='#0284C7', fontweight='bold')

    # Bottom note
    ax.add_patch(patches.FancyBboxPatch((8.4, 0.9), 2.6, 0.85, boxstyle="round,pad=0.05", fc='#F8FAFC', ec='#CBD5E1'))
    ax.text(9.7, 1.45, "ZERO BARRIER ENTRY", fontsize=6.8, fontweight='bold', color='#1E293B', ha='center')
    ax.text(9.7, 1.15, "Allows non-smartphone traders to\nreport volumes via ordinary WhatsApp.", fontsize=5.8, color='#64748B', ha='center')

    plt.tight_layout()
    plt.savefig("assets/vernacular_edge_ui.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/vernacular_edge_ui.png")


# -----------------------------------------------------------------------------
# 2. State & National Interoperability Architecture (PMMSY / NFDB / ASDC)
# -----------------------------------------------------------------------------
def create_interoperability_architecture():
    fig, ax = plt.subplots(figsize=(12, 6.8), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.0)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 6.6, "MatsyaFlow Enterprise & National Mission Interoperability", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.25, "Standards-Compliant REST APIs, National Open Data Standards, and State Cloud Infrastructure", 
            ha='center', va='center', fontsize=9, color='#475569')

    # 3 Horizontal Zones
    # Zone 1: External Data Ingress (Left)
    z1 = patches.FancyBboxPatch((0.5, 1.2), 3.2, 4.7, boxstyle="round,pad=0.1", fc='#EFF6FF', ec='#3B82F6', lw=1.6)
    ax.add_patch(z1)
    ax.text(2.1, 5.6, "1. UPSTREAM INGESTION", fontsize=9.0, fontweight='bold', color='#1D4ED8', ha='center')
    
    in_items = [
        ("Highway Transit Checkposts", "Srirampur & Boxirhat border OCR manifests"),
        ("Wholesale Mandi IoT", "Bluetooth scale streams & Aratdar logs"),
        ("FASTag / e-Way Webhooks", "Automated highway toll cross-reference"),
        ("Household Dietary Surveys", "NSSO / NFHS-5 rural consumption curves")
    ]
    for idx, (head, desc) in enumerate(in_items):
        yp = 4.6 - idx * 1.05
        ax.add_patch(patches.Rectangle((0.7, yp), 2.8, 0.85, fc='#FFFFFF', ec='#BFDBFE'))
        ax.text(0.8, yp + 0.6, head, fontsize=7.2, fontweight='bold', color='#1E293B')
        ax.text(0.8, yp + 0.3, desc, fontsize=6.2, color='#475569')

    # Zone 2: Central MatsyaFlow Core (Center)
    z2 = patches.FancyBboxPatch((4.2, 1.2), 3.6, 4.7, boxstyle="round,pad=0.1", fc='#F8FAFC', ec='#0284C7', lw=2.0)
    ax.add_patch(z2)
    ax.text(6.0, 5.6, "2. MATSYAFLOW ASSAM CORE", fontsize=9.0, fontweight='bold', color='#0284C7', ha='center')
    ax.text(6.0, 5.35, "[Assam State Data Centre - ASDC]", fontsize=6.8, color='#64748B', ha='center')

    core_items = [
        ("FastAPI / NestJS Microservices", "Containerized on MeitY GovCloud"),
        ("PostgreSQL 16 + TimescaleDB", "Spatial PostGIS corridor routing"),
        ("Bayesian State-Space Filter", "Solves Mass-Balance disappearance loop"),
        ("Zero-Trust Security & RBAC", "e-Pramaan Single Sign-On (SSO)")
    ]
    for idx, (head, desc) in enumerate(core_items):
        yp = 4.35 - idx * 0.95
        ax.add_patch(patches.Rectangle((4.4, yp), 3.2, 0.78, fc='#F0F9FF', ec='#BAE6FD'))
        ax.text(4.55, yp + 0.52, head, fontsize=7.2, fontweight='bold', color='#0369A1')
        ax.text(4.55, yp + 0.24, desc, fontsize=6.2, color='#334155')

    # Zone 3: Downstream Government Platforms (Right)
    z3 = patches.FancyBboxPatch((8.3, 1.2), 3.2, 4.7, boxstyle="round,pad=0.1", fc='#F0FDF4', ec='#22C55E', lw=1.6)
    ax.add_patch(z3)
    ax.text(9.9, 5.6, "3. NATIONAL & STATE EXPORT", fontsize=9.0, fontweight='bold', color='#15803D', ha='center')

    out_items = [
        ("PMMSY National Portal", "Central subsidy & infrastructure allocation"),
        ("NFDB Dashboard", "National inland fisheries statistical returns"),
        ("DFO Executive Workbench", "District GIS heatmap & anomaly audit tickets"),
        ("State Statistical Gazette", "Defensible annual fish production returns")
    ]
    for idx, (head, desc) in enumerate(out_items):
        yp = 4.6 - idx * 1.05
        ax.add_patch(patches.Rectangle((8.5, yp), 2.8, 0.85, fc='#FFFFFF', ec='#BBF7D0'))
        ax.text(8.6, yp + 0.6, head, fontsize=7.2, fontweight='bold', color='#1E293B')
        ax.text(8.6, yp + 0.3, desc, fontsize=6.2, color='#475569')

    # Arrows between zones
    ax.annotate('', xy=(4.2, 3.5), xytext=(3.7, 3.5),
                arrowprops=dict(facecolor='#0284C7', edgecolor='#0284C7', arrowstyle="->", lw=2.5))
    ax.annotate('', xy=(8.3, 3.5), xytext=(7.8, 3.5),
                arrowprops=dict(facecolor='#16A34A', edgecolor='#16A34A', arrowstyle="->", lw=2.5))

    # Bottom Compliance Pill
    ax.add_patch(patches.FancyBboxPatch((1.0, 0.4), 10.0, 0.65, boxstyle="round,pad=0.06", fc='#1E293B', ec='#0F172A'))
    ax.text(6.0, 0.72, "COMPLIANCE: OPEN API SPEC 3.0 • NDSAP DATA SHARING • CERT-In AUDITED • MeitY SOVEREIGN HOSTING", 
            ha='center', va='center', fontsize=7.2, fontweight='bold', color='#38BDF8')

    plt.tight_layout()
    plt.savefig("assets/interoperability_architecture.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/interoperability_architecture.png")


# -----------------------------------------------------------------------------
# 3. Closed-Loop Anomaly Detection & DFO Ground-Truthing Audit Protocol
# -----------------------------------------------------------------------------
def create_closed_loop_audit():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.8)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 6.35, "Closed-Loop Statistical Anomaly & Field Audit Protocol", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.0, "Human-in-the-Loop Governance Ensuring Algorithmic Flags Are Empirically Verified by Departmental Officers", 
            ha='center', va='center', fontsize=9, color='#475569')

    steps = [
        {"x": 0.6, "w": 2.5, "step": "STAGE 1: ALGORITHMIC FLAG", "title": "Anomaly Detected", 
         "desc": "• Mass-balance engine flags\n  +24% unexplained surplus in\n  Nagaon-West beel cluster.\n• Reported production exceeds\n  mandi capacity & outward transit.\n• Isolation Forest trigger.",
         "fc": "#FEF2F2", "ec": "#EF4444", "tc": "#991B1B"},

        {"x": 3.4, "w": 2.5, "step": "STAGE 2: DFO ADVISORY", "title": "Audit Ticket Generated", 
         "desc": "• System generates digital ticket\n  #D34-AUD-042 on DFO console.\n• Highlights spatial boundary\n  and discrepancy magnitude.\n• Human DFO authorizes targeted\n  field ground-truthing.",
         "fc": "#FFFBEB", "ec": "#F59E0B", "tc": "#B45309"},

        {"x": 6.2, "w": 2.5, "step": "STAGE 3: SPOT INSPECTION", "title": "FDO Field Verification", 
         "desc": "• Local Fishery Demonstration\n  Officer (FDO) dispatched.\n• Uses mobile app to capture\n  geotagged pond/beel catch logs.\n• Verifies actual harvesting\n  frequency & inventory balances.",
         "fc": "#EFF6FF", "ec": "#3B82F6", "tc": "#1D4ED8"},

        {"x": 9.0, "w": 2.5, "step": "STAGE 4: RESOLUTION", "title": "Gazette Sign-Off", 
         "desc": "• Reconciled model tuned with\n  ground-truthed field report.\n• Cryptographic hash recorded\n  preventing retroactive edits.\n• Final district production\n  approved by Directorate.",
         "fc": "#F0FDF4", "ec": "#22C55E", "tc": "#15803D"}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 1.3), s["w"], 4.3, boxstyle="round,pad=0.1", fc=s["fc"], ec=s["ec"], lw=1.8)
        ax.add_patch(box)
        ax.text(s["x"]+s["w"]/2, 5.25, s["step"], fontsize=7.2, fontweight='bold', color=s["tc"], ha='center')
        ax.text(s["x"]+s["w"]/2, 4.85, s["title"], fontsize=9.0, fontweight='bold', color='#0F172A', ha='center')
        ax.text(s["x"]+0.2, 4.4, s["desc"], fontsize=7.5, color='#334155', va='top')

    # Step transition arrows
    for xa in [3.1, 5.9, 8.7]:
        ax.annotate('', xy=(xa + 0.3, 3.4), xytext=(xa, 3.4),
                    arrowprops=dict(facecolor='#0F172A', edgecolor='#0F172A', arrowstyle="->", lw=2.2))

    # Bottom Policy Banner
    ax.add_patch(patches.FancyBboxPatch((0.6, 0.4), 10.9, 0.65, boxstyle="round,pad=0.06", fc='#FFFFFF', ec='#CBD5E1'))
    ax.text(6.0, 0.72, "GOVERNANCE PRINCIPLE: Algorithms provide advisory flags; human DFOs maintain ultimate administrative authority.", 
            ha='center', va='center', fontsize=7.5, fontstyle='italic', color='#475569')

    plt.tight_layout()
    plt.savefig("assets/closed_loop_audit_protocol.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/closed_loop_audit_protocol.png")


# -----------------------------------------------------------------------------
# 4. Commercial Species Disaggregation & Trade Pathways Matrix
# -----------------------------------------------------------------------------
def create_species_matrix():
    fig, ax = plt.subplots(figsize=(12, 6.2), dpi=300)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.8)
    ax.axis('off')
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    ax.text(6, 6.35, "Commercial Fish Species Disaggregation & Supply Chain Matrix", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(6, 6.0, "Differentiating High-Import Trade Commodities from Native Riverine & Wetland Indigenous Species", 
            ha='center', va='center', fontsize=9, color='#475569')

    classes = [
        {"x": 0.6, "w": 3.4, "title": "CLASS A: INDIAN MAJOR CARPS", "sub": "Rohu, Catla, Mrigal (IMC)",
         "desc": "• Highest volume commercial fish in Assam.\n• HYBRID SUPPLY DYNAMICS:\n  - 45% Local aquaculture & beels.\n  - 55% Interstate iced imports (AP & WB).\n• Reconciliation Impact:\n  Crucial to tag origin at checkposts\n  to prevent false production claims.",
         "fc": "#EFF6FF", "ec": "#0284C7", "tc": "#0369A1"},

        {"x": 4.3, "w": 3.4, "title": "CLASS B: INDIGENOUS RIVERINE", "sub": "Chital, Borali, Magur, Singhi, Ilish",
         "desc": "• Premium price delicacies (Rs 600 - Rs 1,500/kg).\n• STRICTLY NATIVE SUPPLY DYNAMICS:\n  - 100% Native riverine & beel capture.\n  - 0% Out-of-state iced imports.\n• Reconciliation Impact:\n  Tracked via dawn mandi auctions and\n  river landing center Bluetooth scales.",
         "fc": "#F0FDF4", "ec": "#16A34A", "tc": "#15803D"},

        {"x": 8.0, "w": 3.4, "title": "CLASS C: EXOTIC & COMMERCIAL", "sub": "Grass Carp, Silver Carp, Pangasius",
         "desc": "• High-density commercial pond culture.\n• LOCALIZED SUPPLY DYNAMICS:\n  - 85% Local commercial farm harvest.\n  - 15% Inter-district bulk movement.\n• Reconciliation Impact:\n  Modeled using feed consumption\n  indices and local cold storage balances.",
         "fc": "#FEF3C7", "ec": "#D97706", "tc": "#B45309"}
    ]

    for c in classes:
        box = patches.FancyBboxPatch((c["x"], 0.9), c["w"], 4.7, boxstyle="round,pad=0.1", fc=c["fc"], ec=c["ec"], lw=1.8)
        ax.add_patch(box)
        ax.text(c["x"]+c["w"]/2, 5.25, c["title"], fontsize=8.5, fontweight='bold', color=c["tc"], ha='center')
        ax.text(c["x"]+c["w"]/2, 4.9, c["sub"], fontsize=7.2, color='#475569', ha='center', fontstyle='italic')
        ax.text(c["x"]+0.25, 4.4, c["desc"], fontsize=7.6, color='#1E293B', va='top')

    # Bottom Pill
    ax.add_patch(patches.FancyBboxPatch((0.6, 0.3), 10.8, 0.45, boxstyle="round,pad=0.04", fc='#1E293B', ec='#0F172A'))
    ax.text(6.0, 0.52, "TAXONOMIC PURITY: Categorical disaggregation ensures external chilled carps never contaminate native riverine yield figures.", 
            ha='center', va='center', fontsize=7.0, fontweight='bold', color='#38BDF8')

    plt.tight_layout()
    plt.savefig("assets/species_disaggregation_matrix.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print("Generated assets/species_disaggregation_matrix.png")

if __name__ == "__main__":
    create_vernacular_edge_ui()
    create_interoperability_architecture()
    create_closed_loop_audit()
    create_species_matrix()
