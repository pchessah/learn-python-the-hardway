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
    def __init__(self, name):\
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
