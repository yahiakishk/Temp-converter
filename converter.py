temp = float(input("Enter the temperature: "))
unit = input("Enter the current unit (c, f, k): ").lower()
conversion_unit = input("Enter the conversion unit (c, f, k): ").lower()

if unit == "c":
    if conversion_unit == "f":
        print(f"Temp is {round((temp * 1.8) + 32, 1)} degrees Fahrenheit.")

    elif conversion_unit == "k":
        print(f"Temp is {round(temp + 273.15, 1)} degrees Kelvin.")

    elif conversion_unit == "c":
        print(f"Temp is {temp} degrees Celsius.")

elif unit == "f":
    if conversion_unit == "c":
        print(f"Temp is {round((temp - 32) * 5 / 9, 1)} degrees Celsius.")
    elif conversion_unit == "k":
        print(f"Temp is {round(5 / 9 * (temp + 459.67), 1)} degrees Kelvin.")
    elif conversion_unit == "f":
        print(f"Temp is {temp} degrees Fahrenheit.")

elif unit == "k":
    if conversion_unit == "c":
        print(f"Temp is {round(temp - 273.15, 1)} degrees Celsius.")
    elif conversion_unit == "f":
        print(f"Temp is {round((temp - 273.15) * 9 / 5 + 32, 1)} degrees Fahrenheit.")
    elif conversion_unit == "k":
        print(f"Temp is {temp} degrees Kelvin.")

else:
    print(f"{unit} is an invalid unit")
