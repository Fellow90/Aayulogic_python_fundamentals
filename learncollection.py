## counter is a container that stores the collection in a dictionary. It is a subclass of dictionary
'''from collections import Counter
yourlist = ['B','B','A','B','C','A','B',
               'B','A','C']

mycount = Counter(yourlist)
print(mycount)

'''#to be continued'''
'''
#ordered dict
firstDict = {}
firstDict['a'] = 1
firstDict['b'] = 2
firstDict['c'] = 3
firstDict['d'] = 4

for key, value in firstDict.items():
    print(key, value)
del firstDict['c']
del firstDict['a']


for key, value in firstDict.items():
    print(key, value)
'''
'''from collections import OrderedDict
secondDict = OrderedDict()

secondDict['a'] = 1
secondDict['b'] = 2
secondDict['c'] = 3
secondDict['d'] = 4


for key, value in secondDict.items():
    print(key, value)

del secondDict['c']
del secondDict['a']

for key, value in secondDict.items():
    print(key, value)
'''

### namedtuple as collections , it is a tuple class, callable with name.attributes. can be converted into dictionary later on

'''from collections import namedtuple

Person = namedtuple('Person',['name', 'age', 'city'])
person1 = Person('Nabin', 24, 'Kathmandu')
person2 = Person('Rupesh', 23, 'Pokhara')
person3 = ['Hari',33,'Butwal']
print(person1.name)
print(person2.city)

### can be converted into named tuple passed as an argument
print(Person._make(person3))
### can be converted into a regular dict

personx = person1._asdict()
print(personx)'''


'''## DefaultDict, subclass to dictionary, provides default value if the key doesnot have value, saves from causing keyerror
from collections import defaultdict
default_dictionary = defaultdict(int)
default_dictionary['student'] = 2
default_dictionary['teacher'] = 3
print(default_dictionary['student'],default_dictionary['teacher'],default_dictionary['staff'])

default_dictionary_list = defaultdict(list)
default_dictionary_list['college'].append('student')
default_dictionary_list['college'].append('teacher')
default_dictionary_list['college'].append('staff')

print(default_dictionary_list['college'])
print(default_dictionary_list['school'])'''

'''
### chainmap, encapsulates many dictionary into a single unit
from collections import ChainMap 
     
     
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1,d2,d3) ## dictionaries into a single unit

# print(c.keys())
# print(c.values())
# print(c['a'])

d4 = {'g':7}
new_c = c.new_child(d4) ## adds new child
print(new_c)'''

'''## deque , optimized list, double ended append pop
regular_list = [1,2,3,4,5,6,7,8,9,10]
from collections import deque
de = deque(regular_list)
de.appendleft(4)
print(de)
de.reverse()
## includes other list operation'''

'''###userdict, userlist and userstring

from collections import UserDict

class MyDictionary(UserDict):
    def __setitem__(self, key, value):
        # Custom logic before setting the item
        print(f"Setting {key} = {value}")
        # Call the parent class's __setitem__ to actually set the item
        super().__setitem__(key, value)

    ### CUSTOMIZING POP ITEM 
    def popitem(self) -> tuple:
        if not self.data:
            raise KeyError("popitem(): dictionary is empty")
        key, value = self.data.popitem()
        print(f"Popped item: {key} = {value}")
        return key, value

# Using the custom dictionary
my_dict = MyDictionary()
my_dict['apple'] = 3
my_dict['orange'] = 5

print(my_dict)
my_dict.pop('apple')
print(my_dict)
my_dict.popitem()
print(my_dict)
my_dict.popitem()
print(my_dict)

## userlist and userstring works in the same way'''