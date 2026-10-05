# Invoice Generator Package

The [Excel to PDF invoice](../excel-to-pdf-invoices) script turned into a reusable, pip-installable library, with configurable column names, company name and an optional logo.

## Install

```bash
pip install .
```

## Usage

```python
from invoicing import generate

generate(
    invoices_path="invoices",
    pdfs_path="PDFs",
    product_id="product_id",
    product_name="product_name",
    amount_purchased="amount_purchased",
    price_per_unit="price_per_unit",
    total_price="total_price",
    company_name="Acme Corp",
    image_path="logo.png",   # optional
)
```
