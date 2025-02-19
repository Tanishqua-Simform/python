# Decorator

## For function without arguments
print('\n----------------Decorator for Function without Arguments------------------')
def decorator_function(original_function):
    def wrapper_function():
        print('\nInside Wrapper')
        original_function()
        original_function()
        original_function()
        return
    return wrapper_function

### Method 1 - To wrap function with a decorator
def display_name():
    print('Hello! My name is Tanishqua!')

display_name = decorator_function(display_name)
display_name()

### Method 2 - Using @decorator
@decorator_function
def display_age():
    print('I am 21 years old!')

display_age()

#### Note - The above code won't work for functions taking arguments.

## For function with arguments
print('\n-----------------Decorator For Function with Arguments--------------------\n')
def decorator_function1(original_function):
    def wrapper_function1(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function1

@decorator_function1
def sum2(a, b):
    print(f'{a} + {b} is :', a + b)

@decorator_function1
def sum3(a, b, c):
    print(f'{a} * {b} * {c} is :', a + b + c)

sum2(10, 20)
sum3(1, 2, 3)

## For classes
print('\n---------------------------Decorator Classes-------------------------------\n')
class DecoratorClass(object):
    # Acts like decorator function
    def __init__(self, original_function):
        self.original_function = original_function
    
    # Acts like wrapper function
    def __call__(self, *args, **kwargs):
        return self.original_function(*args, **kwargs)

@DecoratorClass
def product(a, b, c):
    print(f'{a} * {b} * {c} is :', a * b * c)

product(10, 2, 3)

## Practical Examples
''' Decorators can be used to add logging as well as timing functionalities to multiple functions at once.
Code becomes error-prone and tedious to handle, if we implement same functionality over multiple functions. 
So to overcome this problem we use decorators.'''
print('\n---------------------Practical Example with Timer---------------------------\n')
def timer(orig_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} secs.'.format(t2))
        return result

    return wrapper

@timer
def countWithTime(n):
    total = 0
    print('Count for {} ran in :'.format(n), end = '')
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += 1
    return total

countWithTime(300)
countWithTime(400)

## Stacking multiple decorators
print('\n---------------------Multiple Decorators Stacking---------------------------\n')
from functools import wraps

def logger(orig_function):
    import logging
    logging.basicConfig(filename='File manipulation/{}.log'.format(orig_function.__name__), level = logging.INFO)

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return orig_function(*args, **kwargs)
    
    return wrapper

def timer1(orig_function):
    import time

    @wraps(orig_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} secs.'.format(t2))
        return result

    return wrapper

@logger
@timer1
def countWithLogAndTime(n):
    total = 0
    print('countWithLogAndTime() for {} ran in - '.format(n), end = '')
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += 1
    return total

countWithLogAndTime(100)
countWithLogAndTime(200)
countWithLogAndTime(300)
countWithLogAndTime(400)


## Decorators with arguments
''' When using Flask or similar framework we will come across decorators which take arguments.
To implement this we need to nest our decorator 1 layer deeper.'''
print('\n---------------------Decorator with Arguments---------------------------\n')
def prefix_decorator(prefix):
    def decorator(original_func):
        def wrapper(*args, **kwargs):
            print('Inside the wrapper for - ', prefix)
            return original_func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_decorator('Sub Function')
def sub(a, b):
    print(f'{a} - {b} is :', a - b)

@prefix_decorator('Mod Function')
def mod(a, b):
    print(f'{a} % {b} is :', a % b)

sub(10, 5)
mod(256, 11)