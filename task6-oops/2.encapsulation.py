
class MyClass:
    def __init__(self):
        self.name = "Aman"  # public variable

    def display(self):  # public method
        print("Name:", self.name)

obj = MyClass()
print(obj.name)   
obj.display()       
