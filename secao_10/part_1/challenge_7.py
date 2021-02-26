'''
Challenge #7

Write a Python program that accepts as input a sequence of words separated
by one or more whitespaces and prints out the same words with the letters
in reversed order. Do not use list comprehension.

Sample input string: I love cat and dogs
Expected Result : I evol tac dna sgod

Create an alternative solution for the previous challenge that uses list comprehension.
'''

words = 'I love cat and dogs'
words_list = words.split(' ')
result = [w[::-1] for w in words_list]

print(' '.join(result))
