def main():
    input_str = input("Enter a number: ")

    if is_palindrome(input_str):
        print("The number is a palindrome!")
    else:
        print("The number is not a palindrome.")


def is_palindrome(input_str):
    reversed_str = input_str[::-1]
    return input_str == reversed_str


if __name__ == "__main__":
    main()
