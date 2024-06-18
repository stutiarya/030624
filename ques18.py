# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove spaces and convert both strings to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if the two strings are anagrams
if sorted(string1) == sorted(string2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
