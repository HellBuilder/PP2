# Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def match_a_bbb(string):
    pattern = r'^ab{2,3}$'
    return bool(re.fullmatch(pattern, string))

print(match_a_bbb("abb"))    
print(match_a_bbb("abbb"))   
print(match_a_bbb("abbbb"))   
print(match_a_bbb("a"))       