#class Factory():
   # a = 12

    #def hello(self):#methods
       # print("how are you")

    #print("hwllow what's up!!!")

#obj = Factory() #object

#print(obj.a)

#obj.hello()

#class Factory:
 #   def __init__(self,material,zip,pockets):
  #      self.material = material
   #     self.zip = zip
    #    self.pockets= pockets

    #def show(self):

#rebock = Factory("Leather",3,2)

#print(rebock.pockets)



# class Animal:
#     name = "lion"  # class attribute

#     def __init__(self, age):
#         self.age = age

#     def show(self):  # instance method
#         print(f"kirtee {self.age}")

#     @classmethod
#     def hello(cls):  # class method
#         print(f"how are you brother {cls.name}")  # use class attribute

#     @staticmethod
#     def static():  # static method
#         print("hello sister")


# obj = Animal(12)

# obj.show()      # kirtee 12
# obj.hello()     # how are you brother lion
# obj.static()    # hello sister

"""
INHERITANCE"""

# class Factoryrajkot:#parent class
#     a = "i am from rajkot"
#     def hello(self):
#         print("how are you")

# class Factoryahmedabad(Factoryrajkot):#child class
#       pass

# obj = Factoryrajkot()
# print(obj.a)

# obj2 = Factoryahmedabad()
# print(obj2.a)
# print(obj2.hello())


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"my name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name) #target class
#         self.age = age

#         def show(self):
#           print(f"my name is {self.name} and my age is {self.age}")

 
#     animals = Animal("lion")
#     animals.show()
# person1 = Human("kirtee", 25)
# person1.show()


# cumstroctur inheritance in this we write any one show and this work in both class and we can also write show in both class and this work in both class but if we write show in both class then the show of child class is execute because of method overriding

# class Factory:
#     def __init__(self,material,zip,pockets):
#         self.material = material
#         self.zip = zip
#         self.pockets= pockets

#     def show(self):
#             print(f"material is {self.material} and zip is {self.zip} and pockets are {self.pockets}")

# class Factoryrajkot(Factory):
#     def __init__(self,material,zip,pockets,color):
#         super().__init__(material,zip,pockets)
#         self.color = color

#     def show(self):
#             print(f"material is {self.material} and zip is {self.zip} and pockets are {self.pockets} and color is {self.color}")    

# class Factoryahmedabad(Factoryrajkot):
#     def __init__(self,material,zip,pockets,color,price):
#         super().__init__(material,zip,pockets,color)
#         self.price = price

#     def show(self):
#             print(f"material is {self.material} and zip is {self.zip} and pockets are {self.pockets} and color is {self.color} and price is {self.price}")

# factory = Factoryrajkot("cotton", "zip1", 2, "blue")
# factory.show()

"""Polymorphism
"""

# class Factory:
#     def __init__(self,material,zip):
#         self.material = material
#         self.zip = zip

#     def show(self):
#         print(f"material is {self.material} and zip is {self.zip}")

# class Factoryrajkot(Factory):
#     def __init__(self,material,zip,pocket):
#         super().__init__(material,zip)
#         self.pocket=pocket

#     def show(self):
#                     print(f"material is {self.material} and zip is {self.zip} and pocket is {self.pocket}")

# class Factoryahmdavad(Factoryrajkot):
#     def __init__(self,material,zip,pocket,price):
#         super().__init__(material,zip,pocket)
#         self.price = price

#     def show(self):
#             print(f"material is {self.material} and zip is {self.zip} and pocket is {self.pocket} and price is {self.price}")

# reebock = Factoryrajkot("leather",3,2)
# reebock.show()

"""
Abstract class is a class that contains one or more abstract methods. 
An abstract method is a method that is declared, but contains no implementation. 
Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods."""

# from abc import ABC, abstractmethod

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Square(shape):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

#     def perimeter(self):
#         return 4 * self.side

#     def show(self):
#         print(f"area of square is {self.area()} and perimeter of square is {self.perimeter()}")

# class Rectangle(shape):

#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

#     def show(self):
#         print(f"area of rectangle is {self.area()} and perimeter of rectangle is {self.perimeter()}")


# obj1 = Square(7)
# obj1.show()

"""Dunder methods
"""

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Animal: {self.name}"

#     def __repr__(self):
#         return f"Animal('{self.name}')"

#     def __add__(self, other):
#         if isinstance(other, Animal):
#             return Animal(self.name + " & " + other.name)
#         return NotImplemented

# obj1 = Animal("Lion")
# obj2 = Animal("Tiger")
# obj3 = obj1 + obj2
# print(obj3)

"""decorator is a function that takes another function and extends the behavior of the latter function without explicitly 
modifying it."""

def decorator_function(original_function):
    def wrapper():
        print("Before executing the function")
        original_function()
        print("After executing the function")
    return wrapper

@decorator_function
def hello():
    print("This is the original function.") 

hello()

