def read_file_safely():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"\n❌ Error: You don't have permission to read '{filename}'.")
    except IsADirectoryError:
        print(f"\n❌ Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"\n❌ Error: Cannot decode contents of '{filename}' (possibly binary).")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
    else:
        print("\n✅ File read successfully!")
    finally:
        print("\n🔚 Program finished.")

# Run the function
if __name__ == "__main__":
    read_file_safely()
