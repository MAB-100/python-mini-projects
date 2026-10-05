# Excel to PDF Invoices

Turns every Excel file in `invoices/` into a formatted PDF invoice in `PDFs/`. The invoice number and date are parsed from the file name (`10001-2023.1.18.xlsx`), and each invoice gets an item table and a calculated total.

## Run

```bash
pip install -r requirements.txt
python main.py
```

The same logic is packaged as a reusable library in [invoice-generator-package](../invoice-generator-package).
