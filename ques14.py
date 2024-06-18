# Initialize an empty list to store the lines of input
lines = []

# Read input from the user
print("Enter multiple lines of text. Enter an empty line to stop.")

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

# Print the lines of input
print("\nLines entered:")
for line in lines:
    print(line)
