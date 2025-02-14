# Inheritance

## Single-Level Inheritance
class Father1:
    def __init__(self):
        print('\nConstructor of Father called.')

    def income(self):
        print("Father's income'!")

class Son1(Father1):
    def sleep(self):
        print('Son is sleeping')

print('\n--------------------Single-level Inheritance--------------------')   
f1 = Father1() # Call its own constructor
f1.income()

s1 = Son1() # It will also call constructor of Father
s1.sleep()
s1.income()

## Multi-Level Inheritance
class Grandfather2:
    def __init__(self, source = 'Grandfather'):
        print(f'\nConstructor of Grandfather called from {source}')

    def property(self):
        print("Grandfather's property!")

class Father2(Grandfather2):
    def __init__(self, source = 'Father'):
        print(f'\nConstructor of Father called from {source}')

    def income(self):
        print("Father's income'!")

class Son2(Father2):
    def __init__(self):
        super().__init__('Son')
        print('\nConstructor of son called.')

    def sleep(self):
        print('Son is sleeping')

print('\n--------------------Multi-level Inheritance--------------------')   
g1 = Grandfather2() # Call its own constructor
g1.property()
  
f1 = Father2() # Call its own constructor
f1.income()
f1.property()

s1 = Son2() # Call its own constructor as well as Father's
s1.sleep()
s1.income()
s1.property()

## Multiple Inheritance
class Father3:
    def __init__(self, source = 'Father'):
        print(f'\nConstructor of Father called from {source}')

    def income(self):
        print("Father's income!")

class Mother3:
    def __init__(self, source = 'Mother'):
        print(f'\nConstructor of Mother called from {source}')

    def meal(self):
        print("Mother's food!")

class Son3(Father3, Mother3):
    def __init__(self):
        super().__init__('Son')
        print('\nConstructor of Son called.')

    def sleep(self):
        print('Son is sleeping')

print('\n--------------------Multiple Inheritance--------------------')   
f1 = Father3()  # Call its own constructor
f1.income()

m1 = Mother3()  # Call its own constructor
m1.meal()

s1 = Son3()  # Call its own constructor as well as Father's due to MRO
s1.sleep()
s1.income()
s1.meal()