# Take input from the user
string = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

# Check if the string starts with the prefix
if string.startswith(prefix):
    print(f"The string '{string}' starts with the prefix '{prefix}'")
else:
    print(f"The string '{string}' does not start with the prefix '{prefix}'")

# Check if the string ends with the suffix
if string.endswith(suffix):
    print(f"The string '{string}' ends with the suffix '{suffix}'")
else:
    print(f"The string '{string}' does not end with the suffix '{suffix}'")
