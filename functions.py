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





