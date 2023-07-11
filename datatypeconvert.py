
def datatypeconverter(a):
    a = input("Which value of the key do you want to search for: ")
    a = int(input("Which value of the key do you want to search for: "))
    if a == str:
        return a
    else:
        return int(a)



a,b = datatypeconverter()
print(a,b)