# make_euler_problem.py

import sys
import json
from pathlib import Path

def create_python_file(problem_number: int):
    problem_str = f"{problem_number:03}"
    filename = f"problems/problem{problem_str}.py"
    if Path(filename).exists():
        print(f"⚠️ {filename} already exists.")
        return

    content = f'''"""Solution to Project Euler Problem {problem_number}."""


def solve() -> int:
    raise NotImplementedError("Problem {problem_number} solution not implemented yet")


if __name__ == "__main__":
    print(solve())
'''
    Path(filename).write_text(content)
    print(f"✅ Created Python file: {filename}")

def create_notebook(problem_number: int):
    problem_str = f"{problem_number:03}"
    filename = f"notebooks/Problem{problem_str}.ipynb"
    if Path(filename).exists():
        print(f"⚠️ {filename} already exists.")
        return

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# Project Euler Problem {problem_number}"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "id": "setup",
                "metadata": {
                    "vscode": {"languageId": "shellscript"}
                },
                "outputs": [],
                "source": [
                    "import sys\n",
                    "sys.path.append(\"..\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["This notebook demonstrates a simple solution in Python."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    f"from problems.problem{problem_str} import solve\n",
                    "from datetime import datetime"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "start = datetime.now()\n",
                    "result = solve()\n",
                    "end = datetime.now()\n",
                    "print(f\"Result: {result}\")\n",
                    "print(f\"Execution time: {end - start}\")"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "venv",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.13.2",
                "mimetype": "text/x-python",
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    Path(filename).write_text(json.dumps(notebook, indent=2))
    print(f"✅ Created notebook: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python make_euler_problem.py <problem_number>")
    else:
        num = int(sys.argv[1])
        create_python_file(num)
        create_notebook(num)
