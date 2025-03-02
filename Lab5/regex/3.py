# Write a Python program to find sequences of lowercase letters joined with a underscore.
import re

def find_lower_underscore(string):
    pattern = r'\b[a-z]+_[a-z]+\b'
    return re.findall(pattern, string)

print(find_lower_underscore("hello_world test_string"))
