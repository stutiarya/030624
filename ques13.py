# Take input from the user
birth_year = int(input("Enter your birth year: "))

# Get the current year
import datetime
current_year = datetime.datetime.now().year

# Calculate the age
age = current_year - birth_year

# Print the age
print("Your age is:", age)
