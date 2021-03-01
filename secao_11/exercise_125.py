def vowel_count(my_str):
    """
    This function counts the number of vowels in a string and returns a dictionary.
    """
    vowels = 'aeiou'
    result = dict()
    for letter in vowels:
        total = 0
        for letter2 in my_str:
            if letter2.lower() == letter.lower():
                total += 1
        if total > 0:
            result[letter] = total

    return result

print(vowel_count('Python JAVA Go'))