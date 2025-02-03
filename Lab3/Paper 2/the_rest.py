def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums) - 1))

def spy_game(nums):
    sequence = [0, 0, 7]
    for num in nums:
        if num == sequence[0]:
            sequence.pop(0)
        if not sequence:
            return True
    return False

def sphere_volume(radius):
    return (4 / 3) * 3.141592653589793 * radius ** 3

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)
