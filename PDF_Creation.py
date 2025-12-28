from fpdf import FPDF

# Initialize the PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title of the PDF
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Kassandra 2026 Master Plan Deck', ln=True, align='C')

# Content Section 1
pdf.set_font('Arial', '', 12)
pdf.ln(10)  # Add a line break
pdf.cell(0, 10, 'This is the official master plan outline for Kassandra 2026.', ln=True)
 
# Finalizing the PDF
pdf.output('Kassandra_2026_MasterPlan_Deck.pdf')

print("PDF file generated: Kassandra_2026_MasterPlan_Deck.pdf")