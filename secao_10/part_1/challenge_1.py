'''
Challenge #1

Create a Python script that asks the user for a number and then prints out
a list of all the divisors of each number less than the asked number.
'''

number = int(input('Entre com um número: '))

for i in range(1, number + 1):
    if number % i == 0:
        print(i)