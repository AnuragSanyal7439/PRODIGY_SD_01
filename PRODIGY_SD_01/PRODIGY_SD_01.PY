def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature():
    print("Temperature Converter: Celsius, Fahrenheit, Kelvin")
    print("Select the input unit of temperature:")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    
    choice = int(input("Enter your choice (1/2/3): "))
    temp = float(input("Enter the temperature value: "))
    
    if choice == 1:  
        fahrenheit = celsius_to_fahrenheit(temp)
        kelvin = celsius_to_kelvin(temp)
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
        print(f"Temperature in Kelvin: {kelvin:.2f}K")
        
    elif choice == 2: 
        celsius = fahrenheit_to_celsius(temp)
        kelvin = fahrenheit_to_kelvin(temp)
        print(f"Temperature in Celsius: {celsius:.2f}°C")
        print(f"Temperature in Kelvin: {kelvin:.2f}K")
        
    elif choice == 3: 
        celsius = kelvin_to_celsius(temp)
        fahrenheit = kelvin_to_fahrenheit(temp)
        print(f"Temperature in Celsius: {celsius:.2f}°C")
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")
        
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

# Call the function
convert_temperature()
