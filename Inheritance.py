'''
###Single Level Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name)
        print(self.age)
    
    def showdetails(self):
        print(f"My name is {self.name} and I am {self.age} years old.")



class Employee(Person):
    def __init__(self, name, age, salary, department):
        self.salary = salary
        self.department = department
        # Person.__init__(name,age)
        super().__init__(name, age)

    def display(self):
        # super().display()
        print(self.name,self.age,self.salary,self.department)

    def introduce(self):
        print(f"Hello There!! My name is {self.name}.\nI am {self.age} years old. \nI earn around Rs.{self.salary}.\nI work in the {self.department}\n\tTHANKYOU!!")




a = Employee('Rahul', 24, 200000, "Human Resource")
b = Employee("Rabin", 26, 150000, "Management")
a.display()
b.display()
a.introduce()
b.introduce()

### MultiLevel Inheritance


class Manager(Employee):
    def __init__(self, name, age, salary, department,title,phone):
        super().__init__(name, age, salary, department)
        self.title = title
        self.phone = phone

    def strictness(self):
        print("The manager is not much strict as compared to others.")

c = Manager("Rabina", 16, 15000000, "HR", "General Manager", 9823564782)
c.strictness()
c.showdetails()
c.introduce()
'''

'''### Getters and setter in python
class Number:
    def __init__(self,num):
        self.num = num
    def displayhalf(self):
        return self.num/2
    def displayokay(self):
        return self.num
    @property
    def display(self):
        print(self.num)
    @display.setter
    def display(self, n):
        if n < 0 and n > 10:
            print("Invalid input")
        else:
            self.num = n
firstnum = Number(1)
print(firstnum.displayhalf())
firstnum.display = 6
print(firstnum.display)'''

'''
class Sample:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    @property
    def fullname(self):
        return f"{self.fname } {self.lname}"
rakesh = Sample("Rakesh","Bachhan", 23)
print(rakesh.fullname)



'''