# Take input from the user
numbers = input("Enter a list of numbers separated by spaces: ")
element_to_count = int(input("Enter the element to count: "))

# Split the input string into a list of numbers
numbers_list = [int(num) for num in numbers.split()]

# Count the occurrences of the element
count = numbers_list.count(element_to_count)

# Print the count
print(f"Count of {element_to_count}: {count}")
