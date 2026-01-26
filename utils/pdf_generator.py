from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(plan_data, image_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "SmartBuild Planner - Floor Plan")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Total Area: {plan_data['area']} sq.ft")
    c.drawString(50, 750, f"Estimated Cost: ₹{plan_data['cost']}")

    # Draw plan image
    c.drawImage(image_path, 50, 400, width=500, height=300)

    c.save()
