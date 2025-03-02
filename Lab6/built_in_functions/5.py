# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(elements):
    return all(elements)

f = (True, True, False)
t = (True, True, True)
print(all_true(f))
print(all_true(t))
