class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Polymorphism - same method name, different behaviors
for animal in [Dog(), Cat()]:
    print(animal.sound())
