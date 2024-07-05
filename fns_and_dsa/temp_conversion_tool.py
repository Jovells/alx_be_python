CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()