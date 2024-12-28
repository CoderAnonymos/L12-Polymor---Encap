class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def info(self):

        print(f"My name is {self.name} and I am {self.age} years old.")


    def make_sound(self):

        print("Bark")


class Cat:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def info(self):

        print(f"My name is {self.name} and I am {self.age} years old.")


    def make_sound(self):

        print("Meow")


dog = Dog("Rory", 4.8)
cat = Cat("Scanter", 12)

for animals in(dog, cat):

    animals.make_sound()
    animals.info()