def length_converter():
    meters = float(input("Enter length in meters: "))
    print("Centimeters:", meters * 100)
    print("Kilometers:", meters / 1000)
    print("Feet:", meters * 3.28084)
    print("Inches:", meters * 39.3701)

def weight_converter():
    kg = float(input("Enter weight in kilograms: "))
    print("Grams:", kg * 1000)
    print("Pounds:", kg * 2.20462)
    print("Ounces:", kg * 35.274)

def temperature_converter():
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit:", c * 9/5 + 32)
    print("Kelvin:", c + 273.15)

while True:
    print("\nUnit Converter Menu:")
    print("1. Length (meters to others)")
    print("2. Weight (kg to others)")
    print("3. Temperature (Celsius to others)")
    print("4. Quit")

    choice = input("Choose an option (1/2/3/4): ")
    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
