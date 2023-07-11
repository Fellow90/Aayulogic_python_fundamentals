'''Numbers = [38,67,98,25,67,89,29,36,46,78]
n = len(Numbers)
for i in range(n-1):
    for j in range(n-i-1):
        # if Numbers[j] > Numbers[j+1]:
        #     Numbers[j],Numbers[j+1]  = Numbers[j+1], Numbers[j]
        if Numbers[j]<Numbers[j+1]:
            Numbers[j],Numbers[j+1]  = Numbers[j+1], Numbers[j]
print(Numbers)'''


# Numbers = [38,67,98,25,67,89,89,29,36,38,89,46,78]
# smallest = Numbers[2]
# largest = 0
# secondlargest = 0
# for i in Numbers:
#     if i < smallest:
#         smallest = i
#     if i > largest:
#         secondlargest = largest
#         largest = i
#     else: 
#         secondlargest = i
#         largest = largest
# print(smallest,largest,secondlargest)


# Numbers = [38,67,98,25,67,89,89,29,36,38,89,46,78]

# Unrepeated = set(Numbers)
# for i in Unrepeated:
#     count = 0
#     for j in Numbers:
#         if i == j:
#             count+=1
#     print(i,count)
 

'''## Program to find the sum
Numbers = [38,67,98,25,67,89,89,29,36,38,89,46,78]

sum = 0
for i in Numbers:
    sum+=i

print(sum)
'''
'''##print all the even numbers in the list
even = []
Numbers = [38,67,98,25,67,89,89,29,36,38,89,46,78]
for i in Numbers:
    if i % 2 == 0:
        even.append(i)
print(even)
'''
'''# Write a function that takes a list of words and returns a new list containing the lengths of the corresponding words.
wordList = input("Enter the text to get the list of words:  ")
newList = wordList.split(" ")
def convertLength(str):
    

    for i in range(len(newList)):
        print(newList[i],len(newList[i]))
convertLength(newList)    
'''


##Write a function that takes a list of words and returns a new list containing the lengths of the corresponding words.
'''List1 = [1,2,4,5,7,9,2,6,8,8,9]
List2 = [3,6,4,8,9,12,25,1,5]  
CommonList = set()
for i in List1:
    for j in List2:
        if i == j:
            CommonList.add(i)
print(list(CommonList))'''
'''

###OR
List1 = [1,2,4,5,7,9,2,6,8,8,9]
List2 = [3,6,4,8,9,12,25,1,5]  
CommonList = []
for i in List1:
    if i in List2:
        CommonList.append(i)
print(CommonList)
'''

'''## Write a program to swap the value of two variables using tuple unpacking
a = int(input("Enter the first value of tuple:"))
b = int(input("Enter the second value of the tuple: "))
print("Before swapping",a,b)
(a,b)=(b,a)
print("After swapping",a,b)
'''
'''
##CREATE THE TUPLE OF YOUR FAVOURITE MOVIE AND PRINT THEM IN ALPHABETICAL ORDER
MyFavouriteMovie = ("Spiderman","Batman","Superman", "Dark Knight", "Suicide Squad")
MyFavouriteMovieList = sorted(list(MyFavouriteMovie))
print(MyFavouriteMovieList)'''

'''### Create a function that takes the tuple of the numbers and return the product of all elements
def returnproduct(numbers):
    product = 1
    for i in numbers:
        product *= i
    return product
print(returnproduct((1,2,3,4,5,6,7,8)))'''

'''### Given a list of tuples, sort the list based on second element  and also first element of each tuples
listoftuple = [(1,2),(3,4),(6,3),(2,1)]
print(sorted(listoftuple, key = lambda x:x[1]))
print(sorted(listoftuple,key = lambda x:x))
'''

'''##Write a program to remove duplicate elements from a given list using sets
yourlist = [1,3,4,7,9,2,3,6,8,3,5,7,9,3,6,8]
print(list(set(yourlist)))'''

'''##Create two sets of numbers and find their union, intersection,symmetric difference and difference
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
set3 = set1.union(set2) 
set4 = set1.intersection(set2) 
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)  
print(set3)
print(set4)    
print(set5)
print(set6)'''

