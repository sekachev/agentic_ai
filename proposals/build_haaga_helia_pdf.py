from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    Flowable,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT = "proposals/Agentic_AI_for_Hospitality_Haaga_Helia_Proposal.pdf"

ACCENT = colors.HexColor("#0F766E")
DARK = colors.HexColor("#111827")
MUTED = colors.HexColor("#4B5563")
LIGHT = colors.HexColor("#ECFDF5")
LINE = colors.HexColor("#D1D5DB")
SOFT = colors.HexColor("#F8FAFC")
GOLD = colors.HexColor("#B45309")


class Rule(Flowable):
    def __init__(self, color=ACCENT, thickness=1.2):
        super().__init__()
        self.color = color
        self.thickness = thickness
        self.height = 6

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.width, 3)


def on_page(canvas, doc):
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.4)
    canvas.line(18 * mm, 16 * mm, width - 18 * mm, 16 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MUTED)
    footer = (
        "Lecturer: Nikolay Sekachev | AI for Business Leaders, Stockholm School of Economics in Riga | "
        "sekachev.ee | sekachev@gmail.com"
    )
    canvas.drawString(18 * mm, 10 * mm, footer)
    canvas.drawRightString(width - 18 * mm, 10 * mm, str(doc.page))
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    base.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=27,
            leading=31,
            textColor=DARK,
            spaceAfter=12,
            alignment=TA_LEFT,
        )
    )
    base.add(
        ParagraphStyle(
            name="CoverSub",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=13.8,
            leading=19,
            textColor=MUTED,
            spaceAfter=16,
        )
    )
    base.add(
        ParagraphStyle(
            name="H1Custom",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=17,
            leading=21,
            textColor=DARK,
            spaceBefore=4,
            spaceAfter=8,
        )
    )
    base.add(
        ParagraphStyle(
            name="H2Custom",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12.1,
            leading=15.5,
            textColor=ACCENT,
            spaceBefore=8,
            spaceAfter=5,
        )
    )
    base.add(
        ParagraphStyle(
            name="BodyCustom",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=12.9,
            textColor=DARK,
            spaceAfter=6,
        )
    )
    base.add(
        ParagraphStyle(
            name="Small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.25,
            leading=10.8,
            textColor=MUTED,
            spaceAfter=4,
        )
    )
    base.add(
        ParagraphStyle(
            name="Callout",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=12.7,
            leading=16.5,
            textColor=DARK,
            spaceAfter=0,
        )
    )
    base.add(
        ParagraphStyle(
            name="TableText",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.05,
            leading=10.6,
            textColor=DARK,
        )
    )
    base.add(
        ParagraphStyle(
            name="TableHead",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=8.25,
            leading=10.7,
            textColor=colors.white,
        )
    )
    return base


S = styles()


def p(text, style="BodyCustom"):
    return Paragraph(text, S[style])


