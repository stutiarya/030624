# Specify the file names
source_file_name = "source.txt"
destination_file_name = "destination.txt"

# Read the contents of the source file
with open(source_file_name, "r") as source_file:
    content = source_file.read()

# Write the contents to the destination file
with open(destination_file_name, "w") as destination_file:
    destination_file.write(content)

print(f"Contents of '{source_file_name}' copied to '{destination_file_name}'.")
