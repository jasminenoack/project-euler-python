# Project Euler Python

This repository contains Python solutions to [Project Euler](https://projecteuler.net/) problems along with example Jupyter notebooks.

## Getting Started

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Launch Jupyter Lab:

```bash
jupyter lab
```

Then open the notebooks found in the `notebooks/` directory.

## Problem Structure

Problem solutions live inside the `problems` package. Each file exposes a `solve()` function that returns the answer.

Example usage:

```python
from problems.problem001 import solve
# Implement the solution yourself then call:
print(solve())
```

Add new problem solutions and notebooks as you progress.