def bullets(items, size="BodyCustom"):
    return ListFlowable(
        [ListItem(p(item, size), leftIndent=10, bulletColor=ACCENT) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletIndent=5,
    )


def callout(text, color=LIGHT, border=colors.HexColor("#99F6E4")):
    table = Table([[p(text, "Callout")]], colWidths=[165 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("BOX", (0, 0), (-1, -1), 0.7, border),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    return table


def card(title, body_items):
    table = Table([[p(title, "H2Custom")], [bullets(body_items, "Small")]], colWidths=[78 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SOFT),
                ("BOX", (0, 0), (-1, -1), 0.55, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return table


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=22 * mm,
        title="Agentic AI for Hospitality Proposal",
        author="Nikolay Sekachev",
    )

    story = []
    story.append(p("Agentic AI for Hospitality", "CoverTitle"))
    story.append(p("Next-Level AI Systems for Hotels, Restaurants and Service Businesses", "CoverSub"))
    story.append(Rule())
    story.append(Spacer(1, 8))
    story.append(
        callout(
            "Agentic AI is the next level in the practical evolution of AI: from isolated model outputs to systems that understand context, use tools, work with business data, follow workflows, ask for approval and produce traceable results."
        )
    )
    story.append(Spacer(1, 15))
    story.append(p("Why this course", "H1Custom"))
    story.append(
        p(
            "Haaga-Helia Online already has a strong hospitality and service-business portfolio: hospitality innovation, strategic revenue management, strategic pricing, distribution, guest experience, business intelligence, F&amp;B management, law and leadership. The opportunity is to connect these business areas through practical AI agent workflows."
        )
    )
    story.append(
        bullets(
            [
                "Teach agentic AI as a hospitality operating capability, not as a generic tool topic.",
                "Frame every module around real venue workflows: guest, commercial, revenue, operations and back office.",
                "Give participants reusable agent blueprints and a pilot plan for their own property or service business.",
            ]
        )
    )
    story.append(Spacer(1, 8))
    story.append(
        callout(
            "Core promise: managers learn how to design controlled agents that support key hospitality functions while keeping human judgment, brand standards and data protection in control.",
            color=colors.HexColor("#FFFBEB"),
            border=colors.HexColor("#FCD34D"),
        )
    )
    story.append(Spacer(1, 14))
    story.append(p("Market scan", "H1Custom"))
    market = [
        [p("Current market theme", "TableHead"), p("How our course goes deeper", "TableHead")],
        [p("AI in hotel management and guest service", "TableText"), p("Agent workflows for guest messaging, feedback triage, escalation and service recovery", "TableText")],
        [p("Front office, reservations and guest communication", "TableText"), p("Context-aware agents connected to policies, services, availability rules and staff approval", "TableText")],
        [p("Revenue, pricing and distribution", "TableText"), p("Revenue decision-support agents: booking pace, demand signals, event calendars, channel mix and margin notes", "TableText")],
        [p("Sales, marketing and personalization", "TableText"), p("Commercial agents for segment discovery, campaign planning, offers, group sales and loyalty workflows", "TableText")],
        [p("Digital transformation and strategy", "TableText"), p("Implementation blueprint: data inventory, governance, ROI, pilot design and scaling path", "TableText")],
    ]
    table = Table(market, colWidths=[70 * mm, 95 * mm], repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                ("GRID", (0, 0), (-1, -1), 0.45, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(table)
    story.append(PageBreak())

    story.append(p("Hospitality Agent Map", "H1Custom"))
    story.append(p("The course is structured around five practical domains where agents can support hospitality work.", "BodyCustom"))
    domains = [
        ("1. Guest Experience Agents", ["multilingual guest messaging", "review and feedback analysis", "complaint triage and service recovery", "pre-arrival and post-stay communication"]),
        ("2. Commercial Agents", ["segment discovery from booking and CRM data", "campaign and offer planning", "corporate and group sales support", "competitor and market signal monitoring"]),
        ("3. Revenue and Distribution Agents", ["demand signal monitoring", "pricing memo preparation", "channel mix and margin analysis", "occupancy, ADR, RevPAR and TRevPAR support"]),
        ("4. Operations and F&amp;B Agents", ["shift handover summaries", "SOP assistant for staff", "procurement and supplier communication", "menu engineering and food-waste notes"]),
        ("5. Back-Office and Governance Agents", ["invoice and document processing", "contract and policy search", "management reporting", "audit trail, permissions and approval workflows"]),
    ]
    rows = []
    for i in range(0, len(domains), 2):
        left = card(domains[i][0], domains[i][1])
        right = card(domains[i + 1][0], domains[i + 1][1]) if i + 1 < len(domains) else ""
        rows.append([left, right])
    grid = Table(rows, colWidths=[82 * mm, 82 * mm], hAlign="LEFT")
    grid.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story.append(grid)
    story.append(Spacer(1, 10))
    story.append(p("Recommended product", "H1Custom"))
    story.append(
        bullets(
            [
                "27-hour online course aligned with Haaga-Helia's compact intermediate course format.",
                "Self-study videos, templates, quizzes and practical assignments.",
                "Final output: hospitality agent opportunity map, one detailed agent blueprint, governance and ROI plan.",
            ]
        )
    )
    story.append(PageBreak())

    story.append(p("Course Route", "H1Custom"))
    modules = [
        [p("Module", "TableHead"), p("Focus", "TableHead"), p("Participant deliverable", "TableHead")],
        [p("1. Agentic AI as the next level of AI", "TableText"), p("Models, context, tools, memory, workflows, approvals; hospitality value chain as agent design map", "TableText"), p("Hospitality agent opportunity map", "TableText")],
        [p("2. Hospitality data, context and knowledge", "TableText"), p("PMS, POS, CRM, reviews, booking engines, menus, SOPs, emails, invoices; access and privacy boundaries", "TableText"), p("Data and context inventory", "TableText")],
        [p("3. Guest Experience Agents", "TableText"), p("Guest journey, multilingual communication, feedback classification, service recovery, escalation rules", "TableText"), p("Guest experience agent blueprint", "TableText")],
        [p("4. Commercial Agents", "TableText"), p("Marketing, sales, segmentation, campaign planning, group sales, review mining for positioning", "TableText"), p("Segment-to-campaign workflow", "TableText")],
        [p("5. Revenue and Distribution Agents", "TableText"), p("Demand signals, booking pace, event calendars, pricing memos, channel mix and revenue manager approval flow", "TableText"), p("Revenue decision-support workflow", "TableText")],
        [p("6. Operations, F&amp;B and Back Office Agents", "TableText"), p("Shift handovers, SOP support, procurement, inventory, menu engineering, invoice extraction and reporting", "TableText"), p("Operations or back-office agent blueprint", "TableText")],
        [p("7. Governance, ROI and implementation roadmap", "TableText"), p("Human approval gates, risk categories, value measurement, pilot design and scaling path", "TableText"), p("Final AI agent pilot plan", "TableText")],
    ]
    route = Table(modules, colWidths=[44 * mm, 82 * mm, 39 * mm], repeatRows=1)
    route.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                ("GRID", (0, 0), (-1, -1), 0.42, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(route)
    story.append(Spacer(1, 13))
    story.append(p("Demo lesson", "H1Custom"))
    story.append(callout("From Guest Signals to Service Recovery Actions"))
    story.append(Spacer(1, 7))
    story.append(
        bullets(
            [
                "Import guest reviews, emails and internal notes.",
                "Classify issues by topic, severity and business impact.",
                "Draft response options in brand tone and escalate high-risk cases.",
                "Create weekly insights for operations, marketing and revenue.",
                "Review actions and update SOPs.",
            ]
        )
    )
    story.append(PageBreak())

    story.append(p("What to reuse from Nikolay's Agentic AI course", "H1Custom"))
    reuse = [
        [p("Use from Nikolay's course", "TableHead"), p("Hospitality adaptation", "TableHead")],
        [p("Agents, tools, memory and dynamic context", "TableText"), p("Agent blueprints for guest, commercial, revenue, operations and back-office workflows", "TableText")],
        [p("Workflow automation and integrations", "TableText"), p("Practical venue processes: handovers, approvals, supplier messages, service recovery", "TableText")],
        [p("AI business process automation", "TableText"), p("Manager-facing pilot design with measurable time, quality and revenue outcomes", "TableText")],
        [p("Voice and speech agents", "TableText"), p("Reservation calls, guest requests, internal reporting and staff support scenarios", "TableText")],
        [p("Multimodal AI for documents, menus, images and OCR", "TableText"), p("Invoices, menus, policies, reviews, forms and operational records", "TableText")],
        [p("Governance and human-in-the-loop", "TableText"), p("Brand standards, escalation rules, permissions, audit trail and ROI tracking", "TableText")],
    ]
    reuse_table = Table(reuse, colWidths=[83 * mm, 82 * mm], repeatRows=1)
    reuse_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                ("GRID", (0, 0), (-1, -1), 0.45, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(reuse_table)
    story.append(Spacer(1, 14))
    story.append(p("Why Nikolay Sekachev", "H1Custom"))
    story.append(
        bullets(
            [
                "Lecturer of AI for Business Leaders in the eMBA programme at Stockholm School of Economics in Riga.",
                "25 years in business and investments; MBA in finance; background in astrophysics and law.",
                "Corporate AI education work in Estonia and Latvia.",
                "Creator of practical programmes on LLMs, agents, workflow automation, voice, multimodal AI and business transformation.",
                "Focus: moving learners from AI usage to AI solution design.",
            ]
        )
    )
    story.append(Spacer(1, 12))
    story.append(p("Contact", "H1Custom"))
    contact = Table(
        [
            [p("Lecturer", "TableHead"), p("Nikolay Sekachev", "TableText")],
            [p("Website", "TableHead"), p("sekachev.ee", "TableText")],
            [p("Email", "TableHead"), p("sekachev@gmail.com", "TableText")],
            [p("Telegram", "TableHead"), p("@sekachev", "TableText")],
        ],
        colWidths=[38 * mm, 127 * mm],
    )
    contact.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), ACCENT),
                ("GRID", (0, 0), (-1, -1), 0.45, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 7),
                ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(contact)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)


if __name__ == "__main__":
    build()
