'''
import random
while True:
    a = random.randint(1,100)
    print(a)
    count = 0
    for i in range(1,6):
        userinput = int(input("Please enter the number from 1 to 100: "))
        count += 1
        if userinput == a:
            print("Congratulations!! 1000 kg or garlands")
        elif userinput < a:
            print("Please enter the higher value")
        else:
            print("Please enter the lower value")
        
        if count == 5:
            print("I am sorry but couldnot stop laughing at your try. :) You missed ",a)
            break
        

    wanttoplay = input("Do you want to play the game again?")
    if wanttoplay.lower() != 'yes':
        break
print("We are not much good at goodbyes!!")
'''





'''import random
count = 5

while count > 0 :
    a = random.randint(1, 100)
    print(a)
    
    for i in range(1, 6):
        userinput = int(input("Please enter a number from 1 to 100: "))
        count -= 1

        if userinput == a:
            print("You have won the game!")
            break
        elif userinput < a:
            print("Please enter the higher value")
        else:
            print("Please enter the lower value")
        if count == 0:
            print("You ran out of our counts.")
        else:
            continue
        
    wanttoplay = input("Hit YES if you want to play the game again: ")
    if wanttoplay.lower() != 'yes':
        break
    
print("Thanks for playing! Goodbye!")'''


### functions

'''import random
def playgame():
    Count = 5
    
    while Count > 0:
        a = random.randint(1, 100)
        print(a)
    
        for i in range(1, 6):
            userinput = int(input("Please enter a number from 1 to 100: "))
            count -= 1

            if userinput == a:
                print("You have won the game!")
                break
            elif userinput < a:
                print("Please enter the higher value")
            else:
                print("Please enter the lower value")
            if count == 5:
                print("You ran out of our counts.")
            else:
                continue
            

    
        wanttoplay = input("Hit YES if you want to play the game again: ")
        if wanttoplay.lower() != 'yes':
            break

    print("Thanks for playing! Goodbye!")
playgame()'''


### NUMBER GUESSING GAME WITH FUNCTIONS
import random
def playgame():
    a = random.randint(0,100)
    print(a)
    for i in range(5):
        count = 0
        userinput = int(input("Enter the number:"))
        count += 1
        if userinput == a:
            print("Congratulations")
            break
        elif userinput < a:
            print("Please enter the greater value")
        else :
            print("Please enter the smaller value")

    else:
        print("GAME OVER \nDONE WITH 5 TIMES \n The correct number is : ",a)

def playagain():
    again = input("Hit yes if you want to play again ").lower()
    if again == 'yes':
        playgame()
    else:
        print("You ran out of our count:")

playgame()
playagain()


            







