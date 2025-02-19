# Iterator
''' In python we have iterables and iterators. 
We can traverse through a iterable using iterator object.
Iterables have dunder iter methods, which make a new iterator object 
of that iterable.
Iterators have dunder next method, which is used to get the next value 
of iterator object. '''

## For loops 
'''They create iterator of iterables (by calling __iter__()) and then uses dunder next 
method everytime. next method raises StopIteration exception which 
for loop handles on its own. '''

### Implementation of For loop using while
print('\n---------------------Mimicing For Loop---------------------------\n')
nums = [1, 2, 3] # List -> Iterable
i_nums = iter(nums) # Object -> Iterator

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

## Creating Our Own Iterable Class
''' A class is called Iterable, if it has dunder iter() method.
A class is called Iterator, if it has dunder next() method. '''

### Implementation of List using iter and next
print('\n---------------------Custom Iterable Class---------------------------\n')
class MyList:
    def __init__(self, items):
        self.items = items
        self.next = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next == len(self.items):
            raise StopIteration
        current = self.items[self.next]
        self.next += 1
        return current

animals = MyList(['dog', 'cat', 'lion', 'tiger', 'fox'])
print(animals)
for _ in range(5): # 5 is the length of animals. 
    print(next(animals))

# Generator
print('\n---------------------Custom Generator---------------------------\n')
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(4, 20)
print(nums)
for _ in range(5):
    print(next(nums))

## Problem by Corey Schafer - Create Sentence class and loop through words in it.
print('\n---------------------Sentence Iterable Class---------------------------\n')
class Sentence():
    def __init__(self, string):
        self.string = string
        self.words = self.string.split()
        self.next = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next == len(self.words):
            raise StopIteration
        word = self.words[self.next]
        self.next += 1
        return word

my_sentence_iterator = Sentence('This is a test')

for word in my_sentence_iterator:
    print(word)

## Same Problem with Generator
print('\n---------------------Sentence Generator---------------------------\n')
def sentence(string):
    words = string.split()
    current = 0
    while current < len(words):
        word = words[current]
        yield word
        current += 1

# ### Simpler code for generator by Corey Schafer -
# def sentence(string):
#     for word in string.split():
#         yield word

my_sentence_generator = sentence('This is a test')

for word in my_sentence_generator:
    print(word)