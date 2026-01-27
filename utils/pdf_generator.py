from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(plan_data, image_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)

    # Title block
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(300, 820, "SMARTBUILD PLANNER")

    c.setFont("Helvetica", 12)
    c.drawCentredString(300, 795, "Residential Building Floor Plan")

    # Plan details
    c.drawString(40, 760, f"Total Area: {plan_data['area']} sq.ft")
    c.drawString(40, 740, f"Estimated Cost: ₹{plan_data['cost']}")
    c.drawString(40, 720, "Scale: 1 ft = 20 units")

    # Floor plan image
    c.drawImage(image_path, 40, 300, width=520, height=400)

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.drawCentredString(300, 40, "Generated using SmartBuild Planner")

    c.save()
