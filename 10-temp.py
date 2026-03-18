import celsius_to_fahrenheit
import fahrenheit_to_celsius
import celsius_to_kelvin

while True:

    print("\nChoose the Conversion: ")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '4':
        print("Exiting the program. Goodbye!")
        break

    try:
        temp = float(input("Enter temperature: "))

        if choice == '1':
            conv_temp = celsius_to_fahrenheit.convert_celsius_to_fahrenheit(temp)
            print(f"{temp} Celsius is equal to {conv_temp:.2f} Fahrenheit")

        elif choice == '2':
            conv_temp = fahrenheit_to_celsius.convert_fahrenheit_to_celsius(temp)
            print(f"{temp} Fahrenheit is equal to {conv_temp:.2f} Celsius")

        elif choice == '3':
            conv_temp = celsius_to_kelvin.convert_celsius_to_kelvin(temp)
            print(f"{temp} Celsius is equal to {conv_temp:.2f} Kelvin")

        else:
            print("Invalid choice. Please select a valid option.")
            
    except ValueError as e:
        print(f"Error: {e}")
