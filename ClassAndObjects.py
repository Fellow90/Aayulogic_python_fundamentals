'''##create a class called rectangle with attributes width and height and define a method to calculate the area
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def show(self):
        print(f"I am a rectangle with a width of {self.width} meters and the height of {self.height}meters.")

    def Area(self):
        return self.width*self.height
    
first = Rectangle(12,8)
second = Rectangle(28,20)
first.show()
second.show()
print(first.Area())
print(second.Area())'''

'''### Create a class named student with attribute as name and age and method as show details
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showdetails(self):
        print(f"My name is {self.name} and my age is {self.age}.")
s1 = Student("Birat",25)
s2 = Student("Sandhya",23)
s1.showdetails()
s2.showdetails()'''
'''
##Create a class programmer for storing information of a few programmers working at Microsoft.
class Programmer:
    def __init__(self,name,age,salary,script):
        self.name = name
        self.age = age
        self.salary = salary
        self.script = script
    
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print(self.script)


    
    def showdetails(self):
        print(f"My name is {self.name} and I am {self.age} years old.\nI earn around {self.salary} and I am cool with {self.script}.")
    
p1 = Programmer("Yuran",36, 250000, "Application Language")
p1.display()
p1.showdetails()'''
'''
##Write a class calculator capable of finding square, cube, and the square root of a number.
#Also Add a static method in problem 2 to greet the user with hello.

class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        return self.n **2
    def cube(self):
        print(self.n ** 3)
    def squareroot(self):
        print(self.n ** 0.5)
    @staticmethod
    def greetuser():
        print("Hello")
    
a = Calculator(4)
b = Calculator(5)
a.greetuser()
print(a.square(),b.square())
a.cube()
b.cube()
a.squareroot()
b.squareroot()
'''

'''
#Create a class with a class attribute a; 
# create an object from it and set a directly using object.a=0 
# Does this change the class attribute?
class SampleClass:
    a=5
anobject = SampleClass()
anobject.SampleClass = 24
print(anobject.a)
print(SampleClass.a)
'''

### Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.
# Can you change the self parameter inside a class to something else (say ‘harry’)? Try changing self to ‘slf’ or ‘harry’ and see the effects.'''
# The answer is yes. whatever you want to write
'''
class Train:
    def __init__(okay,name,fair,seats,fromsource,todest):
        okay.name = name
        okay.fair = fair
        okay.seats = seats
        okay.fromsource = fromsource
        okay.todest = todest
    def display(self):
        print(self.name, self.fair, self.seats, self.fromsource, self.todest)
    def book(self):
        if self.seats > 0:
            print("You have booked the ticket.", self.seats)
            self.seats -= 1
        else:
            print("Sorry!! No tickets left.")
    def rununderindia(self):
        if self.todest == "India":
            print(self.name, self.fair, self.seats,self.fromsource, self.todest)
        else:
            print("Sorry!! We are unable to count the record.")
a = Train("HellWay",50, 3, "Nepal", "India")
a.display()
a.book()
a.book()
a.book()
a.book()
a.display()
a.rununderindia()

'''