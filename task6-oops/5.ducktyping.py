class Lion:
    def roar(self):
        print("lion roar harder")

class Tiger:
    def roar(self):
        print("tiger roar")

# Duck typing - no need for inheritance, just method names
def make_it_roar(creature):
    creature.roar()

make_it_roar(Lion())
make_it_roar(Tiger())

