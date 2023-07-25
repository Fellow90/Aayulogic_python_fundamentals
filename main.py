'''##Type annotation in python
def yourfunc(a : str, b: int) -> str:
    return (f"Hi! Mi name is {a} and I am {b} years old.")

print(yourfunc("Avishek",23))'''


'''#### Walrus operator perform computation and condition check simultaneously and later on store it in variable
numbers = [1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = [i*i for i in numbers if i*i < 10]
# print(squaredNumbers)
squaredNumbers_walrusOperator = [square for i in numbers if (square := i * i) > 10]
print(squaredNumbers_walrusOperator)'''





