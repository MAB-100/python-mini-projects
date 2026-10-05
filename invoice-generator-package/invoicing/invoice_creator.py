import glob
import os
from pathlib import Path

import pandas as pd
from fpdf import FPDF


def generate(invoices_path, pdfs_path, product_id, product_name, amount_purchased,
             price_per_unit, total_price, company_name="Your Company", image_path=None):
    """
    Generate PDF invoices from Excel files.

    Parameters:
    invoices_path (str): Folder containing the Excel invoices, named like "10001-2023.1.18.xlsx".
    pdfs_path (str): Folder where the PDF invoices will be saved.
    product_id (str): Name of the column containing the product ID.
    product_name (str): Name of the column containing the product name.
    amount_purchased (str): Name of the column containing the amount purchased.
    price_per_unit (str): Name of the column containing the price per unit.
    total_price (str): Name of the column containing the total price.
    company_name (str): Company name printed at the bottom of each invoice.
    image_path (str, optional): Path to a company logo image.
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")
    os.makedirs(pdfs_path, exist_ok=True)

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
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=str(row[product_name]), border=1)
            pdf.cell(w=40, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)

        # Total row
        total = df[total_price].sum()
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=40, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total), border=1, ln=1)

        # Total sentence, company name and optional logo
        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=30, h=8, txt=f"The total price is {total}", ln=1)
        pdf.cell(w=30, h=8, txt=company_name)
        if image_path:
            pdf.image(image_path, w=10)

        pdf.output(f"{pdfs_path}/{filename}.pdf")
