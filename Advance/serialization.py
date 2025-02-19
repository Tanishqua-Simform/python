# Serialization and Desrialization
''' The process of converting state of an object to byte stream
is known as serialization. In python, it is called Pickling.

Alternative definition, The process of converting object in python-supported
form to file-supported form(Byte) or network-supported form(JSON/YAML)
The reverse process is called Deserialization/ Unpickling

Marshaling/Unmarshaling is for other languages
-> Pickle module for byte transform
-> json module for json transform
-> pyaml module for yaml transform'''

import pickle

class Student:
    def __init__(self, name):
        self.name = name

    def study(self, subject):
        self.subject = subject
    
    def display(self):
        print(f'{self.name} is studying {self.subject}')

# Serialization
print('\n---------------------Serialization---------------------------\n')
s1 = Student('Tanishqua')
s2 = Student('Soham')

s1.study('Python')
s2.study('DSA')
s1.study('ML')

with open('Pickle Files/s1.pkl', 'wb') as f:
    pickle.dump(s1, f)
print('Pickling of S1 Object Completed.')
    
with open('Pickle Files/s2.pkl', 'wb') as f:
    pickle.dump(s2, f)
print('Pickling of S2 Object Completed.')


# Deserialization
print('\n---------------------Deserialization---------------------------\n')
with open('Pickle Files/s1.pkl', 'rb') as f:
    stud1 = pickle.load(f)
print('\nUnpickling of S1 Object Completed.')
print('Student 1 - ')
stud1.display()
    
with open('Pickle Files/s2.pkl', 'rb') as f:
    stud2 = pickle.load(f)
print('\nUnpickling of S2 Object Completed.')
print('Student 2 - ')
stud2.display()

# Note - Pickle always requires class while deserialization.
# So import the class files inside the file where deserialization is performed.
# Use dill module instead.