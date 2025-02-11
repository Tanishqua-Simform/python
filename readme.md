# Python

As of now, we have gained in-depth knowledge of databases and front-end, now it is time to learn the magic that happens at the Back. This is going to be an interesting ride for sure!

##### Dt. 11 Feb, 2025.

I will jump to classes and objects today as I am aquainted with python syntax. Although I will cover the basics later so stay tuned!

I watched [Python OOP - Corey Schaffer](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) playlist. The summary is as follow -

## Class and Objects

- A class is a blueprint for creating objects. It defines attributes (data) and methods (behavior).
- An object is an instance of a class that has its own unique values for the defined attributes.
- Python classes are created using the `class` keyword and can include methods and properties.

##### Classes and Instances

- A class defines a structure, but it does not allocate memory until an object is instantiated.
- Instance: Each object created from a class is an instance with unique data.
- Example:

  ```python
  class Car:
      def __init__(self, brand):
          self.brand = brand

  my_car = Car("Toyota")  # Instance of Car class
  ```

##### Class Variables vs Instance Variables

- Class variables are shared across all instances of a class.
- Instance variables are unique to each object and defined inside the constructor (`__init__`).
- Example:

  ```python
  class Example:
      class_var = "Shared Variable"  # Class variable

      def __init__(self, value):
          self.instance_var = value  # Instance variable
  ```

- The `__dict__` attribute is a dictionary that stores an object's attributes.
- Example:

  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

  p = Person("Alice", 30)
  print(p.__dict__)  # {'name': 'Alice', 'age': 30}
  ```

##### Class Methods vs Static Methods

- Class methods:

  - Defined using `@classmethod`.
  - Take `cls` as the first parameter, allowing access to class variables.
  - Example:

    ```python
    class Example:
        var = "Class Variable"

        @classmethod
        def show(cls):
            return cls.var
    ```

- Static methods:
  - Defined using `@staticmethod`.
  - Do not take `self` or `cls`.
  - Example:
    ```python
    class Math:
        @staticmethod
        def add(x, y):
            return x + y
    ```

##### Inheritance and Subclasses

- Inheritance allows a child class to inherit attributes and methods from a parent class.
- `isinstance(obj, Class)`: Checks if `obj` is an instance of `Class` or its subclass.
- `issubclass(SubClass, ParentClass)`: Checks if `SubClass` is derived from `ParentClass`.
- Example:

  ```python
  class Parent:
      pass
  class Child(Parent):
      pass

  print(issubclass(Child, Parent))  # True
  ```

##### Dunder Methods

- Dunder (double underscore) methods customize object behavior.
- Common methods:
  - `__init__`: Initializes an instance.
  - `__repr__`: Returns an official string representation.
  - `__str__`: Returns a user-friendly string.
  - `__add__`: Enables `+` operator overloading.
  - `__len__`: Allows an object to be used with `len()`.
- Example:

  ```python
  class Example:
      def __init__(self, value):
          self.value = value

      def __str__(self):
          return f"Value: {self.value}"

  obj = Example(10)
  print(str(obj))  # Value: 10
  ```

##### Property Decorators

- The `@property` decorator turns a method into a getter.
- `@methodname.setter` allows setting a property.
- `@methodname.deleter` allows deleting a property.
- Example:

  ```python
  class Person:
      def __init__(self, name):
          self._name = name

      @property
      def name(self):
          return self._name

      @name.setter
      def name(self, value):
          self._name = value

  p = Person("John")
  print(p.name)  # Access as an attribute
  ```

I felt like revising SQL queries so for the rest of the day I did that. [Check it out.](https://github.com/Tanishqua-Simform/database?tab=readme-ov-file#dt-11-feb-2025-extra-day)

Calling it a day now! We'll cover Python basics tomorrow.
