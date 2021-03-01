'''
Challenge #10

Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].

Create a Set that contains the elements of the 2 lists in pairs.

The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}
'''

names = ["Dan", "John", "Diana"]
phones = [11111, 2222, 3333]
result = tuple(zip(names, phones))
print(result)