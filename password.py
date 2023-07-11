'''Steps to Implement in password generator:

Prompt the user to enter the desired length of the password.
Ask the user which character types they want to include in the password (e.g., lowercase letters, uppercase letters, numbers, special characters).
Generate a random password based on the user's specifications.
Display the generated password to the user'''
'''

import random,string

def generatepassword():
    
    print("Password will consist of lowercase, uppercase, digits and special characters")
    length = int(input("Which length of the password you want us to help with?"))
    if length < 4:
        print("Password length should be at least of 4:")
        return None
    lowerCase = list(string.ascii_lowercase)
    upperCase = list(string.ascii_uppercase)

    digits = [x for x in range(10)]
    specialSymbols = list(string.punctuation)
    allmostsymbols = lowerCase + upperCase + digits + specialSymbols

    password = [random.choice(lowerCase), random.choice(upperCase), random.choice(digits), random.choice(specialSymbols)]
    
    # for i in range(length - 4):
    #     password.append(random.choice(allmostsymbols))
    password.extend(random.choice(allmostsymbols) for i in range(length - int(4)))
    

    random.shuffle(password)

    stringpassword = "".join(str(letter) for letter in password)

    print(stringpassword)



    # password=[random.choice(allmostsymbols) for x in range(length)]

    # stringpassword = "".join(str(letter) for letter in password)


    # stringpassword = ""
    # for i in password:
    #     stringpassword += str(i)
    


        
    # print(stringpassword)


generatepassword()    

'''



'''
### password generator with desired length of letter digits and other special characters
import random,string
length = int(input("Which length of the password you want us to help with?"))
lowerletterlength = int(input("How many lower letter?"))
upperletterlenth = int(input("How many upper letter?"))
digitlength = int(input("How many digits?"))
specialcharacterlength = int(input("How many special characters?"))

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
digits = list(string.digits)
specialcharacter = list(string.punctuation)
allmost = lowercase + uppercase + digits + specialcharacter

lowercaseList = []
uppercaseList = []
digitslist = []
specialcharacterList = []

for _ in range(lowerletterlength):
    lowercaseList.append(random.choice(lowercase))
print(lowercaseList)

for _ in range(upperletterlenth):
    uppercaseList.append(random.choice(uppercase))
print(uppercaseList)


for _ in range(digitlength):
    digitslist.append(random.choice(digits))
print(digitslist)

for _ in range(specialcharacterlength):
    specialcharacterList.append(random.choice(specialcharacter))
print(specialcharacterList)


atleastPassword = lowercaseList + uppercaseList + digitslist + specialcharacterList

for i in range(length - len(atleastPassword)):
    atleastPassword.append(random.choice(allmost))

random.shuffle(atleastPassword)

finalpassword = "".join(str(i) for i in atleastPassword)

print(finalpassword)'''

'''#ride the rollercoaster if your height is equal to or greater than 120 cm and the charge is free if your age is between 45-55
height = int(input("Enter your height:"))
if height >= 120:
    age = int(input("Enter your age: "))
    if age > 45 and age < 55:
        print("We offer you a ride with free of cost.")
    else:
        print("Oops !! Pay full")   
else:
    print("Sorry!! We want you to grow up")'''

'''#scissor pape rock
import random
scissor = 1
paper = 2
rock = 3
userinput = input("Hit S for Scissor, P for paper and  R for rock:")
if userinput == 'S':
    userchoice = scissor
elif userinput == 'P':
    userchoice = paper
elif userinput == 'R':
    userchoice = rock
else:
    print("Enter as specified")
computerchoice = random.choice([scissor,paper,rock])
print(userchoice,computerchoice)

if userchoice != computerchoice:
    if userchoice - computerchoice == 1 or userchoice - computerchoice ==-2:
        print("You loose")
    else:
        print("You win")
        
else:
    print("Draw")
'''

### Demonstration of lambda function
def exponential(n):
    return lambda a : a ** n
firstpower = exponential(1)
square = exponential(2)
cube = exponential(3)
print(firstpower(11))
print(square(2))
print(cube(3))





