"""
Python Code Checker with Flask and pytest support
"""

def check_code(code_lines):
    """Check code and return list of issues"""
    issues = []
    
    for i, line in enumerate(code_lines, 1):
        line = line.rstrip()
        
        # Check missing spaces around =
        if '=' in line and '==' not in line and '!=' not in line:
            if '= ' not in line and ' =' not in line:
                issues.append(f"Line {i}: Missing spaces around = : {line}")
        
        # Check line length
        if len(line) > 80:
            issues.append(f"Line {i}: Line too long ({len(line)} chars)")
        
        # Check print statements
        if 'print(' in line:
            issues.append(f"Line {i}: Found print statement")
    
    return issues

def check_file(filename):
    """Read file and check it"""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        return check_code(lines)
    except FileNotFoundError:
        return [f"Error: File '{filename}' not found!"]

# For command line use
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        issues = check_file(sys.argv[1])
        for issue in issues:
            print(issue)
        print(f"\nTotal: {len(issues)} issues")
    else:
        print("Usage: python checker.py <filename>")