'''###Write a function that checks whether two sets are disjoint or not
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
def checkdisjoint(a,b):
    return a.isdisjoint(b)
print(checkdisjoint(set1,set2))
'''
'''
## Write a program to that return the unique element of the union of the first set in set3 and second set in set4
set1 = {1,2,3,4,5,6,7,8}
set2 = {5,6,7,8,9,10,11,12}
def uniqueness(firstset,secondset):
    set3 = set1.difference(set2)
    set4 = set2.difference(set1)
    return set3,set4
set3,set4 = uniqueness(set1,set2)
print(f"The set with only of first set is : {set3} and the set with only of second set is : {set4}")
'''

'''
#####===== DIDNT WORKED
Write a program to merge two dictionaries into a new dictionary.
Given a dictionary, write a program to find the key with the maximum value.
Write a function that takes a string and returns a dictionary with the count of each character in the string.'''



'''def lengthWord(inputWord):
    dictWord = {}
    for i in inputWord:
        dictWord.update({i:len(i)})
    return dictWord
words = input("Enter the word you want to and count them as in addition:").split(" ")
countwords = lengthWord(words)
print(countwords)'''
'''
### program to merge the two dictionaries
FirstDict = {
    "name":"Sujan",
    "age":18,
    "gender": "male"
}
SecondDict = {
    "mname":"Sujana",
    "mage":28,
    "mgender": "female"
}
# FirstDict.update(SecondDict)
for x,y in SecondDict.items():
    FirstDict[x] = y
print(FirstDict)
'''
'''###Write a program to find the key with a minimum value
DictQUest = {
    1:11,
    2:15,
    3:56,
    67:25,
    46:24,
    28:63,
    45:57
}
# keys = list(DictQUest.keys())
# print(keys)
# for i in range(len(DictQUest)):
#     for j in range(i+1,len(DictQUest)):
#         if DictQUest[keys[i]]>DictQUest[keys[j]]:
#             keys[i],keys[j]= keys[j],keys[i]
# print(keys)
# sortedwithkeys = {}
# for key in keys:
#     sortedwithkeys[key] = DictQUest[key]
# print(sortedwithkeys)

##second option using enumerate
keys = list(DictQUest.keys())
for i in range(len(DictQUest)):
    for j in range(i+1, len(DictQUest)):
        if DictQUest[keys[i]] > DictQUest[keys[j]]:
            keys[i],keys[j] = keys[j],keys[i]
for i,key in enumerate(keys):
    DictQUest[key] = DictQUest[keys[i]]
print(DictQUest)

'''

###function that takes string and return the output as the count of the word in the string
'''
def countWord():
    inputstring = input("Enter the input string:")
    return len(inputstring)
print(countWord())
'''

'''#### program to count the length of the string
def countWord():
    inputstring = input("Enter the input string:")
    count = 0
    for i in inputstring:
        count+=1
    return count
print(countWord())
'''
students = [
    {
        "name": "Alice",
        "age": 20,
        "roll_number": "A001",
        "subjects": ["Math", "Physics"],
        "score":98
    },
    {
        "name": "Bob",
        "age": 19,
        "roll_number": "A002",
        "subjects": ["Physics", "Chemistry"],
        "score":91
    },
    {
        "name": "Charlie",
        "age": 21,
        "roll_number": "A003",
        "subjects": ["Math", "Chemistry"],
        "score":45
    },
    {
        "name": "David",
        "age": 20,
        "roll_number": "A004",
        "subjects": ["Biology", "History"],
        "score": 100
    },
    {
        "name": "John",
        "age": 19,
        "roll_number": "A005",
        "subjects": ["Math", "Physics", "Chemistry"],
        "score":70
    }
]
'''
asubjectlist = []
for i in students:
    for j in i["subjects"]:
        
        if j not in asubjectlist:
            asubjectlist.append(j)
print(asubjectlist)'''
'''
###using set
asubject = set()
for i in students:
    for j in i["subjects"]:
        if j in i["subjects"]:
            asubject.add(j)
print(asubject)
#### return the list of tuples of student with their respective name and roll number
StudentsList = []
for i in students:
    name = i["name"]
    roll_number = i['roll_number']
    tupleofstudent = (name,roll_number)
    StudentsList.append(tupleofstudent)
print(StudentsList)
'''
'''
###return the average of the ages of the students
sum = 0
for i in students:
    print(i["age"])
    sum += i["age"]
print(sum)
average = sum/(len(students))
print(average)'''

