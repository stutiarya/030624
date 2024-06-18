# Take input from the user
number = int(input("Enter a number: "))

# Initialize the result to 1 (as the factorial of 0 is 1)
factorial = 1

# Calculate the factorial using a loop
if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")