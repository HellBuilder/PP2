# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

def replace_with_colon(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ":", string)

print(replace_with_colon("Hello, world. Hello"))
