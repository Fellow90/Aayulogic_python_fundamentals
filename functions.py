'''def power(n):
    
    return lambda x : x**n
square = power(2)
cube = power(3)
quad = power(4)
pent = power(5)
print(square(3),cube(4),quad(5), pent(6))
print(power(4)(3))'''

# def factorial(n):
#     if n == 0:
    
'''
##calculates the age left till the next birthday assuming there are 30 days in a month.
from datetime import datetime
from dateutil import relativedelta
def validateuserinput():
    while True:
        todaysdate = datetime.today()
        userinput = input("Enter your days of birth in D/M/Y format:")
        
        userdate = datetime.strptime(userinput, "%d/%m/%Y")
        if userdate.day > 31 and userdate.month >12:
            print("Please enter the valid credentials")
            break
        else:
            pass
        thisdate = datetime.strptime(todaysdate, "%d/%m/%Y")
        DateDifference = relativedelta.relativedelta(thisdate, userdate)
        print('Years, Months, Days between two dates is')
        print(DateDifference.years, 'Years,', DateDifference.months, 'months,', DateDifference.days, 'days')
        print(f"You are {DateDifference.years} years , {DateDifference.months} months and {DateDifference.days} days older.")
        if DateDifference.months == 0:
            if DateDifference.days  == 0:
               print("Happy Birthday:")
            else:
                print(f"Your birthday is after { 30 - DateDifference.days} months")
        else:
            print(f"Your birthday is after {11 - DateDifference.months} months and {30 - DateDifference.days} days.")
        break
print(validateuserinput())'''

'''def add(a):
    def inner(b):
        return a + b
    return inner
# firstadd = add(5)
# secondadd = add(10)
# thirdadd = add(15)
# final1st = firstadd(6)
# final2nd = secondadd(12)
# final3rd = thirdadd(18)
# print(final1st,final2nd,final3rd)
print((add(5))(6))
print(add("abc")("def"))'''

'''
### Getter and setter decorator in python
class person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        self._age = value

person1 = person("Kripesh", 24)
person2 = person("Niraj", 32)
print(person1.name)
person1.name = "Ritesh"
print(person1.name,person1.age, person2.name, person2.age)'''

### difference between using getter and without using getter
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def okay(self):
        return self.name
    @property
    def okay2(self):
        return self.name
employee1 = Employee("Birat", 24)
print(employee1.okay())
print(employee1.okay2)






