# Specify the file name
file_name = "user_input.txt"

# Read the content of the text file
with open(file_name, "r") as file:
    content = file.read()

# Print the content to the console
print("Content of the file:")
print(content)