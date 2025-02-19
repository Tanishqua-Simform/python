# Abstraction

## Abstract Classes and Abstract Methods
''' Abstract classes should have atleast 1 abstract method.
It is used when we need to force the classes to implement certain functionalities.'''

from abc import ABC, abstractmethod

print('\n-------------------------------Abstract Classes----------------------')
class Device(ABC):
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def configuration(self):
        pass

class Laptop(Device):
    def process(self):
        print('OS is running inside Laptop')
    
    def configuration(self):
        self.os = 'Windows'
        self.core = 'Intel i5'
        self.ram = 16
        self.camera = True
        print('OS - ', self.os, '\nCore - ', self.core, '\nRam - ', self.ram, '\nWith Camera - ', self.camera)

    def __str__(self):
        return 'Laptop'

class Desktop(Device):
    def process(self):
        print('OS is running inside Desktop')

    def configuration(self):
        self.os = 'Ubuntu'
        self.core = 'Ryzen 3'
        self.ram = 8
        self.camera = False
        print('OS - ', self.os, '\nCore - ', self.core, '\nRam - ', self.ram, '\nWith Camera - ', self.camera)

    def __str__(self):
        return 'Desktop'

class Developer:
    def working(self, device):
        print(f'\nI am developing code using {device}')
        device.process()
        print(f'\n--------------------{device}-------------------')
        print(f'\nThe configuration of my {device} is -')
        device.configuration()

Tanishqua = Developer()
Dell = Laptop()
LG = Desktop()

Tanishqua.working(Dell)
Tanishqua.working(LG)
