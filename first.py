# firstinput = int(input("Enter any number you want to: "))
# if firstinput == 50:
#   print('100')
# elif firstinput == 100:
#   print('50')
# else:
#   print("You are out of our range")

# yourInput = int(input("Enter the number 50 or 100:"))
# yourDict = {
#     50:100,
#     100:50
# }
# print(yourDict[yourInput])

# firstinput = int(input("Enter any number you want to: "))
# match firstinput:
#   case 50:
#     print(f"You had entered 50, So we will provide you 100.")
#   case 100:
#     print(f"You had entered 100. So we will provide you 50.")
#   case _:
#     print("You are out of our range:")

'''number = int(input("Enter the number 50 or 100: "))
dictionary = {50: 100, 100: 50}
result = dictionary.get(number)
print(result)'''

'''
mylist = [1,2,3,6,12,1,2,3,4,10]
#accessing the list length
print(len(mylist))

"""
#List, tuples, set and dictionary 
list = ordered, changeable, allow duplicates
tuples = ordered, unchangeable, allow duplicates
set = unordered, unchangeable, no duplicates
dict = ordered, changeable, no duplicates
"""
#accessing items in the list 
print(mylist[4:-1])
print(mylist[:2])
#Adding new elements in the list
mylist.append(True)
#extend can add any iterable to the list
#list can be extended with tuple using the extend function
mylist.extend([123])
mylist[2:4]=["okay", "not"]
#can only be inserted upto the specified range
mylist[11] = "Inserted"
print(mylist)
#can insert out of the range
mylist.insert(12,"Okay")
print(mylist)

'''

'''
##Removing the element from the list
mylist = [1,2,3,6,12,1,2,3,4,10]
mylist.remove(1)
mylist.pop()
# x = mylist.pop()
# print(x)
#deleted the list using del keyword
# del mylist
#clear empties the list
mylist.clear()
print(mylist)
'''



'''
#looping through the list and looping through the index numbers
newlist = [1,2,3,4,5,6,7]
#through each elements
for i in newlist:
    print(i)

#looping through index of each elements 
for i in range(len(newlist)):
    print(i)

i = 0
while i < len(newlist):
    print(i) #Return index
    print(newlist[i]) #return element
    i+=1
    if i == 5:
        break # terminate the loop after the condition occurs
else:
    #Executed after the completion of loop
    print("You are out of your loop")
'''


'''
### list comprehension as a shorthand for loop to work with item in the list
newlist = [1,2,3,4,5,6,7]
[print(i) for i in newlist]
[print(i) for i in range(len(newlist))]
x = [1,2,4,7,2,4,7]
new_x = [i for i in x if i > 2]
print(new_x)
'''

'''
##Shorthand if else statement
a = [1,2,4,7,2,4,7]
new_x = ["odd" if x%2 !=0 else "even" for x in a]
print(new_x)
'''

'''
#list methods
yourList = [1,4,5,2,89,45,23]
yourList.sort()
yourList.sort(reverse = True)
print(yourList)
'''
'''
##Sort and reverse in list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist.sort())
print(thislist)
#since sort is case sensitive , you need to change the string into lowercase or uppercase
thislist.sort(key = str.lower)
print(thislist)
thislist.reverse()
print(thislist)
'''
'''
x = [1,2,3,4]
#y = x # y will only be created as an instance of the x
y = x.copy() # so y is the copy
x.append(5)
print(y)
'''
'''
#joining lists 
x = [1,2,3,4]
y = [5,6,7,8]
print(x+y)
z = (9,10,11)
x.append(15) 
y.extend(z) #extend the iterable
x.extend(y)
print(x)
'''

'''
#other list method
x = [1,3,6,9,2,4,7,1,3,3,3,3,4]
print(x.index(9))
print(x.count(3))
'''

'''
fruits = ["apple", "mango", "papaya", "pineapple", "cherry"]
[*green, tropic, red] = fruits
print(green)
print(tropic)
print(red)
'''

