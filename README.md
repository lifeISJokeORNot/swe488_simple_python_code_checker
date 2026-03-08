# Simple Python Code Checker - SWE488

A basic tool that checks Python files for common problems.

## What it does:
- Finds missing spaces (like `x=1` instead of `x = 1`)
- Finds very long lines (>80 characters)
- Finds functions that are too long (>10 lines)
- Finds `print()` statements (reminder to remove them)

## How to run:
```bash
python checker.py sample.py
