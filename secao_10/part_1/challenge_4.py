'''
Challenge #4

Write a program that asks the user for a long string containing
multiple words separated by whitespaces.
Make it to print back the same string with the words in backward order.
For example, say I type the string: My name is Andrei
Then the script should print out: Andrei is name My
'''

long_string = input('Entre com uma frase: ')
long_string_list = long_string.split(' ')
long_string_list.reverse()

print(' '.join(long_string_list))