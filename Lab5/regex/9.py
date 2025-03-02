# Write a Python program to insert spaces between words starting with capital letters. 
import re

def insert_spaces(string):
    pattern = r'([A-Z])'
    return re.sub(pattern, r' \1', string).strip()

print(insert_spaces("HelloWorld"))
