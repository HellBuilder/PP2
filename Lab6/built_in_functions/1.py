
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

numbers = [2, 3, 4, 5]
print(multiply_list(numbers))
