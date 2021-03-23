##Animal is-a object
class Animal(object):
    pass

#THE DOG IS AN ANIMAL
class Dog(Animal):
    def __init__(self, name):
        #THE DOG HAS A NAME
        self.name = name

#THE CAT IS AN ANIMAL
class Cat(Animal):
    def __init__(self, name):
        #THE CAT HAS A NAME
        self.name = name


class Person(object):
    def __init__(self, name):
        #THE PERSON HAS A NAME
        self.name = name
        #THE PERSON CAN ALSO HAVE A PET
        self.pet = None

#THE EMPLOYEE IS A PERSON
class Employee(Person):
    def __init__(self, name):
        #access the init function of the person class
        super(Employee, self).__init__(name)
        #the employee has a salary
        self.salary =  salary

class Fish(object):
    pass

#THE SALMON IS-A FISH
class Salmon(Fish):
    pass

#THE HALIBUT IS-A FISH
class Halibut(Fish):
    pass

#rover is a dog, named "Rover"
rover = Dog("Rover")

#satan is a cat, named "Satan"
satan = Cat("Satan")

#mary is a person, named "Mary"
mary =  Person("Mary")

#mary's pet is satan
mary.pet = satan

#frank is an employee named "Frank" with a salary of 1200000
frank = Employee("Frank", 120000)

#frank's pet is rover, gets from person class
frank.pet = rover

#Fli[pper is a fish
flipper = Fish()

#crouse is a samon
crouse = Salmon()

#harry is a halibut
harry = Halibut()


