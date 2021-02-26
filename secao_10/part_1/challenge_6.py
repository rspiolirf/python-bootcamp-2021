'''
Challenge #6

Write a Python program that accepts as input a sequence of words separated
by one or more whitespaces and prints out the same words with the letters
in reversed order. Do not use list comprehension.

Sample input string: I love cat and dogs
Expected Result : I evol tac dna sgod
'''

# words = input('Entre com uma sequencia de palavras: ')
words = 'I love cat and dogs'
words_list = words.split(' ')

result = list()
for w in words_list:
    w_list = list(w)
    w_list.reverse()
    result.append(''.join(w_list))

print(' '.join(result))