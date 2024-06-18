# Take input from the user
text = input("Enter a string: ")

# Specify the file name
file_name = "user_input.txt"

# Write the input to a text file
with open(file_name, "w") as file:
    file.write(text)

print(f"String '{text}' has been written to '{file_name}'.")