'''
#sort and sorted in list
numbers1= [3, 1, 4, 1, 5, 9, 2, 6, 5]
okay = sorted(numbers1)
print(okay) 
print(numbers1)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.sort()
print(numbers) 
'''
'''
newtuple = (1,2,3,4,5,2,3,4,56,7,8,9,12,56,24,32,2,3,4,5)
print(newtuple.count(3))
print(newtuple.index(3))
print(newtuple.remove(3))
'''

'''#True and 1 are same, and False and 0 are same in sets
sets = {1,0,True,False}
print(sets)'''


'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# Update methods
set1.update(set2)
print("Update (set1):", set1)

set1.intersection_update(set2)
print("Intersection Update (set1):", set1)

set1.difference_update(set2)
print("Difference Update (set1):", set1)

set1.symmetric_difference_update(set2)
print("Symmetric Difference Update (set1):", set1)

'''


'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "Mustang" in thisdict["model"]:
  print("Yes, 'Mustang ' is one of the value of a key in the thisdict dictionary")
print(len(thisdict))
print(thisdict.keys())
print(thisdict.values())
print(thisdict["model"])
print(type(thisdict))

print(thisdict.get("model1","Not found"))

thisdict = dict(name = "John", age = 36, country = "Norway")
thisdict["gender"] = "male"
print(thisdict.keys())
thisdict["gender"] = "female"
print(thisdict.values())

for s in thisdict:
  print(s)
  print(thisdict[s])
for n in thisdict.values():
  print(n)

print(thisdict)
'''

'''
thisdict = dict(name = "John", age = 36, country = "Norway")

for i,j in thisdict.items():
  print(i,j)

thisdict2 = thisdict.copy()
thisdict3 = dict(thisdict)
print(thisdict)
print(thisdict2)
print(thisdict3)
'''

'''
#nested dictionary
country = {
    "nepal":{
        "firstletter" : "n",
        "secondletter" : "e"
    },
    "india":{
        "firstletter" : "i",
        "secondletter" : "n"
    },
    "china": {
        "firstletter" : "c",
        "secondletter" : "h"
    }
}
print(country["china"]['firstletter'])
'''

'''child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"]["name"])
'''
'''

# keys for the dictionary
alphabets = {'a', 'b', 'c'}

# value for the dictionary
number = 1

# creates a dictionary with keys and values
dictionary = dict.fromkeys(alphabets, number)

print(dictionary)

dictionary.setdefault('a',3)
print(dictionary)
'''

'''#shorthand if else
x = int(input("Enter the input number:"))
print("positive ") if x > 0 else print("negative") if x < 0 else print("Zero")
'''
 


'''##do while loop
while True:
    userinput = int(input("Enter the number"))
    if userinput < 0:
        break 

#while loop
i = 0
while i < 20:
    print(i+1)
    i+=1
'''

##$Functions in python
'''def addsurname(firstname): #parameter
    print(f"Your name is {firstname} Poudel")
addsurname('Hari')#argument
addsurname('Ram')'''

# list1 = [1,2,5,6]
# list1.insert(0,23)
# print(list1)
# list2 = [5,6,9]

# list1 = list1+ list2
# print(list1)
# print(list1[2:-2])

# x = list1.pop(2)
# y = list1.remove(9)
# print(list1,x,y)

# newlist1 = [x*2 for x in list1 if x <3 ]
# print(newlist1)

# newdict = {
#     "name": "Ram",
#     "age": 22,
#     "isnotmale" : True
# }
# newdict["country"] = "Nepal"
# print(newdict)
# print(newdict.get("address", "Not found"))
# newdict.setdefault("ismale",False)
# print(newdict)
# newdict.update
# print(newdict["country1"])



'''#####TODAYS TASK
newdict = {
    "name": "Ram",
    "age": 22,
    "isnotmale" : True
}
newdict.update({"country":"Nepal"})


## FIRST ONE
newdict1= dict([(x,y) for (y,x)in newdict.items() ])
print(newdict1)


## THIRD ONE
newdict1= [(x,y)for  y,x in newdict.items() ]
newdict1 = dict(newdict1)
print(newdict1)

##SECOND ONE
newdictionary = {}

for x,y in newdict.items():
    newdictionary.update([(y,x)])       
print(newdictionary)
'''

