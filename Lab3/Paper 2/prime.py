
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

number = int(input())

is_it = bool(is_prime(number))

if is_it:
    print(f"The number {number }is brime!")
else:
    print(f"The number {number} is NOT prime!")