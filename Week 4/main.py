from rectangle import Rectangle

def main():
    print("=== Land Calculator ===")

    try:
        length = float(input("Enter length of land: "))
        width = float(input("Enter width of land: "))

        land = Rectangle(length, width)

        area = land.calculate_area()
        perimeter = land.calculate_perimeter()

        print(f"\nArea of land: {area}")
        print(f"Perimeter of land: {perimeter}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()