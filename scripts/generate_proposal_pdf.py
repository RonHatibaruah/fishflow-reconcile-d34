import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

sys.path.append("scripts")
from build_proposal_texts import sections

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
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#0284C7"))
            self.drawString(54, letter[1] - 34, "NESFIC 2026 | GOVERNMENT TRACK PROPOSAL")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawRightString(letter[0] - 54, letter[1] - 34, "NESFIC-D-34: MatsyaFlow-Assam")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, letter[1] - 40, letter[0] - 54, letter[1] - 40)
            
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#64748B"))
            self.drawString(54, 34, "Directorate of Fisheries, Govt of Assam & Assam Innovation & Startup Foundation (AISF)")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(letter[0] - 54, 34, page_text)
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 44, letter[0] - 54, 44)
        self.restoreState()

def build_proposal_pdf(filename="output/NESFIC_D34_Proposal_Document.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    doc_title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=6
    )

    doc_subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0284C7'),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15.5,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=12,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=7,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.6,
        leading=12.5,
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
    story.append(Paragraph("TECHNICAL & COMMERCIAL PROPOSAL DOSSIER", doc_title_style))
    story.append(Paragraph("<b>Problem Statement NESFIC-D-34:</b> Fish-Flow and Market Data for Independent Validation of Annual Fish Production Estimates", doc_subtitle_style))
    
    meta_data = [
        [Paragraph("<b>Innovation Challenge:</b> North East Seva First Innovation Challenge (NESFIC) 2026", table_cell),
         Paragraph("<b>Department:</b> Directorate of Fisheries, Govt of Assam", table_cell)],
        [Paragraph("<b>Proposed Solution:</b> MatsyaFlow-Assam Reconciled System", table_cell),
         Paragraph("<b>Sponsoring Body:</b> Assam Innovation & Startup Foundation (AISF)", table_cell)],
        [Paragraph("<b>Total Project Grant:</b> ₹40.00 Lakhs (40 lacs)", table_cell),
         Paragraph("<b>Technical Engineering Allocation:</b> ₹20.00 Lakhs (50.0%)", table_cell)],
        [Paragraph("<b>Target Pilot Districts:</b> Kamrup Metro, Nagaon, Cachar", table_cell),
         Paragraph("<b>Project Duration:</b> 9 Months (4 Sequential Phases)", table_cell)]
    ]
    t_meta = Table(meta_data, colWidths=[250, 254])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------------------
    # SECTIONS 1 TO 12 WITH INTEGRATED DIAGRAMS
    # -------------------------------------------------------------------------
    for title, text in sections.items():
        story.append(Paragraph(f"{title}", h1_style))
        story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor('#0284C7'), spaceBefore=2, spaceAfter=5))
        
        paras = text.strip().split("\n\n")
        for p in paras:
            p_clean = p.strip().replace("\n", "<br/>")
            if p_clean.startswith("Current Workflow") or p_clean.startswith("Target Users") or \
               p_clean.startswith("Specific Gaps") or p_clean.startswith("Intended Outcomes") or \
               p_clean.startswith("System Architecture") or p_clean.startswith("User Interaction") or \
               p_clean.startswith("Transformative Shift") or p_clean.startswith("Proposed User Journey") or \
               p_clean.startswith("Wireframes & UI") or p_clean.startswith("Prototype & Proof of Work") or \
               p_clean.startswith("Architectural Layers") or p_clean.startswith("Sequential Development") or \
               p_clean.startswith("Detailed Timeline") or p_clean.startswith("Core Data Categories") or \
               p_clean.startswith("Data Processing") or p_clean.startswith("Explicit Assumptions") or \
               p_clean.startswith("Key Personnel") or p_clean.startswith("Indicative Manpower") or \
               p_clean.startswith("Development Testing") or p_clean.startswith("Performance & Quality") or \
               p_clean.startswith("Prior Research") or p_clean.startswith("Key Security") or \
               p_clean.startswith("Safety, Human-Review") or p_clean.startswith("Interoperability") or \
               p_clean.startswith("Novel Technological") or p_clean.startswith("Comparison with") or \
               p_clean.startswith("Basis of Differentiation") or p_clean.startswith("Intellectual Property") or \
               p_clean.startswith("Key Project Risks") or p_clean.startswith("Pilot Validation"):
                story.append(Paragraph(f"<b>{p_clean}</b>", h2_style))
            else:
                story.append(Paragraph(p_clean, body_style))
        
        # Diagram 1: Market Fallacy after Section 1
        if "1. Problem understanding" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/market_fallacy_infographic.png"):
                story.append(Image("assets/market_fallacy_infographic.png", width=6.5*inch, height=3.35*inch))
        
        # Diagram 2: Assam Strategic Corridor Map & Closed-Loop Protocol after Section 2
        elif "2. Proposed solution" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/assam_corridor_map.png"):
                story.append(Image("assets/assam_corridor_map.png", width=6.5*inch, height=3.9*inch))
            story.append(Spacer(1, 4))
            if os.path.exists("assets/closed_loop_audit_protocol.png"):
                story.append(Image("assets/closed_loop_audit_protocol.png", width=6.5*inch, height=3.35*inch))
        
        # Diagram 3: Vernacular Edge UI after Section 3
        elif "3. Describe User Journey" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/vernacular_edge_ui.png"):
                story.append(Image("assets/vernacular_edge_ui.png", width=6.5*inch, height=3.9*inch))

        # Diagram 4: System Architecture & Interoperability after Section 4
        elif "4. Technology & solution architecture" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/system_architecture.png"):
                story.append(Image("assets/system_architecture.png", width=6.5*inch, height=4.06*inch))
            story.append(Spacer(1, 4))
            if os.path.exists("assets/interoperability_architecture.png"):
                story.append(Image("assets/interoperability_architecture.png", width=6.5*inch, height=3.68*inch))

        # Diagram 5: Implementation Gantt Chart after Section 6
        elif "6. Development timeline & milestones" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/implementation_gantt.png"):
                story.append(Image("assets/implementation_gantt.png", width=6.5*inch, height=3.03*inch))

        # Diagram 6: Species Matrix after Section 7
        elif "7. Data & information requirements" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/species_disaggregation_matrix.png"):
                story.append(Image("assets/species_disaggregation_matrix.png", width=6.5*inch, height=3.35*inch))

        # Diagram 7: Budget Donut Chart & Pilot District Profiles after Section 12
        elif "12. Resources, risks & pilot validation" in title:
            story.append(Spacer(1, 4))
            if os.path.exists("assets/budget_breakdown_chart.png"):
                story.append(Image("assets/budget_breakdown_chart.png", width=5.6*inch, height=3.24*inch))
            story.append(Spacer(1, 4))
            if os.path.exists("assets/pilot_district_profiles.png"):
                story.append(Image("assets/pilot_district_profiles.png", width=6.5*inch, height=3.25*inch))
        
        story.append(Spacer(1, 6))

    # Formal Institutional Sign-off Block
    story.append(Spacer(1, 8))
    sign_box = [
        [Paragraph("<b>OFFICIAL SUBMISSION CERTIFICATION — NESFIC 2026</b>", table_header), Paragraph("", table_header)],
        [Paragraph("<b>Submitted By:</b> MatsyaFlow Consortium<br/><b>Designated Contact:</b> Principal Investigator & Lead Systems Architect<br/><b>Entity Type:</b> Registered Technology Startup & Research Enterprise", table_cell),
         Paragraph("<b>Sponsoring Department:</b> Directorate of Fisheries, Govt of Assam<br/><b>Challenge Track:</b> Departmental / Government Innovation (D-34)<br/><b>Date of Proposal:</b> November 2026", table_cell)]
    ]
    t_sign = Table(sign_box, colWidths=[250, 254])
    t_sign.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_proposal_pdf()
