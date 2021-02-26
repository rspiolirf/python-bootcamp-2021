'''
Challenge #5

Write a Python program that accepts a hyphen-separated sequence of words as input
and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample input string : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
'''

words = input('Entre com uma sequencia de palavras separadas por "-": ')
words_list = words.split('-')
words_list.sort()
words = '-'.join(words_list)
print(words)