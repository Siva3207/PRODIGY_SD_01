def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    print("Choose the original temperature unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    
    choice = int(input("Enter your choice (1/2/3): "))
    temp = float(input("Enter the temperature value: "))
    
    if choice == 1:
        # Celsius to Fahrenheit and Kelvin
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"{temp}°C is equal to {fahrenheit}°F and {kelvin}K")
    elif choice == 2:
        # Fahrenheit to Celsius and Kelvin
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F is equal to {celsius}°C and {kelvin}K")
    elif choice == 3:
        # Kelvin to Celsius and Fahrenheit
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"{temp}K is equal to {celsius}°C and {fahrenheit}°F")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

convert_temperature()