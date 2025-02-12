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

##### Dt. 12 Feb, 2025.

Let's begin with the basics of python. I will be refering [Python - TutorialsPoint](https://www.tutorialspoint.com/python/index.htm) website to get deeper understanding of core concepts of Python.

## Python basics

#### What is Python ?

Python is a very popular general-purpose interpreted, interactive, object-oriented, and high-level programming language. Python is dynamically-typed and garbage-collected programming language.

##### Python vs C++ Comparison

| Criteria           | Python                                        | C++                                    |
| ------------------ | --------------------------------------------- | -------------------------------------- |
| Execution          | Interpreted-based, executed by an interpreter | Compiler-based, compiled by a compiler |
| Typing             | Dynamic-typed                                 | Static-typed                           |
| Portability        | Highly portable                               | Not portable without changes           |
| Garbage Collection | Automatic memory management                   | Manual memory management               |
| Syntax             | Easy to read, write, and understand           | Tedious syntax                         |
| Performance        | Slower execution                              | Faster execution                       |
| Application Areas  | Machine learning, web applications            | Embedded systems, device drivers       |

#### Interpreter

- The Python interpreter executes Python code line by line.
- It converts source code into machine code at runtime.
- Supports interactive mode where commands can be executed one at a time.
- Can be run as a script by executing `.py` files.
- Different implementations include CPython, PyPy, and Jython.

#### Virtual Environment

- A virtual environment is an isolated workspace for Python projects.
- It allows managing dependencies separately for different projects.
- Created using `venv` module: `python -m venv myenv`.
- Activated using `source myenv/bin/activate` (Linux/macOS) or `myenv\Scripts\activate` (Windows).
- Deactivated using `deactivate` command.

#### Identifiers

- Identifiers are names used for variables, functions, and classes.
- Must start with a letter (A-Z or a-z) or an underscore (\_) followed by letters, digits, or underscores.
- Cannot be a Python keyword (e.g., `if`, `class`, `return`).
- Case-sensitive (`Var` and `var` are different identifiers).

#### Variables

- Variables store data values and are dynamically typed in Python.
- Assigned using `=` operator: `x = 10`.
- No need for explicit declaration before use.
- Can reference different types during execution: `x = 10` then `x = "hello"`.
- Multiple assignments are possible: `a, b, c = 1, 2, 3`.

#### Memory of Variables and id()

- Each variable in Python is an object stored in memory.
- The `id()` function returns the memory address of an object.
- Example:
  ```python
  x = 5
  print(id(x))
  y = 5
  print(id(y))  # Same as x because integers are immutable
  ```
- Mutable objects like lists have different `id()` values after modification.

#### Data Types

- Python has several built-in data types:
  - Numeric: `int`, `float`, `complex`
  - Sequence: `list`, `tuple`, `range`
  - Text: `str`
  - Set: `set`, `frozenset`
  - Mapping: `dict`
  - Boolean: `bool`
  - Binary: `bytes`, `bytearray`, `memoryview`
- Use `type()` to check the data type: `type(10) # int`.

#### Type Casting

- Converting one data type to another.
- `int()`, `float()`, `str()`, `list()`, etc.
- Example:
  ```python
  x = "10"
  y = int(x)  # Converts string to integer
  ```

#### Unicode System

- Python uses Unicode for character representation.
- Unicode supports multiple languages and symbols.
- Example:
  ```python
  print("\u20B9")  # Prints ₹ symbol
  ```

#### Literals

- Fixed values assigned to variables.
- Types: String, Numeric, Boolean, Special (`None`).
- Example: `x = 42`, `y = "Hello"`.

#### Operators

- Operators perform operations on variables and values.

##### Arithmetic Operators

- `+`, `-`, `*`, `/`, `//`, `%`, `**` (addition, subtraction, multiplication, etc.)

##### Comparison Operators

- `==`, `!=`, `>`, `<`, `>=`, `<=` (compare values)

##### Assignment Operators

- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=` (assign and update values)

##### Logical Operators

- `and`, `or`, `not` (combine boolean expressions)

##### Bitwise Operators

- `&`, `|`, `^`, `~`, `<<`, `>>` (bitwise operations on integers)

##### Membership Operators

- `in`, `not in` (check if value exists in sequence)

##### Identity Operators

- `is`, `is not` (compare memory locations)

##### Operator Precedence

- Determines execution order.
- Example: `*` has higher precedence than `+`.
- Use parentheses `()` to override default precedence.

#### Comments

- Used to explain code.
- Single-line: `# This is a comment`
- Multi-line: `""" This is a multiline comment """`

#### User Input

