# Python Code Reviewer - SWE488 Project

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-in%20development-yellow)

An automated code review tool that helps Python developers write better, safer, and cleaner code. Think of it as a **spell checker + security guard + complexity meter** all in one!

---

## **Table of Contents**
- [What is this?](#what-is-this)
- [Features](#features)
- [Why This Project?](#why-this-project)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Team](#team)
- [Course Connection](#course-connection)

---

## **What is this?**

This tool automatically examines Python code and tells you:

| Problem Type | What We Check | Example |
|-------------|---------------|---------|
| **Style Issues** | PEP 8 rules (spacing, naming, formatting) | `def badFunction():` → should be `def bad_function():` |
| **Security Risks** | Passwords, dangerous functions, injections | `password = "12345"` → Alert! |
| **Complexity** | Functions too hard to understand/fix | A function with 15 nested ifs → Too complex! |
| **Duplicates** | Copy-pasted code blocks | Same code in 3 places → Don't repeat yourself! |

Then it creates a **professional report** (PDF) with all the problems and suggestions to fix them.

---

## **Features**

**Style Checker** - Enforces Python's "neat handwriting" rules (PEP 8)  
**Security Scanner** - Finds vulnerabilities before hackers do  
**Complexity Meter** - Flags functions that are too complicated  
**Duplicate Detector** - Finds copy-pasted code  
**PDF Reports** - Beautiful, printable analysis results  
**GitHub Integration** - Automatically checks code on pull requests  
**Web Dashboard** - View all past reviews in one place  

---

## **Why This Project?**

This is my **SWE488 (Software Implementations)** course project. It demonstrates:

- **Clean Code Practices** - The tool itself follows what it preaches
- **Software Testing** - Unit tests, integration tests, load tests
- **Security Awareness** - Built-in security scanning
- **DevOps Practices** - GitHub Actions, CI/CD
- **Documentation** - Clear guides for users and developers
- **Team Collaboration** - Built using Git/GitHub workflows

---

## **Technologies Used**

| Category | Tools | Why |
|----------|-------|-----|
| **Language** | Python 3.8+ | Everyone knows it! |
| **Web Framework** | Flask | Lightweight, perfect for small dashboard |
| **Code Analysis** | flake8, radon, bandit | Industry standards for Python |
| **Testing** | pytest, coverage, Selenium | Unit + UI testing |
| **API Testing** | Postman | Easy endpoint validation |
| **Performance** | locust | Simulates 1000s of users |
| **Reports** | Jinja2, WeasyPrint | HTML → PDF conversion |
| **Database** | SQLite | Simple, no setup needed |
| **Version Control** | Git/GitHub | Collaboration & CI/CD |

---

## **Installation**

### Prerequisites
- Python 3.8 or higher
- Git
- (Optional) Docker

### Steps

```bash
# 1. Clone this repository
git clone https://github.com/lifeISJokeORNot/swe488-python-code-reviewer.git
cd swe488-python-code-reviewer

# 2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a test
pytest tests/
