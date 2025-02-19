# Collections 
'''Collections - It is a conatiner used to store data.
List, Tuple, Set and Dictionary are collections in Python.
Collections Module - Specialised collection data structures.
They are - 
-> namedtuple() - A tuple with named values
-> chainmap() - A dict combined of multiple dicts
-> deque() - list-like container with fast appends and pops on either end
-> counter() - Dict subclass to count hashable objects (simply - Frequency Map)
-> OrderedDict() - Dict that remembers the order in which entries made
-> defaultdict() - Dict subclass that supplies default values for missing keys
-> userdict() - Wrapper around Dict() for creating sub classes
-> userList() - Wrapper around List() for creatinf sub classes
-> UserString() - Wrapper around Str() for creating sub classes
'''

## NamedTuple()
print('\n---------------------NamedTuple---------------------------\n')
from collections import namedtuple
course = namedtuple('Course', 'Name, Faculty, Marks')
dbms = course('DBMS', 'Nakul', 85)
os = course('OS', 'Avani', 89)
web = course('Web', 'Jashvant', 82)
print(dbms)
print('Faculty of OS - ', os.Faculty)
print('Marks of Web - ', web.Marks)

## Deque()
print('\n---------------------Deque---------------------------\n')
from collections import deque
name = [1, 2, 3, 4]
d_name = deque(name)
print(d_name)
d_name.append('End')
print(d_name)
d_name.appendleft('Start')
print(d_name)
d_name.pop()
print(d_name)
d_name.popleft()
print(d_name)
d_name.extendleft([8,7,6]) # Appends at left in reverse order
print(d_name)
d_name.rotate(2)
print(d_name)

## Chainmap()
print('\n---------------------Chainmap---------------------------\n')
from collections import ChainMap
consonants = {1: 'b', 2: 'c', 3: 'd', 4: 'f', 5: 'g'}
vowels = {1: 'a', 2: 'e', 3:'i', 4: 'o', 5: 'u'}
alphabets = ChainMap(consonants, vowels)
print(alphabets)

## Counter()
print('\n---------------------Counter---------------------------\n')
from collections import Counter
nums = [1, 1, 2, 3, 2, 3, 5, 4, 6, 4, 3, 2, 3, 3, 2, 4, 1, 1, 2]
freq_map = Counter(nums)
print(freq_map)
print('elements() method - ', list(freq_map.elements()))
print('most_common() method - ', freq_map.most_common())
sub = {2:1, 6:1}
freq_map.subtract(sub)
print('After subtract() method - ', freq_map.most_common())
print('Most common number is - ', freq_map.most_common()[0][0])

## OrderedDict()
''' There is no significant diff in dict and orderedDict after python 3.7'''
print('\n---------------------OrderedDict---------------------------\n')
from collections import OrderedDict
word = OrderedDict()
word[1] = 'T'
word[2] = 'e'
word[3] = 's'
word[4] = 't'
print(word)
print(word.values())
word[1] = 'R'
print(word.values())

## defaultdict()
print('\n---------------------defaultdict---------------------------\n')
from collections import defaultdict
# family = defaultdict(int) 
family = defaultdict(lambda: 'Nope') # Gives the default value of 'Nope' to non-members
family[1] = 'Meetu'
family[2] = 'Lamha'
family[3] = 'Rajesh'
print(family.items())
print('Is there a 4th member in family ? -', family[4])