- `input()` function takes user input as a string.
- Example:
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```

#### Numbers

- Includes `int`, `float`, and `complex` types.
- Example:
  ```python
  a = 10  # int
  b = 10.5  # float
  c = 3+4j  # complex
  ```

#### Booleans

- Boolean values are `True` and `False`.
- Example:
  ```python
  x = True
  y = False
  print(x and y)  # False
  ```

## Control Statements

#### Control Flow

- Defines the order in which statements are executed.
- Controlled using loops and conditional statements.

#### Decision Making

- Allows execution of different code blocks based on conditions.
- Uses `if`, `if-else`, `elif`, and `match-case` statements.

#### If Statement

- Executes a block of code if a condition is `True`.
- Example:
  ```python
  x = 10
  if x > 5:
      print("x is greater than 5")
  ```

#### If-Else

- Executes one block if the condition is `True`, otherwise executes another block.
- Example:
  ```python
  if x > 5:
      print("x is greater than 5")
  else:
      print("x is 5 or less")
  ```

#### Nested If

- An `if` statement inside another `if` statement.
- Example:
  ```python
  if x > 5:
      if x < 20:
          print("x is between 5 and 20")
  ```

#### Match-Case Statement

- Python’s version of a `switch-case`.
- Example:
  ```python
  match x:
      case 1:
          print("One")
      case 2:
          print("Two")
      case _:
          print("Other")
  ```

#### Loops

- Used for executing a block of code multiple times.

#### For Loops

- Iterates over a sequence (list, tuple, string, range, etc.).
- Example:
  ```python
  for i in range(5):
      print(i)
  ```

#### For-Else Loops

- Executes the `else` block if the loop completes normally without `break`.
- Example:
  ```python
  for i in range(3):
      print(i)
  else:
      print("Loop finished")
  ```

#### While Loops

- Repeats as long as the condition is `True`.
- Example:
  ```python
  x = 5
  while x > 0:
      print(x)
      x -= 1
  ```

#### Break Statement

- Exits the loop prematurely.
- Example:
  ```python
  for i in range(5):
      if i == 3:
          break
      print(i)
  ```

#### Continue Statement

- Skips the rest of the code in the loop and proceeds to the next iteration.
- Example:
  ```python
  for i in range(5):
      if i == 3:
          continue
      print(i)
  ```

#### Pass Statement

- Placeholder that does nothing.
- Ellipse(...) ccan also be used as placeholder
- Example:
  ```python
  if x > 0:
      pass
  ```

#### Nested Loops

- A loop inside another loop.
- Example:
  ```python
  for i in range(3):
      for j in range(2):
          print(i, j)
  ```

## Strings

- A sequence of characters enclosed in quotes.
- Example:
  ```python
  s = "Hello, World!"
  ```

#### Slicing Strings

- Extracts substrings using indices.
- Example:
  ```python
  print(s[0:5])  # Output: Hello
  ```

#### Modify Strings

- Use built-in methods like `lower()`, `upper()`, `strip()`, `replace()`, etc.
- Example:
  ```python
  print(s.lower())
  ```

#### String Concatenation

- Joining strings using `+` operator.
- Example:
  ```python
  name = "Alice"
  greeting = "Hello, " + name
  ```

#### String Formatting

- Formatting strings using f-strings or `format()`.
- Example:
  ```python
  age = 25
  print(f"I am {age} years old")
  ```

#### Escape Characters

- Special characters like `\n` (newline) and `\t` (tab).
- Example:
  ```python
  print("Hello\nWorld")
  ```

## Lists

#### Access List Items

- Use indexing to access elements.
- Example:
  ```python
  lst = [1, 2, 3]
  print(lst[0])
  ```

#### Change List Items

- Modify elements by index.
- Example:
  ```python
  lst[1] = 10
  ```

#### Add List Items

- Use `append()`, `insert()`, or `extend()`.
- Example:
  ```python
  lst.append(4)
  ```

#### Remove List Items

- Use `remove()`, `pop()`, or `del`.
- Example:
  ```python
  lst.pop(1)
  ```

#### Loop Lists

- Iterate using `for` loop.
- Example:
  ```python
  for item in lst:
      print(item)
  ```

#### List Comprehension

- Compact syntax for creating lists.
- Example:
  ```python
  squares = [x**2 for x in range(5)]
  ```

#### Sort Lists

- Use `sort()` or `sorted()`.
- Example:
  ```python
  lst.sort()
  ```

#### Copy Lists

- Use `copy()` or slicing.
- Example:
  ```python
  new_list = lst.copy()
  ```

#### Join Lists

- Use `+` or `extend()`.
- Example:
  ```python
  combined = lst1 + lst2
  ```

### Points to Note -

- **Sets** can only store immutable objects (e.g., numbers, strings, tuples). Lists and dictionaries are not allowed.
- **Hashing** enables fast searching in memory. Only immutable objects are hashable.
- **Lists and tuples** store memory addresses of elements, not the elements themselves.
- **Docstrings** document modules, classes, functions, and methods using triple quotes (`'''` or `"""`).
- **Docstrings** can be accessed via `.__doc__` or `help()`.
- **For-Else** executes the `else` block only if the loop completes normally without `break`.

I also discovered new facts about memory allocation of literals and loop variables. You can look at it here - [basic.py](/basic.py) [Recommended]

See you tomorrow!
