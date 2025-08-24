def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add(num1, num2)
    print(f"The sum of the two numbers is {result}")


if __name__ == "__main__":
    main()
