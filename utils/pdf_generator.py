from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(plan_data, image_path, pdf_path):
    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph("<b>SMARTBUILD PLANNER</b>", styles["Title"]))
    elements.append(Paragraph(f"Total Area: {plan_data['area']} sq.ft", styles["Normal"]))
    elements.append(Paragraph(f"Estimated Cost: ₹{plan_data['cost']}", styles["Normal"]))
    elements.append(Image(image_path, width=400, height=300))

    doc.build(elements)
