from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=24)

pdf.cell(text="Sample PDF document")
pdf.ln(10)
pdf.set_font("Arial", "B", size=18)
pdf.cell(text="Python basics course")

pdf.output("sample.pdf")