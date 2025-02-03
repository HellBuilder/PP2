from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

word = str(input())

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(string_permutations(word))

print(reverse_sentence(word))