def menu():
    print("\n" + "=" * 50)
    print("Unit Converter")
    print("=" * 50)
    print()

    print("1. Length")
    print("2. Weigth")
    print("3. Temperature")


def find_length():
    length = int(input("Enter the length to convert : "))
    print()

    unit_convert_from = int(
        input(
            "Select unit to convert from: \n1. millimeter \n2. centimeter \n3. meter \n4. kilometer \n5. inch \n6. foot \n7. yard \n8. mile \nyour choice : "
        )
    )
    print()
    unit_convert_to = int(
        input(
            "Select unit to convert to:\n1. millimeter\n2. centimeter \n3. meter\n4. kilometer \n5. inch\n6. foot\n7. yard\n8. mile\nyour choice (1-8) : "
        )
    )

    list_unit_length = [
        "millimeter",
        "centimeter",
        "meter",
        "kilometer",
        "inch",
        "foot",
        "yard",
        "mile",
    ]

    length_conversion = {
        "meter": (1, "m"),
        "millimeter": (1000, "mm"),
        "centimeter": (100, "cm"),
        "kilometer": (0.001, "km"),
        "inch": (39.37, "in"),
        "foot": (3.281, "ft"),
        "yard": (1.094, "yd"),
        "mile": (0.000621371, "mi"),
    }

    a = unit_convert_from - 1
    b = unit_convert_to - 1

    unit_from = list_unit_length[a]
    unit_to = list_unit_length[b]

    to_meter = length / length_conversion[unit_from][0]
    to_united_wanted = to_meter * length_conversion[unit_to][0]

    print(
        f"\n{length} {length_conversion[unit_from][1]} = {to_united_wanted:.4f} {length_conversion[unit_to][1]}"
    )


def find_weigth():

    weight = int(input("Enter the weigth to convert : "))
    print()

    unit_convert_from = int(
        input(
            "Select unit to convert from: \n1. milligram \n2. gram \n3. kilogram \n4. ounce \n5.pound \n your choice (1-5) : "
        )
    )
    print()
    unit_convert_to = int(
        input(
            "Select unit to convert to: \n1. milligram \n2. gram \n3. kilogram \n4. ounce \n5.pound \n your choice (1-5) : "
        )
    )

    list_unit_weigth = ["milligram", "gram", "kilogram", "ounce", "pound"]

    weigth_conversion = {
        "gram": (1, "g"),
        "milligram": (1000, "mg"),
        "kilogram": (0.001, "kg"),
        "ounce": (39.37, "oz"),
        "pound": (3.281, "pd"),
    }

    a = unit_convert_from - 1
    b = unit_convert_to - 1

    unit_from = list_unit_weigth[a]
    unit_to = list_unit_weigth[b]

    to_gram = weight / weigth_conversion[unit_from][0]
    to_united_wanted = to_gram * weigth_conversion[unit_to][0]

    print(
        f"\n{weight} {weigth_conversion[unit_from][1]} = {to_united_wanted:.4f} {weigth_conversion[unit_to][1]}"
    )


def find_temp():

    temp = int(input("Enter the temperature to convert : "))
    print()

    unit_convert_from = int(
        input(
            "Select unit to convert from: \n1.celsius \n2.fahrenheit \n3.kelvin your choice (1-3) : "
        )
    )
    print()
    unit_convert_to = int(
        input(
            "Select unit to convert from: \n1.celsius \n2.fahrenheit \n3.kelvin your choice (1-3) : "
        )
    )

    list_unit_temp = ["celsius", "fahrenheit", "kelvin"]

    a = unit_convert_from - 1
    b = unit_convert_to - 1

    unit_from = list_unit_temp[a]
    unit_to = list_unit_temp[b]

    if unit_from == "celsius":
        to_celsius = temp
        u = "°C"
    elif unit_from == "fahrenheit":
        to_celsius = (temp - 32) * (5 / 9)
        u = "°F"
    elif unit_from == "kelvin":
        to_celsius = temp - 273.15
        u = "°K"

    if unit_to == "celsius":
        to_united_wanted = to_celsius
        ut = "°C"
    if unit_to == "fahrenheit":
        to_united_wanted = (to_celsius * 9 / 5) + 32
        ut = "°F"
    if unit_to == "kelvin":
        to_united_wanted = to_celsius + 273.15
        ut = "°K"

    print(f"\n{temp} {u} = {to_united_wanted:.4f} {ut}")


if __name__ == "__main__":
    menu()
    choice = int(input("Select between unit of mesurement brlow : "))

    if choice == 1:
        find_length()
    elif choice == 2:
        find_weigth()
    elif choice == 3:
        find_temp()
    else:
        print("Invalide choice. Please choose a correct number !")
