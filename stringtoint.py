def main():
    try:
        input_str = input("Enter an integer as a string: ")
        int_value = int(input_str)
        print(f"Converted integer value: {int_value}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
