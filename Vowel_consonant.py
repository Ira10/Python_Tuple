# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    # s = input("Enter the string as you please  : ")
    vowel = 0 
    consonant = 0
    for i in s.lower():  # Make it case-insensitive
        if i in "aeiou":
            vowel += 1
        else:
            consonant +=1
    return (vowel,consonant)


# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)
# print(char_counts(s))
print(char_counts("Indrani Sarkar"))  # (5, 9) # counting space too

### possible that people might insert some numbers as well.


# Write a function that meets these specifications:
def char_counts(s):
    """ s is a string of lowercase chars 
    Returns a tuple where the first value is the 
    number of vowels in s and the second value 
    is the number of consonants in s 
    """
    # your code here
    # s = input("Enter the string as you please  : ")
    vowel = 0 
    consonant = 0
    for i in s.lower():  # Make it case-insensitive
        if i in "aeiou":
            vowel += 1
        elif i.isalpha():
            consonant +=1
    return (vowel,consonant)


# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)
# print(char_counts(s))
print(char_counts("Indrani Sarkar 1522")) #(5, 8) ## removing space as well
