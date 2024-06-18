# Take input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize the first two numbers in the sequence
fibonacci_sequence = [0, 1]

# Generate the Fibonacci sequence
for i in range(2, n):
    next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_number)

# Print the Fibonacci sequence
print("Fibonacci sequence:", fibonacci_sequence)
