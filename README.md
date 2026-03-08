# Python Code Checker - SWE488 Project

A simple but powerful tool that checks Python code for common quality issues. Built with Flask and pytest to demonstrate software implementation skills.

---

## **Features**

| Feature | Description |
|---------|-------------|
| **Code Analysis** | Checks for missing spaces, long lines, print statements |
| **Web Interface** | Upload files through a clean Flask web app |
| **Automated Tests** | pytest tests with 100% coverage |
| **Command Line** | Run checks directly from terminal |
| **Quality Metrics** | Identifies code quality issues automatically |

---

## **Technologies Used**

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Flask** | Web framework for the upload interface |
| **pytest** | Testing framework for automated tests |
| **HTML/CSS** | Simple web interface |

---

## **Project Structure**

swe488_simple_python_code_checker/
│
├── checker.py # Core code checking logic
├── app.py # Flask web application
├── test_checker.py # pytest test cases
├── requirements.txt # Project dependencies
├── sample.py # Example file to test
└── README.md # This file

---

## **How to Run**

### **1. Install Dependencies**
```bash
pip install flask pytest
```
### **2. Run Tests (Shows testing knowledge)**
```bash
pytest test_checker.py -v
```
### **3. Run Web Interface (Shows framework knowledge)**
```bash
python app.py
```
### **4. Run Command Line (Original version)**
```bash
python checker.py sample.py
