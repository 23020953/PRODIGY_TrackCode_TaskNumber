# Temperature Conversion Program

def convert_temperature():
    temp_str = input("Enter the temperature value: ").strip()
    try:
        temperature = float(temp_str)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit in ("C", "CELSIUS"):
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
        print(f"{temperature:.2f}°C is {fahrenheit:.2f}°F and {kelvin:.2f} K")

    elif unit in ("F", "FAHRENHEIT"):
        celsius = (temperature - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temperature:.2f}°F is {celsius:.2f}°C and {kelvin:.2f} K")

    elif unit in ("K", "KELVIN"):
        celsius = temperature - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temperature:.2f} K is {celsius:.2f}°C and {fahrenheit:.2f}°F")

    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    convert_temperature()
