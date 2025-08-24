class Myerror(Exception):
    pass
try:
    age = int(input("enter the age: "))
    if age <= 0:
        raise Myerror("age cannot be zero or less than zero")
except Myerror as e:
    print("error:",e)