# Take input from the user
number = int(input("Enter a number: "))

# Initialize sum to 0
sum_of_digits = 0

# Calculate the sum of digits
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number // 10

# Print the sum of digits
print("Sum of digits:", sum_of_digits)