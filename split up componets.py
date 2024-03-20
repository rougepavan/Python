import re

def is_valid_number(s):
    
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    
    
    return bool(re.match(pattern, s.strip()))

# Test cases
valid_numbers = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
invalid_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for num in valid_numbers:
    print(f"{num}: {is_valid_number(num)}")  # Expected: True

for num in invalid_numbers:
    print(f"{num}: {is_valid_number(num)}")  # Expected: False
