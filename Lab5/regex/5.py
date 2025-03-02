# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def match_a_anything_b(string):
    pattern = r'^a.*b$'
    return bool(re.fullmatch(pattern, string))

print(match_a_anything_b("ab"))
print(match_a_anything_b("axb"))   
print(match_a_anything_b("abc"))    
print(match_a_anything_b("a123b"))   
