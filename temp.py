def main():
    num1 = 10.5
    num2 = 20.3

    print("Before swapping:")
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")

    temp = num1
    num1 = num2
    num2 = temp

    print("\nAfter swapping:")
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")


if __name__ == "__main__":
    main()
