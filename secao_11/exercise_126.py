# It returns the number of vowels and consonants in the string as a tuple.
def counter(my_str):
    vowels = 'aeiou'
    
    ## YOUR CODE STARTS HERE
    total_vowels = 0
    total_consoants = 0
    for char in my_str.lower():
        if char in vowels:
            total_vowels += 1
        else:
            total_consoants += 1

    return (total_vowels, total_consoants)

print(counter('Python'))
print(counter('Beautiful'))