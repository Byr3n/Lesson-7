user_input = input("Enter a character:")

if user_input.isascii():
    print("The input is a valid ASCII string.")
else:
    print("The input is not a ASCII string")