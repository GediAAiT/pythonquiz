def main():
    try:
        input_str = input("Enter a number: ")
        number = int(input_str)
        square = number * number
        print(f"The square of {number} is {square}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
