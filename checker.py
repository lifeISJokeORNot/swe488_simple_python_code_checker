---

## **File 2: checker.py** (THE MAIN CODE)

```python
"""
SIMPLE Python Code Checker
Checks a Python file for basic issues
"""

import sys

def check_file(filename):
    """Check a Python file for simple issues"""
    
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        return
    
    print("=" * 50)
    print(f"CHECKING FILE: {filename}")
    print("=" * 50)
    
    issues_found = 0
    
    for i, line in enumerate(lines, 1):
        line = line.rstrip()  # Remove trailing newline
        
        # Check 1: Missing spaces around = 
        if '=' in line and '==' not in line and '!=' not in line:
            if '= ' not in line and ' =' not in line:
                print(f"Line {i}: Missing spaces around = : {line}")
                issues_found += 1
        
        # Check 2: Line too long (>80 chars)
        if len(line) > 80:
            print(f"Line {i}: Line too long ({len(line)} chars)")
            issues_found += 1
        
        # Check 3: Print statement (for debugging)
        if 'print(' in line and '#' not in line.split('print')[0]:
            print(f"Line {i}: Found print statement: {line.strip()}")
            issues_found += 1
        
        # Check 4: Function too long
        if line.startswith('def '):
            func_name = line[4:].split('(')[0]
            func_lines = 0
            for j in range(i, len(lines)):
                if lines[j].strip() and not lines[j].startswith(' '):
                    break
                if lines[j].strip() and not lines[j].startswith('def'):
                    func_lines += 1
            if func_lines > 10:
                print(f"Line {i}: Function '{func_name}' is too long ({func_lines} lines)")
                issues_found += 1
    
    print("=" * 50)
    if issues_found == 0:
        print("✅ No issues found! Good code!")
    else:
        print(f"❌ Found {issues_found} potential issues")
    print("=" * 50)

# Run the program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python checker.py <filename.py>")
    else:
        check_file(sys.argv[1])
