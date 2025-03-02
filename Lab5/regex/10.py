# Write a Python program to convert a given camel case string to snake case.
import re

def camel_to_snake(string):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1\2', string).lower()

print(camel_to_snake("HelloWorld"))
