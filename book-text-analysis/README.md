# Book Text Analysis

A Jupyter notebook that explores the text of a book:

- counts chapters with regular expressions
- finds every sentence containing a given word
- ranks the most frequent words, with and without NLTK stop words
- scores the sentiment of each chapter with NLTK's VADER analyzer

## Run

The book text is not included. Save any plain-text book as `book.txt` in this folder. [Project Gutenberg](https://www.gutenberg.org) has many free ones; the notebook expects chapter headings like `Chapter 1`.

```bash
pip install -r requirements.txt
jupyter notebook book_analysis.ipynb
```
