# Pylint
''' A Linter is dev tool used to improve code quality. 
Pylint is one such tool. There are many linter available in the market.
Some of them are Pylint, flake8, mypy, and more. 
Lint can be a logical or stylistic error in our code, just like we have
on our clothes.'''

# Below code has Pylint Rating of 1.43
# class car:
#     def __init__(self, color):
#         self.color = color

# my_car = car('blue')

# def   crash(car1, car2):
#     car1.color = 'burnt'

# crash(car('red'), my_car)

# Below code has Pylint Rating of 10.0
class Car:
    ''' This is a docstring to improve code quality'''
    def __init__(self, color):
        ''' Initializes the car object'''
        self.color = color
        self.speed = 0

    def drive(self):
        ''' Starts the car and gets speed of 20'''
        self.speed = 20

    def stop(self):
        ''' Stops the car and speed become 0'''
        self.speed = 0

my_car = Car('blue')

def crash(car1, car2): #pylint: disable=unused-argument # <- This will suppress the lint error
    ''' Crashes the car'''
    car1.color = 'burnt'

crash(Car('red'), my_car)
