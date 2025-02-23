# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_other_scales(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_other_scales(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_other_scales(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

# Function to handle the temperature conversion process
def temperature_conversion():
    # Taking input from the user
    temp_value = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    if original_unit == 'celsius':
        fahrenheit, kelvin = celsius_to_other_scales(temp_value)
        print(f"{temp_value}°C is equal to {fahrenheit}°F and {kelvin}K.")
    elif original_unit == 'fahrenheit':
        celsius, kelvin = fahrenheit_to_other_scales(temp_value)
        print(f"{temp_value}°F is equal to {celsius}°C and {kelvin}K.")
    elif original_unit == 'kelvin':
        celsius, fahrenheit = kelvin_to_other_scales(temp_value)
        print(f"{temp_value}K is equal to {celsius}°C and {fahrenheit}°F.")
    else:
        print("Invalid unit entered. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")

# Running the program
temperature_conversion()
