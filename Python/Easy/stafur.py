a = input().strip() # Read input and remove any surrounding whitespace

vowels = "AEIOU" # Define vowels

if a in vowels:
    print("Jebb") # Prints "Jebb" if the input is a vowel
elif a == "Y":
    print("Kannski") # Prints "Kannski" if the input is 'Y'
else:
    print("Neibb") # Prints "Neibb" if the input is a consonant