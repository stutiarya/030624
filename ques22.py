# Take input from the user
numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers_list = [float(num) for num in numbers.split()]

# Find the minimum and maximum values in the list
minimum_value = min(numbers_list)
maximum_value = max(numbers_list)

# Print the minimum and maximum values
print(f"Minimum value: {minimum_value}")
print(f"Maximum value: {maximum_value}")
