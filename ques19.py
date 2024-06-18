import string

# Take input from the user
string_with_punctuation = input("Enter a string with punctuation: ")

# Remove punctuation from the string
string_without_punctuation = string_with_punctuation.translate(str.maketrans('', '', string.punctuation))

# Print the string without punctuation
print("String without punctuation:", string_without_punctuation)
