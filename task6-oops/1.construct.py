# defining class
class Animal:
   # constructor    
   def __init__(self, species, name):
      self.species = species
      self.name = name
   
   # method of the class
   def description(self):
      return f"{self.species} is  {self.name} species"

# creating object of the class
animalObj = Animal("labrador", "dog")
print(animalObj.description()) 