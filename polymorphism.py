# Polymorphism

## Duck Typing
print('\n----------------------------Duck Typing--------------------------------\n')
class Animal:
    def live(self):
        print('Animals live on oxygen, food and water. They can walk.')
    
class Fish:
    def live(self):
        print('Fishes live on oxygen and food. They can swim.')
    
class Tree:
    def live(self):
        print("Tree live on Sunlight and CO2. They can't walk or swim.")

def livingThings(entity):
    entity.live()

livingThings(Tree())
livingThings(Animal())
livingThings(Fish())


## Operator Overloading
print('\n--------------------------Operator Overloading--------------------------\n')
class Food:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def __add__(self, other):
        items = self.item + ' te ' + other.item
        quantity = self.quantity + other.quantity
        meal = Food(items, quantity)
        return meal
    
    def __gt__(self, other):
        return self.quantity > other.quantity 
    
    def __str__(self):
        return self.item 

roti = Food('Makaai di Roti', 10)
sabzi = Food('Sarso da Saag', 3)
meal = roti + sabzi
print(roti)
print(sabzi)
print(meal)

more, less = (roti, sabzi) if (roti > sabzi) else (sabzi, roti) 
print(f'\n{more} zyada hegi {less} de karta!')


## Method Overloading
''' In Python there isn't Method Overloading but it can be achieved using *args as parameter'''
print('\n--------------------------Method Overloading--------------------------\n')
class Calculator:
    # Below functions won't work in Python
    # def sum(self, a, b):
    #     return a + b
    # def sum(self, a, b, c):
    #     return a + b + c

    # To overcome this and still implement feature similar to overloading
    def sum(self, *nums):
        total = 0
        for num in nums:
            total += num
        return total
    

c1 = Calculator()

print('Sum of 2 and 5 is - ', c1.sum(2,5))
print('Sum of 10, 12, 34 is - ', c1.sum(10, 12, 34))
print('Sum of 1, 2, 3, 4, 5, 6, 100 is - ', c1.sum(1, 2, 3, 4, 5, 6, 100))


## Method Overriding
print('\n--------------------------Method Overriding--------------------------\n')
class Shape:
    def draw(self):
        print('Drawing a SHAPE !!!')
    
class Triangle(Shape):
    def draw(self):
        print('Drawing a TRIANGLE !!!')

class Circle(Shape):
    def draw(self):
        print('Drawing a CIRCLE !!!')

print('Shape().draw() -> ', end='')
Shape().draw()
print('Triangle().draw() -> ', end='')
Triangle().draw()
print('Circle().draw() -> ', end='')
Circle().draw()