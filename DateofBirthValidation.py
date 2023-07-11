'''import datetime
currentDate = datetime.date.today()
currentDate = str(currentDate).split("-")
userinput = input("Enter the date of birth in YYYY/MM/DD format ").split("/")
toyear = int(currentDate[0])
tomonth = int(currentDate[1])
todate = int(currentDate[2])
print(f"{toyear}/{tomonth}/{todate}")
uyear = int(userinput[0])
umonth = int(userinput[1])
udate = int(userinput[2])
print(f"{uyear}/{umonth}/{udate}")

DaysCountInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
Monthtodays = {}
for i in range(len(DaysCountInMonths)):
    Monthtodays[i+1] = DaysCountInMonths[i]

def calculateDays(key):
    return sum(value for k,value in Monthtodays.items() if k <= key - 1)

userUptoPreviousMonth = calculateDays(umonth)
todayUptoPreviousMonth = calculateDays(tomonth)

totalUserDays = userUptoPreviousMonth + udate
totaltodayDays = todayUptoPreviousMonth + todate

if totalUserDays != totaltodayDays:
    calcdate = totalUserDays - totaltodayDays
    if calcdate > 0:
        print("You birthday is after ",calcdate," days.")
    else:
        print(f"Your birthday was before {abs(calcdate)} days.")
    
else:
     a = input("Please Enter your name: ")
     print("Happy Birthday!!",a.upper())
'''





'''
from datetime import datetime
from dateutil import relativedelta

currentDate = datetime.today()
myday = datetime.strftime(currentDate,"%d/%m/%Y").split("/")
todaysDate = str(int(myday[0])) + "/" + str(int(myday[1])) + "/" + str(int(myday[2]))

userinput = input("Enter your days of birth in D/M/Y format:")
userdate = datetime.strptime(userinput, "%d/%m/%Y")



        
thisdate = datetime.strptime(todaysDate, "%d/%m/%Y")


DateDifference = relativedelta.relativedelta(thisdate, userdate)
print('Years, Months, Days between two dates is')
print(DateDifference.years, 'Years,', DateDifference.months, 'months,', DateDifference.days, 'days')
'''


##calculates the age left till the next birthday assuming there are 30 days in a month.
from datetime import datetime
from dateutil import relativedelta
def validateuserinput():
    Validate = True
    while Validate:

        currentDate = datetime.today()
        myday = datetime.strftime(currentDate,"%d/%m/%Y").split("/")
        todaysDate = str(int(myday[0])) + "/" + str(int(myday[1])) + "/" + str(int(myday[2]))
        userinput = input("Enter your days of birth in D/M/Y format:")
        DaysCountInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
        Monthtodays = {}
        for i in range(len(DaysCountInMonths)):
            Monthtodays[i+1] = DaysCountInMonths[i]
        userdate = datetime.strptime(userinput, "%d/%m/%Y")
        if userdate.day > 31 and userdate.month >12:
            print("Please enter the valid credentials")
            Validate = False
            
        else:
            pass
        thisdate = datetime.strptime(todaysDate, "%d/%m/%Y")
        DateDifference = relativedelta.relativedelta(thisdate, userdate)
        print('Years, Months, Days between two dates is')
        print(DateDifference.years, 'Years,', DateDifference.months, 'months,', DateDifference.days, 'days')
        print(f"You are {DateDifference.years} years , {DateDifference.months} months and {DateDifference.days} days older.")
        for i in range(len(DaysCountInMonths)):
            if DateDifference.months == 0:
                if DateDifference.days  == 0:
                    print("Happy Birthday:")
                else:
                    print(f"Your birthday is after { 30 - DateDifference.days} months")
            else:
                print(f"Your birthday is after {11 - DateDifference.months} months and {30 - DateDifference.days} days.")
            Validate = False
print(validateuserinput())


    

        