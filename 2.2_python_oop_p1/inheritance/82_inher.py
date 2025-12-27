class Animal:
    def eat(self):
        print("Animal is eating.")
    
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

puppy  = Dog()
puppy.eat() # due to inheritance with Animal class
puppy.bark()