# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

text = "Hello World!"
upper, lower = count_case(text)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")
