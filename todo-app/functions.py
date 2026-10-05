import os

FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.txt")


def get_todos(filepath=FILEPATH):
    """Read the todo items from the text file."""
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todos(todos, filepath=FILEPATH):
    """Write the todo items to the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos)
