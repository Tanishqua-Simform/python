# Calculator
''' This is a helper module for Unit Testing purposes.'''

def add(x, y):
    ''' Add Function '''
    return x + y

def subtract(x, y):
    ''' Subtract Function '''
    return x - y

def multiply(x, y):
    ''' Multiply Function '''
    return x * y

def divide(x, y):
    ''' Divide Function '''
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

# # This way we used to test our function 
# # But this is not good way.
# # Instead we will use unittest module.
# print(add(10, 5))
# print(subtract(10, 5))
# print(multiply(10, 5))
# print(divide(10, 5))
# print(divide(10, 0))