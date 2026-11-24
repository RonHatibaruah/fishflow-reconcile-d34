import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        if self._pageNumber > 1:
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(54, letter[1] - 36, "NESFIC-D-34: Additional Supporting Material | Indicative Budget & Annexures")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
            
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(54, 36, "Government of Assam — North East Seva First Innovation Challenge (NESFIC) 2026")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(letter[0] - 54, 36, page_text)
            self.line(54, 46, letter[0] - 54, 46)
        self.restoreState()

def build_supporting_material_pdf(filename="output/NESFIC_D34_Additional_Supporting_Material.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0284C7'),
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=9,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=13.0,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.0,
        leading=11.0,
        textColor=colors.HexColor('#1E293B')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor('#FFFFFF')
    )

    story = []

    # -------------------------------------------------------------------------
    # COVER / HEADER
    # -------------------------------------------------------------------------
    story.append(Paragraph("ADDITIONAL SUPPORTING MATERIAL & BUDGET", title_style))
    story.append(Paragraph("<b>Problem Statement NESFIC-D-34:</b> Fish-Flow and Market Data for Independent Validation of Annual Fish Production Estimates", subtitle_style))
    
    # Meta Box
    meta_data = [
        [Paragraph("<b>Grant Program:</b> NESFIC 2026 (Assam Innovation & Startup Foundation)", table_cell),
         Paragraph("<b>Department:</b> Directorate of Fisheries, Govt of Assam", table_cell)],
        [Paragraph("<b>Total Sanction Limit:</b> ₹40.00 Lakhs (40 lacs)", table_cell),
         Paragraph("<b>Technical Engineering Share:</b> ₹20.00 Lakhs (50.0%)", table_cell)]
    ]
    t_meta = Table(meta_data, colWidths=[250, 254])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------------------
    # 1. Indicative Budget Allocation (Total ₹40 Lakhs)
    # -------------------------------------------------------------------------
    story.append(Paragraph("1. Comprehensive Budget Breakdown (Total Grant: ₹40.00 Lakhs)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=8))
    
    intro_budget = ("In strict alignment with the problem statement grant of ₹40.00 Lakhs, the budget allocates "
                    "<b>₹20.00 Lakhs (50.0%)</b> directly to the Technical Engineering Team to guarantee robust core algorithm "
                    "development, offline-first edge architecture, and spatial database engineering, while appropriately sizing "
                    "all complementary field, hardware, cloud, and governance heads:")
    story.append(Paragraph(intro_budget, body_style))
    story.append(Spacer(1, 4))

    budget_table_data = [
        [Paragraph("<b>Major Cost Head</b>", table_header), 
         Paragraph("<b>Line Item Description & Manpower / Resource Justification</b>", table_header), 
         Paragraph("<b>Allocated Cost (₹ Lakhs)</b>", table_header), 
         Paragraph("<b>Share (%)</b>", table_header)],
        
        [Paragraph("<b>1. Technical Engineering Team</b>", table_cell),
         Paragraph("• <b>Lead Fullstack & Systems Architect:</b> Overall software architecture, API gateway, PostGIS database & cloud security (9 months @ ₹75k/mo = ₹6.75L)<br/>"
                   "• <b>Senior Data Scientist / ML Modeler:</b> Bayesian mass-balance state-space filters, anomaly detection & multiple imputation (9 months @ ₹75k/mo = ₹6.75L)<br/>"
                   "• <b>Mobile & Offline-First Edge Engineer:</b> Flutter PWA, edge OCR waybill scanner, Bluetooth scale sync & WhatsApp bot (9 months @ ₹55.5k/mo = ₹5.00L)<br/>"
                   "• <b>Technical QA & Security Integration Specialist:</b> Unit test suites, load testing & ASDC deployment (Part-time = ₹1.50L)", table_cell),
         Paragraph("<b>₹20.00</b>", table_cell),
         Paragraph("<b>50.0%</b>", table_cell)],

        [Paragraph("<b>2. Field Hardware, Edge Devices & Mandi Setup</b>", table_cell),
         Paragraph("• 8 Ruggedized IP67 Android Tablets for highway checkposts (Srirampur, Boxirhat, Khanapara) & mandis (₹2.20L)<br/>"
                   "• 6 Industrial Bluetooth-enabled weighing scale bridge converters & IoT telemetry units (₹1.80L)<br/>"
                   "• High-speed handheld 2D waybill barcode/OCR scanners, solar power banks & waterproof casings (₹1.50L)", table_cell),
         Paragraph("<b>₹5.50</b>", table_cell),
         Paragraph("<b>13.75%</b>", table_cell)],

        [Paragraph("<b>3. Field Enumeration & Ground-Truthing</b>", table_cell),
         Paragraph("• <b>Field Operations Lead:</b> On-ground coordination across 3 pilot districts (9 months @ ₹30k/mo = ₹2.70L)<br/>"
                   "• <b>3 Regional Field Enumerators:</b> Stationed at Kamrup Metro, Nagaon, and Cachar wholesale yards & checkposts (6 months @ ₹15k/mo × 3 = ₹2.70L)<br/>"
                   "• Local field transit, logistics, fuel allowances & market survey travel (₹0.60L)", table_cell),
         Paragraph("<b>₹6.00</b>", table_cell),
         Paragraph("<b>15.0%</b>", table_cell)],

        [Paragraph("<b>4. Cloud Infrastructure, Hosting & Security</b>", table_cell),
         Paragraph("• MeitY-empaneled sovereign cloud hosting (ASDC / AWS GovCloud) & TimescaleDB high-throughput instances (₹1.60L)<br/>"
                   "• High-resolution GIS vector tiles (Mapbox), Twilio/Gupshup WhatsApp Business API & SMS credits (₹0.90L)<br/>"
                   "• Comprehensive third-party CERT-In empaneled VAPT security audit & penetration testing (₹1.00L)", table_cell),
         Paragraph("<b>₹3.50</b>", table_cell),
         Paragraph("<b>8.75%</b>", table_cell)],

        [Paragraph("<b>5. Stakeholder Workshops & Training</b>", table_cell),
         Paragraph("• 3 District capacity-building workshops for DFDOs, Fishery Demonstration Officers, and statistical clerks (₹1.25L)<br/>"
                   "• Mandi Commission Agent (Aratdar) association onboarding, multilingual manuals (Assamese/Bengali) (₹1.25L)", table_cell),
         Paragraph("<b>₹2.50</b>", table_cell),
         Paragraph("<b>6.25%</b>", table_cell)],

        [Paragraph("<b>6. Project Management & Contingency</b>", table_cell),
         Paragraph("• Statutory CA financial audit, legal filings, utility overheads, project reporting & contingency reserve (₹2.50L)", table_cell),
         Paragraph("<b>₹2.50</b>", table_cell),
         Paragraph("<b>6.25%</b>", table_cell)],

        [Paragraph("<b>TOTAL GRANT ALLOCATION</b>", table_header),
         Paragraph("<b>Fully Balanced Project Budget for 9-Month Development & 3-District Validation</b>", table_header),
         Paragraph("<b>₹40.00</b>", table_header),
         Paragraph("<b>100.0%</b>", table_header)]
    ]

    t_budget = Table(budget_table_data, colWidths=[110, 260, 74, 60])
    t_budget.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#0284C7')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_budget)
    story.append(Spacer(1, 8))

    if os.path.exists("assets/budget_breakdown_chart.png"):
        story.append(Image("assets/budget_breakdown_chart.png", width=6.2*inch, height=3.58*inch))
    
    story.append(PageBreak())

    # -------------------------------------------------------------------------
    # 2. Work Breakdown Structure (WBS) & Deliverables
    # -------------------------------------------------------------------------
    story.append(Paragraph("2. Work Breakdown Structure (WBS) & Deliverables", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=8))

    wbs_data = [
        [Paragraph("<b>Phase & Month</b>", table_header), 
         Paragraph("<b>Major Work Packages & Engineering Activities</b>", table_header), 
         Paragraph("<b>Verifiable Output / Deliverable</b>", table_header)],
        
        [Paragraph("<b>Phase 1</b><br/>(M1 – M2)", table_cell),
         Paragraph("• WP 1.1: Directorate stakeholder discovery & institutional alignment.<br/>"
                   "• WP 1.2: Physical corridor mapping of Srirampur, Boxirhat, and Khanapara.<br/>"
                   "• WP 1.3: Mathematical parameterization of Mass-Balance equation.", table_cell),
         Paragraph("• Inception Report & Stakeholder MOU<br/>"
                   "• Corridor Reconnaissance Survey<br/>"
                   "• System Requirements Specification (SRS)", table_cell)],

        [Paragraph("<b>Phase 2</b><br/>(M3 – M4)", table_cell),
         Paragraph("• WP 2.1: TimescaleDB & PostGIS cloud database deployment.<br/>"
                   "• WP 2.2: Development of offline-first Flutter Transit Logger PWA.<br/>"
                   "• WP 2.3: Edge OCR waybill scanner and Bluetooth weighing scale integration.", table_cell),
         Paragraph("• Core Database & API Gateway v0.5<br/>"
                   "• Alpha Prototype Mobile Applications<br/>"
                   "• Lab Usability Benchmark Report", table_cell)],

        [Paragraph("<b>Phase 3</b><br/>(M5 – M6)", table_cell),
         Paragraph("• WP 3.1: Bayesian state-space filter & Kalman reconciliation coding.<br/>"
                   "• WP 3.2: Automated anomaly detection algorithms (Isolation Forests).<br/>"
                   "• WP 3.3: Executive DFO GIS Workbench and discrepancy ticket system.", table_cell),
         Paragraph("• Reconciled Analytics Engine (v1.0)<br/>"
                   "• Executive DFO Management Console<br/>"
                   "• Pre-Pilot Simulation Benchmark Report", table_cell)],

        [Paragraph("<b>Phase 4</b><br/>(M7 – M9)", table_cell),
         Paragraph("• WP 4.1: Live 60-day field pilot deployment across Kamrup (M), Nagaon, Cachar.<br/>"
                   "• WP 4.2: Comprehensive CERT-In third-party VAPT security audit.<br/>"
                   "• WP 4.3: Departmental capacity building, training, and final handover.", table_cell),
         Paragraph("• 3-District Live Pilot Validation Report<br/>"
                   "• CERT-In Compliance Certificate<br/>"
                   "• Production Source Code & Knowledge Transfer", table_cell)]
    ]

    t_wbs = Table(wbs_data, colWidths=[75, 275, 154])
    t_wbs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_wbs)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------------------
    # 3. Risk Mitigation Matrix
    # -------------------------------------------------------------------------
    story.append(Paragraph("3. Risk Mitigation Matrix", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=8))

    risk_data = [
        [Paragraph("<b>Identified Risk Factor</b>", table_header), 
         Paragraph("<b>Likelihood / Impact</b>", table_header), 
         Paragraph("<b>Engineered Mitigation Strategy & Safeguards</b>", table_header)],
        
        [Paragraph("<b>1. Mandi Trader Reluctance</b><br/>(Reluctance to share transaction volumes)", table_cell),
         Paragraph("Moderate / High", table_cell),
         Paragraph("<b>Differential Privacy & Aggregation:</b> System strictly ingests aggregated tonnage and broad species class. Zero pricing or individual financial turnover data is collected; traders are insulated from commercial surveillance.", table_cell)],

        [Paragraph("<b>2. Intermittent Checkpost Connectivity</b><br/>(Remote border gate connectivity drops)", table_cell),
         Paragraph("High / Moderate", table_cell),
         Paragraph("<b>Offline-First Architecture:</b> Edge PWAs use client-side IndexedDB/SQLite. Transactions are signed locally and automatically synchronized with conflict-free replication upon network reconnection.", table_cell)],

        [Paragraph("<b>3. Night-Time Transit Bypass</b><br/>(Fish reefers entering during off-duty hours)", table_cell),
         Paragraph("Moderate / Moderate", table_cell),
         Paragraph("<b>Bayesian Multiple Imputation:</b> Engine automatically imputes unmonitored window inflows using historical time-of-day distributions and downstream morning mandi arrival surges.", table_cell)],

        [Paragraph("<b>4. Resistance to New Technology</b><br/>(Field enumerators accustomed to paper)", table_cell),
         Paragraph("Moderate / Moderate", table_cell),
         Paragraph("<b>Multimodal Low-Friction Entry:</b> Support for WhatsApp audio/text bots, optical waybill scanning, and localized interfaces in Assamese, Bengali, and Bodo requiring zero manual typing.", table_cell)]
    ]

    t_risk = Table(risk_data, colWidths=[130, 80, 294])
    t_risk.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_risk)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------------------
    # 4. Compliance & Institutional Undertaking
    # -------------------------------------------------------------------------
    story.append(Paragraph("4. Regulatory Compliance & Institutional Undertaking", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=8))

    comp_text = ("We hereby certify that the proposed MatsyaFlow-Assam solution complies fully with all applicable laws and regulations: "
                 "(1) <b>Digital Personal Data Protection (DPDP) Act 2023:</b> All personally identifiable data is pseudonymized and cryptographically hashed at the edge; "
                 "(2) <b>National Data Sharing and Accessibility Policy (NDSAP):</b> Built with open REST API standards for inter-operability with PMMSY and NFDB; "
                 "(3) <b>MeitY Cloud Guidelines:</b> Hosted exclusively on sovereign, MeitY-empaneled state data centers (ASDC); "
                 "(4) <b>Zero Commercial IP Lock-in:</b> Complete source code and analytical models will be handed over to the Directorate of Fisheries upon project completion.")
    story.append(Paragraph(comp_text, body_style))
    story.append(Spacer(1, 6))

    undertaking_box = [
        [Paragraph("<b>FORMAL DECLARATION OF COMPLIANCE — NESFIC 2026</b>", table_header), Paragraph("", table_header)],
        [Paragraph("We solemnly affirm that the information submitted in this proposal is authentic, and that the budget breakdown (Total: ₹40.00 Lakhs, with ₹20.00 Lakhs dedicated to the Technical Engineering Team) reflects a prudent, realistic, and deliverable operational cost model for the Government of Assam.", table_cell),
         Paragraph("<b>Authorized Signatory:</b><br/>Lead Technical Architect & PI<br/>MatsyaFlow Consortium<br/>Date: 25th November 2026", table_cell)]
    ]
    t_under = Table(undertaking_box, colWidths=[310, 194])
    t_under.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0284C7')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#0284C7')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_under)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_supporting_material_pdf()
