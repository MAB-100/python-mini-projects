# Todo App

One todo list with three interchangeable front ends. All three read and write the same `todos.txt`.

- `cli.py`: command-line app (`add`, `show`, `complete`, `exit`)
- `gui.py`: desktop app built with FreeSimpleGUI, with a live clock and add, edit and complete buttons
- `webapp.py`: Streamlit web app where ticking a checkbox completes a todo

## Run

```bash
pip install -r requirements.txt
python cli.py            # command line
python gui.py            # desktop GUI
streamlit run webapp.py  # web app
```
