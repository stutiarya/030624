# Take input from the user
string = input("Enter a string: ")
substring = input("Enter a substring to search for: ")

# Check if the substring is present in the string
if substring in string:
    print(f"The substring '{substring}' is present in the string.")
else:
    print(f"The substring '{substring}' is not present in the string.")
