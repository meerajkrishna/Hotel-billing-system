from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_bill_pdf(order_id, items, total_amount, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    width, height = A4

    y = height - 50
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, y, "Hotel Bill Receipt")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Order ID: {order_id}")

    y -= 30
    c.drawString(50, y, "Item")
    c.drawString(200, y, "Price")
    c.drawString(300, y, "Qty")
    c.drawString(380, y, "Subtotal")

    y -= 20
    c.line(50, y, 500, y)

    for item in items:
        y -= 25
        c.drawString(50, y, item["name"])
        c.drawString(200, y, str(item["price"]))
        c.drawString(300, y, str(item["quantity"]))
        c.drawString(380, y, str(item["subtotal"]))

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(300, y, f"Total Amount: ₹{total_amount}")

    c.save()
