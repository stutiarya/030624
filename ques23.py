# Take input from the user
temperature = input("Enter the temperature value: ")
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit): ")

# Convert the temperature based on the unit
if unit.upper() == 'C':
    celsius = float(temperature)
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}°F")
elif unit.upper() == 'F':
    fahrenheit = float(temperature)
    celsius = (fahrenheit - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}°C")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