# newdict = {
#     "name": "Ram",
#     "age": 22,
#     "isnotmale" : True
# }
# newdict.update({"country":"Nepal"})
# del newdict["name"]
# newdict["Ram"]="name"
# print(newdict)



'''
newdict = {
    "name": "Ram",
    "age": 22,
    "isnotmale" : True
}
newdict.update({"country":"Nepal"})

removedkey = []
newdiction = {}
for c in newdict.keys():
    if c == "name":
        removedkey.append(c)
    

for i in removedkey:
    # newdict.pop(i)
    del newdict[i]

# newdiction["Ram"]= "name"
newdiction.update({"Ram": "name"})

for x,y in newdict.items():
    # newdiction.update([(x,y)])
    newdiction[x]= y

# print(newdict)
print(newdiction)

'''

# studentDetails = {
#     "name": "Sujan",
#     "faculty": "IT",
#     "roomNo": 101,
#     "gender":"male"
# }

# removedKey = []
# for i in studentDetails.items():
#     newdict.pop(i)

    
# newlist = [1,3,6,7,2,6,7,3,76]
'''
##TO PRINT THE LARGEST AND SECOND LARGEST OF THE LIST
newlist = [1,3,6,7,2,6,7,3,76,32,45]
largest = 0
secondlargest = 0
for i in newlist:
    if i > largest:
        secondlargest = largest
        largest = i
    else:
        secondlargest = i
print(largest,secondlargest)
'''
'''

newlist = [1,3,6,7,2,6,7,3,76,32,45]

## to convert the newlist into a new form with elements unrepeated of its own
unrepeatedlist = []
for i in newlist:
    if i not in unrepeatedlist:
        unrepeatedlist.append(i)
print(unrepeatedlist)

 




### to count the each element in the newlist
for i in unrepeatedlist:
    count = 0
    for j in newlist:
        if i == j:
          count+=1
    print(i,count)

print(sorted(newlist))





'''

# students = [
#     {
#         "name":"nabin",
#         "age":18,
#         "gender":"male",
#         "score":90
#     },{
#         "name":"Sabin",
#         "age":17,
#         "gender":"male",
#         "score":46
#     },
#     {
#         "name":"Gota",
#         "age":22,
#         "gender":"female",
#         "score":90
#     },
#     {
#         "name":"nabina",
#         "age":18,
#         "gender":"female",
#         "score":68
#     }
#     ]


##swapping without using temp variable
'''a = 3
b =4
c = 5
a,b,c = c,a,b
print(a,b,c)'''
        
'''
#### Python program to sort  numbers in a list
NumberList = [12,34,78,23,67,90,24,78,15,67]
for i in range(len(NumberList)):
    for j in range(i+1,len(NumberList)):
        if NumberList[i] < NumberList[j]:
            NumberList[i],NumberList[j] = NumberList[i],NumberList[j]
        else:
            NumberList[i],NumberList[j] = NumberList[j],NumberList[i]
print(NumberList)


### program to sort the list of the dictionary according to a key of dictionary in the list
students = [
    {
        "name":"nabin",
        "age":18,
        "gender":"male",
        "score":90
    },{
        "name":"Sabin",
        "age":17,
        "gender":"male",
        "score":46
    },
    {
        "name":"Gota",
        "age":22,
        "gender":"female",
        "score":90
    },
    {
        "name":"nabina",
        "age":18,
        "gender":"female",
        "score":68
    }
]
for i in range(len(students)):
    for j in range(i+1,len(students)):
        if students[i]['age'] > students[j]['age']:
            temp_age = students[i]['age']
            students[i]['age'] = students[j]['age']
            students[j]['age'] = temp_age
print(students)
print(students[0]["age"])

'''









    # if userInput != a and i!=6:
    #     i += 1
    #     continue
    # elif userInput!=a and i == 6:
    #     print("Sorry!! you are not the looser but you failed to win!!")

    # else:
    #     print(f"Congratulations !! You have won the game. The number you guessed {userInput} match with my number {a}")


        
