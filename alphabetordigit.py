#alphabetordigit
a = input("Enter a character")
if a.isalpha():
    print("Alphabet")
elif a.isdigit():
    print("Digit")
else:
    print("Special character")