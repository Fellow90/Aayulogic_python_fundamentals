# import itertools

'''## count as itertools
result = itertools.count(step= 3)
for number in range(10):
    print(next(result))'''

'''
###cycle in itertools
mylist = [1,2,3]
result = itertools.cycle(mylist)
for i in range(10):
    print(next(result))'''


## repeat in itertools
'''result = itertools.repeat('abc', times= 3)
for i in result:
    print(i)


result = itertools.repeat('abc')
for i in range(3):
    print(next(result))
'''



'''## chain
list1 = [1,2,3,4]
list2 = ('a','b','c','d','e')
result = itertools.chain(list1, list2)
for i in result:
    print(i)'''

'''#compress
list1 = [1,2,3,4]
list2 = [0,0,1,1]
result = list(itertools.compress(list1, list2))
print(result)'''

'''
### dropwhile
onelist = [1,2,6,8,3,7,0,1]
onelist.sort()
for i in onelist:
    print(i, end= " ")
dropwhilelilst = list(itertools.dropwhile(lambda x : x < 5,onelist))
print(dropwhilelilst)
'''