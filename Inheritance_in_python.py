class Animal:
    def walk(self):
        print("Walk")
class Mamul(Animal):
    def eat(self):
        print("eat")
class Fish(Animal):
    def swim(self):
        print("swim")
mamul = Mamul()
fish = Fish()
mamul.walk()
fish.swim()

        
    