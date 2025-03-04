
def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome("madam"))
print(is_palindrome("12321"))
print(is_palindrome("RaoR"))
