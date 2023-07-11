'''
#List comprehension
yournum = [1,2,4,7,9,2,6,8]
sqnum = [x*x for x in yournum]
print(sqnum)'''

'''
#map and filter syntax as map(function,iterable) or filter(function,iterable)
def halfsquare(n):
    return (n**2)/2

numbers = [1,3,5,7,9,23,67,90,15,78]

halfsquareobject = map(halfsquare,numbers)
halfsquarelist = list(map(halfsquare,numbers))
print(halfsquareobject)
print(halfsquarelist)


def filtereven(n):
    if n%2 == 0:
        return n
filteredhalfsquare = filter(filtereven, halfsquarelist)
filteredhalfsquarelist= list(filter(filtereven, halfsquarelist))

print(filteredhalfsquare)
print(filteredhalfsquarelist)'''
'''
#print whose name starts with A   
names = ['Alice', 'Bob', 'Anna', 'Andrew', 'Alex', 'Ben']
# def filtername(name):
#     if name.startswith('A'):
#         return name
    
# namestartwithA = list(filter(filtername, names))

namestartwithA = list(filter(lambda name:name.startswith('A'),names))

print(namestartwithA)'''

'''pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sortedPair = sorted(pairs, key = lambda pair:pair[1])
print(sortedPair)
'''



'''
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key = lambda pair:pair[1])
print(pairs)
'''


'''def sortpair(okay):
    for i in range(len(okay)):
        for j in range(i+1,len(okay)):
            if okay[i][1]>okay[j][1]:
                okay[i],okay[j] = okay[j], okay[i]
    return okay
                
pairs = [(1, 11), (2, 22), (3, 12), (4, 5)]

print(sortpair(pairs))'''

'''pairs = [(1, 11), (2, 22), (3, 12), (4, 5)]

def sort_pair(pairs):
    for i in range(len(pairs)):
        min_idx = i
        for j in range(i + 1, len(pairs)):
            if pairs[j][1] < pairs[min_idx][1]:
                min_idx = j
        pairs[i], pairs[min_idx] = pairs[min_idx], pairs[i]
print(sort_pair(pairs))'''





        
    


