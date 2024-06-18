# Take input from the user
numbers = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of numbers
numbers_list = [float(num) for num in numbers.split()]

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers_list)

# Print the sum of the numbers
print("Sum of the numbers:", sum_of_numbers)
