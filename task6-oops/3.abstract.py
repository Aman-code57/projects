from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road.")

class Boat(Vehicle):
    def drive(self):
        print("Boat is sailing on the water.")

# car = Vehicle() # This would raise a TypeError as Vehicle is an abstract class
my_car = Car()
my_boat = Boat()

my_car.drive()
my_boat.drive()