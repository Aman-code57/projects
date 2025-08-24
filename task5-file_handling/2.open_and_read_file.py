def main():
    """Read and print the content of a file."""
    with open("aman.txt", "r") as file:
        content = file.read()
    print(content)


if __name__ == "__main__":
    main()