'''
##Create a dictionary with subject and list of the students
DictSubject = {}
for student in students:
    name = student["name"]
    subjects = student["subjects"]
    for subject in subjects:
        if subject in DictSubject:
            DictSubject[subject].append(name)
        else:
            DictSubject[subject] = [name]
print(DictSubject)'''

'''##create a list of all students names
Student_Names = []
for student in students:
    names = student["name"]

    # if names not in Student_Names:
    Student_Names.append(names)

print(Student_Names)
'''

'''
Find the student(s) with the highest score if each student has a "score" key in their dictionary.
Sort the students' names in alphabetical order.
'''
'''###Create a set of unique ages of all the students.
ageList = []
for i in students:
    age = i['age']
    if age not in ageList:
        ageList.append(age)
print(ageList)
'''
'''###Calculate the total number of subjects across all students.
subjectList = []
count = 0
for student in students:
    subject = student['subjects']
    for each in subject:
        if each not in subjectList:
            subjectList.append(each)
            count+=1
print(count)
print(subjectList)'''

'''###Create a dictionary where the keys are the roll numbers and the values are the corresponding student names.
RollNameDict = {}
for student in students:
    name = student["name"]
    roll_number = student["roll_number"]
    RollNameDict[roll_number] = name
print(RollNameDict)'''

'''###Create a list of tuples where each tuple contains the student's name, age, and subjects.
ListOfTuple = []
for student in students:
    name = student["name"]
    age = student["age"]
    subjects = student["subjects"]
    yourtuple = (name,age,subjects)
    ListOfTuple.append(yourtuple)
print(ListOfTuple)'''

'''##Calculate the average score of all the students if each student has a "score" key in their dictionary.
sum_score = 0
for student in students:
    score = student["score"]
    sum_score += score
average_score = sum_score/(len(students))
print(f"The total score is : {sum_score}")
print(f"The average score is : {average_score}")
'''
'''## Check if there is any student with the name "John" in the list.
count = 0
for student in students:
    name = student["name"]
    if "John" in name:
        count+=1
print("There are ",count," record of the student belonging to John")'''

'''#Create a dictionary where the keys are the subjects and the values are the total name of students studying each subject.
subjectStudentDict = {}
for student in students:
    name = student['name']
    subjects = student["subjects"]
    for subject in subjects:
        if subject not in subjectStudentDict:
            subjectStudentDict[subject] = [name]
        else:
            subjectStudentDict[subject].append(name)
print(subjectStudentDict)


#Create a dictionary where the keys are the subjects and the values are the total number of students studying each subject.
subjectStudentDict = {}
for student in students:
    name = student['name']
    subjects = student["subjects"]
    count = 0
    for subject in subjects:
        if subject not in subjectStudentDict:
            subjectStudentDict[subject] = 1
        else:
            subjectStudentDict[subject] += 1
print(subjectStudentDict)
'''

'''
Calculate the average age of all the students.
Create a dictionary where the keys are the subjects, and the values are the list of students who are studying that subject.'''

'''##Create a set of unique subjects from all the students.
studentsset = set()
studentlist = []
for student in students:
    name = student['name']
    studentsset.add(name)
    if student not in studentlist:
        studentlist.append(name)
print(studentsset,studentlist)'''

'''##Create a list of tuples where each tuple contains the student's name and their roll number.
Listoftuple = []
for student in students:
    name = student['name']
    roll_number = student['roll_number']
    namerolltuple = (name,roll_number)
    Listoftuple.append(namerolltuple)
print(Listoftuple)'''


'''students = [('Alice', 95), ('Bob', 80), ('Charlie', 90)]
# students.sort(key = lambda x : x[1])
# print(students)

# print(students[0][1])
for i in range(len(students)):
    for j in range(i+1, len(students)):
        if students[i][1] > students[j][1]:
            students[i],students[j] = students[j],students[i]
        else:
            students[i],students[j] = students[i],students[j]
print(students)'''


'''## factorial program 
def fact(n):
    if n == 0 or n == 1:
        factorial = 1
    else:
        factorial = n * fact(n-1)
    return factorial
print(fact(5))

### fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
number = int(input("Enter the number:"))

for i in range(number):
    print(fibonacci(i),end = " ")
'''

