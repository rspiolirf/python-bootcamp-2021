'''
Challenge #3

Write a Python script that finds all numbers that are divisible by 7
but are not a multiple of 5, between 1500 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.
'''

numbers = list()
for number in range(1500, 3200 + 1):
    if number % 7 == 0 and number % 5 != 0:
        numbers.append(number)

str_numbers = [str(n) for n in numbers]
print(', '.join(str_numbers))