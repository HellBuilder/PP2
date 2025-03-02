# Write a Python program to split a string at uppercase letters.
import re

def split_at_uppercase(string):
    pattern = r'[A-Z][a-z]*'
    return re.findall(pattern, string)

print(split_at_uppercase("HelloWorld"))
