class MyError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 0:
        raise MyError("Age cannot be negative")
except MyError as e:
    print("❌ Error:", e)
