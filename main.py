import math
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Available balance is {self.balance}.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance is {self.balance}.")


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)
