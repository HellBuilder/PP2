# Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re

def find_upper_lower(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

print(find_upper_lower("Hello World"))
