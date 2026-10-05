import glob
import os
from pathlib import Path

import pandas as pd
from fpdf import FPDF

COMPANY_NAME = "Acme Corp"

filepaths = glob.glob("invoices/*.xlsx")
os.makedirs("PDFs", exist_ok=True)

for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, invoice_date = filename.split("-")

    pdf.set_font("Times", "B", 16)
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.cell(w=50, h=8, txt=f"Date {invoice_date}", ln=1)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Header
    columns = [item.replace("_", " ").title() for item in df.columns]
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Rows
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=12)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=40, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)

    # Total row
    total = df["total_price"].sum()
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=40, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

    # Total sentence and company name
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total}", ln=1)
    pdf.cell(w=30, h=8, txt=COMPANY_NAME)

    pdf.output(f"PDFs/{filename}.pdf")
