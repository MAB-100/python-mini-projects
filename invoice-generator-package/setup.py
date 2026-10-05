from setuptools import setup

setup(
    name="free_invoice_generator",
    packages=["invoicing"],
    version="1.1.0",
    license="MIT",
    description="Convert Excel invoices to PDF invoices.",
    author="Abbas Bukhari",
    url="https://github.com/MAB-100/python-mini-projects/tree/main/invoice-generator-package",
    keywords=["invoice", "excel", "pdf"],
    install_requires=["pandas", "fpdf", "openpyxl"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
