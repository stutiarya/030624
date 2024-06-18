# Take input from the user
string = input("Enter a string: ")

# Initialize a dictionary to store the frequency of each character
frequency = {}

# Count the frequency of each character
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Print the frequency of each character
print("Character frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
