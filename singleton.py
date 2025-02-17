# Singleton - A Design Pattern
''' When we need to create a single instance of a class we use Singleton.
It shares the global state of our code. Although this can also be done using modules in python. 
[SEARCH UP FOR MORE INFO]
NoneType is a singleton class. '''

## Method 1 - Singleton Class
print('\n-------------------SINGLETON USING CLASS-----------------\n')
class MySingleton(object):
    ''' Singleton class to increment user count, everytime a new user 
    is created on our application.'''
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.users = 0
        return self._instance
    
    def addUsers(self):
        self.users += 1

myApp = MySingleton()
print('Users just after myApp created :', myApp.users)
for i in range(10):
    myApp.addUsers()
print('User count after some employees created :', myApp.users)

### Interesting Notes - 
print('\nAre users sharing single instance ? -', myApp.users is MySingleton().users)
print('Is MySigleton.users and myApp.users same ? -', myApp.users is MySingleton.users)

## Method 2 - Singleton Decorator
print('\n-------------------SINGLETON DECORATORS-----------------\n')
def singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@singleton
class Phonebook(object):
    ''' Singleton class to create a global directory of numbers. Add and 
    retrieve information using functions.'''
    _directory = dict()

    def add(self, name, number):
        self._directory[name] = number
        return 'Number added!'
    
    def get(self, name):
        return self._directory[name]

pb1 = Phonebook()
pb1.add('Tanishqua', 123456789)
pb1.add('Lamha', 234567891)
pb2 = Phonebook()
pb2.add('Meetu', 345678912)
pb2.add('Rajesh', 456789123)

print('Finding Meetu in 1st instance - ', pb1.get('Meetu'))
print('Finding Lamha in 2nd instance - ', pb2.get('Lamha'))
print('\npb1 is pb2 ? -', pb1 is pb2)
print('\nSo, it is clear that Singleton creates 1 instance and always references to it!')

