'''
Challenge #2

Consider the following string: nums = '10,20,30,40,50'
Create a Python script that creates a list of integers from the string.
The resulting list will be: [10, 20, 30, 40, 50]
'''

nums = '10,20,30,40,50'
my_list_str = nums.split(',')

my_list = [int(num) for num in my_list_str]
print(type(my_list))
print(my_list)