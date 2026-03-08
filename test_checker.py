"""
Tests for the code checker
"""

import checker

def test_check_code_finds_missing_spaces():
    code = ["x=5"]  # Bad: missing spaces
    issues = checker.check_code(code)
    assert len(issues) > 0
    assert "Missing spaces" in issues[0]

def test_check_code_passes_good_code():
    code = ["x = 5"]  # Good: with spaces
    issues = checker.check_code(code)
    assert len(issues) == 0

def test_check_code_finds_long_lines():
    long_line = ["x" * 100]  # 100 chars
    issues = checker.check_code(long_line)
    assert len(issues) > 0
    assert "Line too long" in issues[0]
