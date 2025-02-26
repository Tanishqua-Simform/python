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

  ```python
  class Car:
      def __init__(self, brand):
          self.brand = brand

  my_car = Car("Toyota")  # Instance of Car class
  ```

##### Class Variables vs Instance Variables

- Class variables are shared across all instances of a class.
- Instance variables are unique to each object and defined inside the constructor (`__init__`).

  ```python
  class Example:
      class_var = "Shared Variable"  # Class variable

      def __init__(self, value):
          self.instance_var = value  # Instance variable
  ```

- The `__dict__` attribute is a dictionary that stores an object's attributes.

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

  ```python
  class Parent:
      pass
  class Child(Parent):
      pass

  print(issubclass(Child, Parent))  # True
  ```

##### Dunder/Special/Magic Methods

- Dunder (double underscore) methods customize object behavior.
- Common methods:

  - `__init__`: Initializes an instance.
  - `__repr__`: Returns an official string representation.
  - `__str__`: Returns a user-friendly string.
  - `__add__`: Enables `+` operator overloading.
  - `__len__`: Allows an object to be used with `len()`.

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

  ```python
  x = "10"
  y = int(x)  # Converts string to integer
  ```

#### Unicode System

- Python uses Unicode for character representation.
- Unicode supports multiple languages and symbols.

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

  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```

#### Numbers

- Includes `int`, `float`, and `complex` types.

  ```python
  a = 10  # int
  b = 10.5  # float
  c = 3+4j  # complex
  ```

#### Booleans

- Boolean values are `True` and `False`.

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

  ```python
  x = 10
  if x > 5:
      print("x is greater than 5")
  ```

#### If-Else

- Executes one block if the condition is `True`, otherwise executes another block.

  ```python
  if x > 5:
      print("x is greater than 5")
  else:
      print("x is 5 or less")
  ```

#### Nested If

- An `if` statement inside another `if` statement.

  ```python
  if x > 5:
      if x < 20:
          print("x is between 5 and 20")
  ```

#### Match-Case Statement

- Python’s version of a `switch-case`.

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

  ```python
  for i in range(5):
      print(i)
  ```

#### For-Else Loops

- Executes the `else` block if the loop completes normally without `break`.

  ```python
  for i in range(3):
      print(i)
  else:
      print("Loop finished")
  ```

#### While Loops

- Repeats as long as the condition is `True`.

  ```python
  x = 5
  while x > 0:
      print(x)
      x -= 1
  ```

#### Break Statement

- Exits the loop prematurely.

  ```python
  for i in range(5):
      if i == 3:
          break
      print(i)
  ```

#### Continue Statement

- Skips the rest of the code in the loop and proceeds to the next iteration.

  ```python
  for i in range(5):
      if i == 3:
          continue
      print(i)
  ```

#### Pass Statement

- Placeholder that does nothing.
- Ellipse(...) ccan also be used as placeholder

  ```python
  if x > 0:
      pass
  ```

#### Nested Loops

- A loop inside another loop.

  ```python
  for i in range(3):
      for j in range(2):
          print(i, j)
  ```

## Strings

- A sequence of characters enclosed in quotes.

  ```python
  s = "Hello, World!"
  ```

#### Slicing Strings

- Extracts substrings using indices.

  ```python
  print(s[0:5])  # Output: Hello
  ```

#### Modify Strings

- Use built-in methods like `lower()`, `upper()`, `strip()`, `replace()`, etc.

  ```python
  print(s.lower())
  ```

#### String Concatenation

- Joining strings using `+` operator.

  ```python
  name = "Alice"
  greeting = "Hello, " + name
  ```

#### String Formatting

- Formatting strings using f-strings or `format()`.

  ```python
  age = 25
  print(f"I am {age} years old")
  ```

#### Escape Characters

- Special characters like `\n` (newline) and `\t` (tab).

  ```python
  print("Hello\nWorld")
  ```

## Lists

#### Access List Items

- Use indexing to access elements.

  ```python
  lst = [1, 2, 3]
  print(lst[0])
  ```

#### Change List Items

- Modify elements by index.

  ```python
  lst[1] = 10
  ```

#### Add List Items

- Use `append()`, `insert()`, or `extend()`.

  ```python
  lst.append(4)
  ```

#### Remove List Items

- Use `remove()`, `pop()`, or `del`.

  ```python
  lst.pop(1)
  ```

#### Loop Lists

- Iterate using `for` loop.

  ```python
  for item in lst:
      print(item)
  ```

#### List Comprehension

- Compact syntax for creating lists.

  ```python
  squares = [x**2 for x in range(5)]
  ```

#### Sort Lists

- Use `sort()` or `sorted()`.

  ```python
  lst.sort()
  ```

#### Copy Lists

- Use `copy()` or slicing.

  ```python
  new_list = lst.copy()
  ```

#### Shallow Copy

- Copies only references to objects, so changes to mutable objects inside affect both copies.

  ```python
  import copy
  list1 = [[1, 2], [3, 4]]
  shallow = copy.copy(list1)
  shallow[0][0] = 99
  print(list1)  # [[99, 2], [3, 4]]
  ```

#### Deep Copy

- Creates independent copies of all objects, so changes don’t affect the original.

  ```python
  deep = copy.deepcopy(list1)
  deep[0][0] = 100
  print(list1)  # [[99, 2], [3, 4]]
  ```

  #### Join Lists

- Use `+` or `extend()`.

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

##### Dt. 13 Feb, 2025.

Today we will be continuing learning from [TutorialsPoint](https://www.tutorialspoint.com/python/index.htm). We shall cover Functions, Tuples, Sets, Dictionaries and so on.

## Functions & Modules

- Blocks of reusable code that perform a specific task
- Defined using the `def` keyword
- Can accept parameters and return values
- Improves code readability and reusability

#### Features

- Supports default, keyword, positional, and arbitrary arguments
- Can return multiple values
- Supports recursion
- Functions can be assigned to variables and passed as arguments

#### Pass by Reference vs Value

- Immutable objects (e.g., integers, strings) are passed by value
- Mutable objects (e.g., lists, dictionaries) are passed by reference
- Modifying a mutable object inside a function affects the original object

#### Default Arguments

- Assign default values to parameters
- If no argument is provided, the default value is used

  ```python
  def greet(name="Guest"):
      print("Hello,", name)
  ```

#### Keyword Arguments

- Arguments are passed using parameter names
- Order of arguments does not matter

  ```python
  def greet(name, age):
      print(f"Name: {name}, Age: {age}")
  greet(age=25, name="Alice")
  ```

#### Keyword-Only Arguments

- Specified after `*` in the function definition
- Must be passed using parameter names

  ```python
  def greet(*, name):
      print("Hello,", name)
  ```

#### Positional Arguments

- Arguments are passed based on their position in the function call

  ```python
  def add(a, b):
      return a + b
  add(2, 3)
  ```

#### Positional-Only Arguments

- Specified before `/` in the function definition
- Cannot be passed as keyword arguments

  ```python
  def multiply(a, b, /):
      return a * b
  ```

#### Arbitrary Arguments

- Allows passing a variable number of arguments
- Uses `*args` for positional arguments and `**kwargs` for keyword arguments

  ```python
  def func(*args, **kwargs):
      print(args, kwargs)
  ```

  ![alt text](/images/order_of_formal_arguments.jpg)

#### lambda function

- Anonymous functions defined using `lambda`
- Single-line, inline functions

  ```python
  square = lambda x: x * x
  print(square(5))
  ```

#### Variables Scope

- **Local Scope**: Variables inside a function
- **Global Scope**: Variables outside functions, accessible everywhere
- **Nonlocal Scope**: Variables in an enclosing function

#### locals() and globals()

- `locals()`: Returns a dictionary of local variables
- `globals()`: Returns a dictionary of global variables

  ```python
  x = 10
  def func():
      y = 5
      print(locals())
      print(globals()["x"])
  ```

#### Function Annotations

- Metadata for function parameters and return values

  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```

#### Modules

- Files containing Python code (functions, variables, classes)
- Can be imported using `import` statement

  ```python
  import math
  print(math.sqrt(16))
  ```

- Adding `if __name__ == '__main__'` inside modules, ensures that the script runs only when executed directly, preventing unintended execution when the module is imported elsewhere.

#### Packages

- Collection of related modules stored in a directory
- Contains an `__init__.py` file to mark it as a package

  ```python
  from mypackage import mymodule
  ```

#### Built-in Functions

- Predefined functions available in Python
- Examples: `print()`, `len()`, `type()`, `id()`, `sum()`

## Tuples

- Ordered, immutable collection of elements
- Defined using parentheses `()`
- Supports heterogeneous data types
- Useful for read-only data storage

#### Features

- Faster than lists due to immutability
- Hashable if containing only immutable elements
- Supports indexing and slicing
- Can be used as dictionary keys

#### Access Tuple Items

- Access elements using zero-based indexing
- Supports negative indexing

  ```python
  t = (10, 20, 30)
  print(t[0])  # Output: 10
  print(t[-1])  # Output: 30
  ```

#### Update Tuples

- Tuples are immutable; elements cannot be changed directly
- Can create a new tuple by concatenation

  ```python
  t = (1, 2, 3)
  t = t + (4, 5)
  print(t)  # Output: (1, 2, 3, 4, 5)
  ```

#### Unpack Tuples

- Assign tuple elements to multiple variables

  ```python
  t = (10, 20, 30)
  a, b, c = t
  print(a, b, c)  # Output: 10 20 30
  ```

#### Loop Tuples

- Iterate over tuple elements using loops

  ```python
  t = ("apple", "banana", "cherry")
  for item in t:
      print(item)
  ```

#### Join Tuples

- Combine multiple tuples using `+` operator

  ```python
  t1 = (1, 2, 3)
  t2 = (4, 5, 6)
  t3 = t1 + t2
  print(t3)  # Output: (1, 2, 3, 4, 5, 6)
  ```

- `sum()` can join tuples by adding them together, but it requires specifying an empty tuple as the starting value to avoid type errors.

  ```python
  t1 = (1, 2)
  t2 = (3, 4)
  t3 = (5, 6)
  result = sum((t1, t2, t3), ())
  print(result)  # Output: (1, 2, 3, 4, 5, 6)
  ```

## Sets

- Unordered collection of unique elements
- Defined using curly braces `{}` or `set()`
- Does not allow duplicate values
- Supports mathematical set operations

#### Features

- Mutable (can add or remove elements)
- Unordered (does not maintain insertion order)
- Fast membership testing using hashing
- Can contain only immutable data types

#### Frozen Set

- Immutable version of a set
- Defined using `frozenset()`
- Supports set operations but cannot be modified

  ```python
  fs = frozenset([1, 2, 3])
  print(fs)
  ```

#### Access Set Items

- No indexing (unordered nature)
- Can check existence using `in` keyword

  ```python
  s = {1, 2, 3}
  print(2 in s)  # Output: True
  ```

#### Add Set Items

- Use `add()` to add a single item
- Use `update()` to add multiple items

  ```python
  s = {1, 2}
  s.add(3)
  s.update([4, 5])
  print(s)  # Output: {1, 2, 3, 4, 5}
  ```

#### Remove Set Items

- Use `remove()` (raises error if item not found)
- Use `discard()` (does not raise error if item not found)
- Use `pop()` to remove a random element

  ```python
  s = {1, 2, 3}
  s.remove(2)
  print(s)  # Output: {1, 3}
  ```

#### Loop Sets

- Iterate using `for` loop

  ```python
  s = {"apple", "banana", "cherry"}
  for item in s:
      print(item)
  ```

#### Join Sets

- Use `union()` to combine sets
- Use `update()` to merge sets

  ```python
  s1 = {1, 2}
  s2 = {3, 4}
  s3 = s1.union(s2)
  print(s3)  # Output: {1, 2, 3, 4}
  ```

#### Copy Sets

- Use `copy()` method to create a copy

  ```python
  s = {1, 2, 3}
  s_copy = s.copy()
  print(s_copy)
  ```

#### Set Operators

- `|` (Union) - Combines sets
- `&` (Intersection) - Common elements
- `-` (Difference) - Elements in one set but not another
- `^` (Symmetric Difference) - Elements in either set but not both

  ```python
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  print(s1 | s2)  # Output: {1, 2, 3, 4, 5}
  print(s1 & s2)  # Output: {3}
  print(s1 - s2)  # Output: {1, 2}
  print(s1 ^ s2)  # Output: {1, 2, 4, 5}
  ```

## Dictionaries

- Unordered collection of key-value pairs
- Defined using curly braces `{}` with keys and values separated by colons
- Keys must be unique and immutable (strings, numbers, or tuples)
- Values can be of any data type

#### Features

- Mutable (can add, remove, and modify items)
- Fast lookups using hashing
- Supports dictionary comprehension
- Allows storing nested structures

#### defaultdict()

- Part of `collections` module
- Returns a default value if a key is not found

  ```python
  from collections import defaultdict
  d = defaultdict(int)
  d["a"] += 1
  print(d)  # Output: {'a': 1}
  ```

#### Access Dictionary Items

- Use `dict[key]` to get value (raises KeyError if key does not exist)
- Use `get()` to avoid errors and return a default value

  ```python
  d = {"name": "Alice", "age": 25}
  print(d["name"])  # Output: Alice
  print(d.get("city", "Unknown"))  # Output: Unknown
  ```

#### Change Dictionary Items

- Modify value using `dict[key] = new_value`

  ```python
  d = {"name": "Alice"}
  d["name"] = "Bob"
  print(d)  # Output: {'name': 'Bob'}
  ```

#### Add Dictionary Items

- Assign value to a new key

  ```python
  d = {"name": "Alice"}
  d["age"] = 25
  print(d)  # Output: {'name': 'Alice', 'age': 25}
  ```

#### Remove Dictionary Items

- Use `pop(key)` to remove key-value pair and return value
- Use `del dict[key]` to delete a key
- Use `popitem()` to remove and return the last inserted pair

  ```python
  d = {"name": "Alice", "age": 25}
  d.pop("age")
  print(d)  # Output: {'name': 'Alice'}
  ```

#### Dictionary View Objects

- `keys()`, `values()`, `items()` return dynamic views of dictionary content

  ```python
  d = {"name": "Alice", "age": 25}
  print(d.keys())  # Output: dict_keys(['name', 'age'])
  print(d.values())  # Output: dict_values(['Alice', 25])
  print(d.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])
  ```

#### Loop Dictionaries

- Iterate over keys, values, or key-value pairs

  ```python
  d = {"name": "Alice", "age": 25}
  for key, value in d.items():
      print(key, "->", value)
  ```

#### Copy Dictionaries

- Use `copy()` to create a shallow copy

  ```python
  d = {"name": "Alice"}
  d_copy = d.copy()
  print(d_copy)
  ```

#### Nested Dictionaries

- Dictionaries within dictionaries

  ```python
  students = {
      "student1": {"name": "Alice", "age": 25},
      "student2": {"name": "Bob", "age": 22}
  }
  print(students["student1"]["name"])  # Output: Alice
  ```

## Arrays

- Ordered collection of elements of the same data type
- More efficient than lists for numerical operations
- Requires `array` module in Python

  ```python
  import array
  arr = array.array('i', [1, 2, 3, 4, 5])
  ```

#### Features

- Fixed type storage
- Supports indexing and slicing
- Mutable (can modify elements)
- Efficient memory usage

#### Access Array Items

- Use indexing to retrieve values

  ```python
  print(arr[0])  # Output: 1
  ```

#### Add Array Items

- Use `append()` to add at the end
- Use `insert()` to add at a specific index

  ```python
  arr.append(6)
  arr.insert(2, 10)
  ```

#### Remove Array Items

- Use `remove()` to delete a specific value
- Use `pop()` to remove an item by index

  ```python
  arr.remove(3)
  arr.pop(1)
  ```

#### Loop Arrays

- Use a `for` loop to iterate over array elements

  ```python
  for num in arr:
      print(num)
  ```

#### Copy Arrays

- Use `copy()` method or list slicing

  ```python
  arr_copy = arr[:]
  ```

#### Reverse Arrays

- Use `reverse()` method

  ```python
  arr.reverse()
  ```

#### Sort Arrays

- Use `sorted()` for a new sorted array
- Use `sort()` for in-place sorting

  ```python
  arr.sort()
  ```

#### Join Arrays

- Use `+` operator to concatenate two arrays

  ```python
  arr2 = array.array('i', [6, 7, 8])
  arr3 = arr + arr2
  ```

## File Handling

- Allows reading, writing, and managing files in Python
- Uses built-in `open()` function to handle files

  ```python
  file = open("example.txt", "r")
  content = file.read()
  file.close()
  ```

#### Write to File

- Use `w` mode to overwrite or `a` mode to append

  ```python
  with open("example.txt", "w") as file:
      file.write("Hello, World!")
  ```

#### Read Files

- Use `read()`, `readline()`, or `readlines()`

  ```python
  with open("example.txt", "r") as file:
      content = file.read()
  ```

#### Renaming and Deleting Files

- Use `os.rename()` to rename files
- Use `os.remove()` to delete files

  ```python
  import os
  os.rename("old.txt", "new.txt")
  os.remove("new.txt")
  ```

#### Directories

- Use `os.mkdir()` to create a directory
- Use `os.rmdir()` to remove an empty directory

  ```python
  os.mkdir("new_folder")
  os.rmdir("new_folder")
  ```

#### File Methods

- `file.write()`, `file.read()`, `file.readlines()`
- `file.seek()`, `file.tell()`, `file.close()`

#### OS File/Directory Methods

- `os.listdir()`: List files in a directory
- `os.remove()`: Delete a file
- `os.mkdir()`, `os.rmdir()`: Create and remove directories

#### OS Path Methods

- `os.path.exists()`: Check if a path exists
- `os.path.isfile()`: Check if path is a file
- `os.path.isdir()`: Check if path is a directory
- `os.path.join()`: Join paths properly

I have made boolint() function inside [basic.py](/basic.py). It includes an interesting fact about bool class inheriting from int class. I have also practiced tuples and their workings.

Calling it a day! Will resume from here tomorrow.

##### Dt. 14 Feb, 2025.

We have covered classes and objects already, so let's cover OOPs in depth. I have skimmed through the [TutorialsPoint](https://www.tutorialspoint.com/python/python_oops_concepts.htm) website and provided the summary below -

## Object-Oriented Programming (OOP)

- A programming paradigm that organizes code into objects that contain both data and methods.
- It promotes modularity, reusability, and abstraction.
- Key principles:
  - **Encapsulation**: Bundling data and methods into a single unit.
  - **Inheritance**: Creating new classes from existing ones.
  - **Polymorphism**: Using a single interface for different types.
  - **Abstraction**: Hiding implementation details and exposing only essential features.

#### Classes & Objects

- **Class**: A blueprint for creating objects, defined using the `class` keyword.

  ```python
  class Car:
      def __init__(self, brand, model):
          self.brand = brand
          self.model = model
  ```

- **Object**: An instance of a class that contains actual data.
  ```python
  car1 = Car("Toyota", "Camry")
  print(car1.brand)  # Output: Toyota
  ```

#### Class Attributes

- Shared among all instances of the class.
- Defined within the class but outside any instance methods.
  ```python
  class Employee:
      company = "TechCorp"  # Class attribute
  ```
- Accessed using `ClassName.attribute` or `self.attribute`.

#### Instance Attributes

- Unique to each object and defined inside the constructor (`__init__`).
  ```python
  class Employee:
      def __init__(self, name, salary):
          self.name = name  # Instance attribute
          self.salary = salary
  ```
- Accessed using `self.attribute`.

#### Class Methods

- Defined using the `@classmethod` decorator.
- Operate on class-level attributes.
- Use `cls` as the first parameter instead of `self`.

  ```python
  class Employee:
      company = "TechCorp"

      @classmethod
      def change_company(cls, new_name):
          cls.company = new_name
  ```

#### Static Methods

- Defined using `@staticmethod`.
- Do not modify class or instance data.
- Used for utility functions related to the class.
  ```python
  class MathUtils:
      @staticmethod
      def add(x, y):
          return x + y
  ```

#### Constructors

- Special method `__init__()` is called automatically when an object is created.
- Used to initialize instance attributes.
  ```python
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age
  ```

#### Access Modifiers

- **Public (`name`)**: Accessible from anywhere.
- **Protected (`_name`)**: Indicated by a single underscore, used as a convention.
- **Private (`__name`)**: Name-mangled to prevent accidental modification.
  ```python
  class BankAccount:
      def __init__(self, balance):
          self.__balance = balance  # Private attribute
  ```

#### Inheritance

- A class (child) can inherit properties and behaviors from another class (parent).

  ```python
  class Animal:
      def speak(self):
          return "Sound"

  class Dog(Animal):
      def speak(self):
          return "Bark"
  ```

#### Polymorphism

- Methods in different classes can share the same name but behave differently.

  ```python
  class Cat:
      def sound(self):
          return "Meow"

  class Dog:
      def sound(self):
          return "Bark"
  ```

#### Method Overriding

- A child class can provide a new implementation for a method inherited from its parent.

  ```python
  class Vehicle:
      def start(self):
          return "Starting vehicle"

  class Car(Vehicle):
      def start(self):
          return "Starting car engine"
  ```

#### Method Overloading

- Python does not support method overloading in the traditional sense.
- Achieved using default or variable-length arguments.
  ```python
  class MathOps:
      def add(self, a, b, c=0):
          return a + b + c
  ```

#### Dynamic Binding

- The method that gets called is determined at runtime.

  ```python
  class Parent:
      def show(self):
          print("Parent")

  class Child(Parent):
      def show(self):
          print("Child")

  obj = Child()
  obj.show()  # Output: Child
  ```

#### Dynamic Typing

- Variables do not have fixed types and can hold different types of values at runtime.
  ```python
  x = 5
  x = "hello"  # No type error
  ```

#### Abstraction

- Achieved using abstract base classes (ABC).
- Enforces method implementation in child classes.

  ```python
  from abc import ABC, abstractmethod

  class Shape(ABC):
      @abstractmethod
      def area(self):
          pass
  ```

#### Encapsulation

- Restricts direct access to certain data members.
- Achieved using private attributes (`__attribute`).

#### Interfaces

- Python does not have explicit interfaces but uses abstract base classes to achieve similar functionality.

#### Packages

- Used to organize multiple modules.
- A package is a directory containing a special `__init__.py` file.

#### Inner Classes

- A class defined within another class.
  ```python
  class Outer:
      class Inner:
          pass
  ```

#### Anonymous Classes and Objects

- Python does not support anonymous classes.
- Anonymous objects can be created dynamically using `types.SimpleNamespace`.

#### Singleton Class

- Ensures only one instance exists.
  ```python
  class Singleton:
      _instance = None
      def __new__(cls):
          if cls._instance is None:
              cls._instance = super().__new__(cls)
          return cls._instance
  ```

#### Wrapper Classes

- Used to modify the behavior of an object or function.
- Implemented using decorators.
  ```python
  def wrapper(func):
      def inner():
          print("Before function call")
          func()
          print("After function call")
      return inner
  ```

#### Enums

- Used for defining named constants.

  ```python
  from enum import Enum

  class Color(Enum):
      RED = 1
      BLUE = 2
  ```

#### Reflection

- Allows runtime inspection of classes and objects.

  ```python
  class Person:
      def __init__(self, name):
          self.name = name

  obj = Person("Alice")
  print(getattr(obj, "name"))  # Output: Alice
  ```

#### Python OOP vs C++ & Java

- **No method overloading**: Python does not support function overloading based on different parameter lists like Java/C++.
- **No explicit access specifiers**: Unlike `private`, `protected`, and `public` in C++/Java, Python relies on naming conventions (`_`, `__`).
- **Dynamic typing**: Python does not require explicit type declarations, unlike Java and C++.
- **Multiple inheritance**: Python allows multiple inheritance, unlike Java (which uses interfaces instead).
- **No explicit `this` keyword**: Python uses `self` explicitly in instance methods.
- **No strict interface concept**: Python uses abstract base classes instead of interfaces in Java.
- **Garbage collection**: Python automatically manages memory, whereas C++ requires manual memory management.

### Points to Note -

- **Ctrl + Click Interesting**:

  - Allows quick navigation to function, class, or variable definitions in IDEs.

- **Namespace**:

  - A container for identifiers to avoid naming conflicts.
  - Types: Local, Global, Built-in.

- **Accessor and Mutator**:

  - **Accessor (Getter)**: Retrieves a private attribute's value.
  - **Mutator (Setter)**: Modifies a private attribute's value.

- **MRO (Method Resolution Order)**:

  - Defines the order of method inheritance in multiple inheritance.
  - Uses C3 Linearization (`Class.__mro__`).

- **Duck Typing**:

  - Determines an object's type by its behavior rather than inheritance.
  - "If it quacks like a duck, it's a duck."

- **Operator Overloading**:

  - Customizes built-in operators using special methods (`__add__()`, `__sub__()`).

- **DRY (Don't Repeat Yourself) Principle**:
  - Encourages code reuse to reduce redundancy.
  - Achieved through functions, inheritance, and modular design.

I have watched [OOP in Python - Telusko](https://www.youtube.com/watch?v=qiSCMNBIP2g) and [Abstract Class and Abstract Method in Python - Telusko](https://www.youtube.com/watch?v=UDmJGvM-OUw), it is very concise and to the point. Must watch!

Along with that I have implemented all the OOPs concept. You can access them from here -

- Objects & Classes -

  - Code - [login.py](/OOPs/login.py)
  - Output - [Snapshot](/images/Login.png)

- Inheritance -

  - Code - [inheritance.py](/OOPs/inheritance.py)
  - Output - [Snapshot](/images/Inheritance.png)

- Polymorphism -

  - Code - [polymorphism.py](/OOPs/polymorphism.py)
  - Output - [Snapshot](/images/Polymorphism.png)

- Abstraction -
  - Code - [abstraction.py](/OOPs/abstraction.py)
  - Output - [Snapshot](/images/Abstraction.png)

I also read this blog - [Abstract Classes and Abstract Methods in Python](https://medium.com/@prashampahadiya9228/abstract-classes-and-abstract-methods-in-python-e632ea34bc79), it explains the concept using real-life scenarios.

Calling it a day! See you on Monday!

##### Dt. 17 Feb, 2025.

Today I will be covering some advance topics in Python, like decorator, singleton design pattern, PDB and so on...

## Advance Concepts

#### Decorator

- A function that modifies another function or method without changing its code.
- Implemented using `@decorator_name` syntax.
- Used for logging, authentication, timing, and enforcing access control.
- Can be applied to both functions and methods.

```python
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello")

say_hello()
```

#### Lambda

- Anonymous, single-expression function using `lambda` keyword.
- Used for short, simple functions where defining a full function is unnecessary.
- Often used in combination with `map()`, `filter()`, and `sorted()`.

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

#### Map

- Applies a function to all elements in an iterable.
- Returns a `map` object (can be converted to a list).
- Useful for transforming data in a concise way.

```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
```

#### Reduce

- Aggregates elements using a function.
- Requires `functools.reduce`.
- Used for cumulative computations like sum, product, or concatenation.

```python
from functools import reduce

numbers = [1, 2, 3, 4]
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)  # Output: 10
```

#### Filter

- Filters elements from an iterable based on a condition.
- Returns only elements that satisfy the condition.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```

#### File Read and Write

- The `open()` function is used to read/write files.
- Supports multiple modes: `r` (read), `w` (write), `a` (append), `rb/wb` (binary).
- Always use `with open()` to handle file closing automatically.

```python
with open("file.txt", "w") as file:
    file.write("Hello, World!")

with open("file.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, World!
```

#### Singleton

- Ensures a class has only one instance.
- Used for global state management, logging, and database connections.

```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True
```

#### Python Debugger (PDB)

- Debugging tool for stepping through Python code.
- Use `import pdb; pdb.set_trace()` to set breakpoints.
- Commands:
  - `n` (next): Execute next line.
  - `s` (step): Step into function calls.
  - `c` (continue): Continue execution.
  - `q` (quit): Exit debugger.

```python
import pdb

def test():
    x = 5
    pdb.set_trace()  # Debugging starts here
    y = x * 2
    print(y)

test()
```

#### Sync and Async

- **Synchronous**:
  - Code executes sequentially, one statement at a time.
  - Slower when dealing with I/O-bound or network-based operations.
- **Asynchronous**:
  - Tasks run concurrently using `async` and `await`.
  - Allows non-blocking execution, improving performance for I/O-bound operations.
  - Used for handling multiple network requests, database queries, and file operations efficiently.

##### Future in Async:

- A `Future` is an object representing the result of an asynchronous computation.
- It acts as a placeholder for a value that will be available later.
- Used with `asyncio` to handle concurrent tasks.

```python
import asyncio

async def compute():
    await asyncio.sleep(2)
    return "Result ready"

async def main():
    future = asyncio.ensure_future(compute())
    print("Task started")
    result = await future
    print(result)

asyncio.run(main())
```

##### Uses of Async Programming:

- Web scraping with multiple requests.
- Real-time applications like chatbots and gaming servers.
- Handling multiple file operations efficiently.
- Improving responsiveness in GUI applications.
- Running background tasks without blocking the main program.

I have watched videos on youtube for each topic and practiced them as well. The links are providied below.

- Decorator -

  - Resources - [Video 1](https://www.youtube.com/watch?v=FsAPt_9Bf3U) | [Video 2](https://www.youtube.com/watch?v=KlBPCzcQNU8)
  - Code - [decorator.py](/Advance/decorator.py)
  - Output - [Snapshot](/images/Decorator.png)

- Map Filter Reduce Lambda -

  - Resources - [Video 1](https://www.youtube.com/watch?v=kYIrDMbqunw) | [Video 2](https://www.youtube.com/watch?v=cKlnR-CB3tk)
  - Code - [advance.py](/Advance/advance.py)
  - Output - [Snapshot](/images/Lambda.png)

- File Objects -

  - Resources - [Video](https://www.youtube.com/watch?v=Uh2ebFW8OYM)
  - Code - [file.py](/Advance/file.py)
  - Output - [Snapshot](/images/File.png)

- Singletons -

  - Resources - [Video 1](https://www.youtube.com/watch?v=6IV_FYx6MQA) | [Video 2](https://www.youtube.com/watch?v=sppHANksoG4)
  - Code - [singleton.py](/Advance/singleton.py)
  - Output - [Snapshot](/images/Singleton.png)

- Python Debugger -

  - Resources - [Video](https://www.youtube.com/watch?v=ChuU3NlYRLQ)
  - Code - [advance.py](/Advance/advance.py)
  - Output - [Snapshot](/images/PDB.png)

- AsyncIO -
  - Resources - [Video 1](https://www.youtube.com/watch?v=6RbJYN7SoRs) | [Video 2](https://www.youtube.com/watch?v=RIVcqT2OGPA)
  - Code - [advance.py](/Advance/advance.py)
  - Output - [Snapshot](/images/AsyncIO.png)

Alright! So that's it for today. See you tomorrow.

##### Dt. 18 Feb, 2025.

Today let's cover some more advance concepts. We will be learning about Pylint, Iterators and Generators, Collections as well as Serialization in Python.

#### Venv

- A virtual environment tool in Python that helps manage project-specific dependencies.
- Prevents conflicts between different projects by isolating package installations.
- Created using:
  ```bash
  python3 -m venv <project-name>
  ```
- Activation:
  - Windows: `myenv\Scripts\activate`
  - macOS/Linux: `source <project-name>/bin/activate`
- View installed packages:
  ```bash
  pip list
  ```
- Save dependencies for sharing:
  ```bash
  pip freeze > requirements.txt  # Stores dependencies in requirements.txt
  ```
- Install dependencies from a file:
  ```bash
  pip install -r requirements.txt
  ```
- Deactivate environment:
  ```bash
  deactivate
  ```
- Delete environment by removing its directory.
- Avoid placing files inside the `venv` directory.
- Use `.gitignore` to exclude the virtual environment from version control.
- Alternative tools: `virtualenv` and `pipenv`.

#### Pylint

- A static analysis tool that helps improve Python code quality.
- Checks for errors, enforces coding standards (PEP 8), and suggests improvements.
- Installed using:
  ```bash
  pip install pylint
  ```
- Run analysis on a script:
  ```bash
  pylint script.py
  ```
- Provides a numeric score based on code quality.
- Helps detect issues like unused variables, missing docstrings, and redundant imports.
- Categories of messages:
  - `[R]` Refactor: Good practice violations.
  - `[C]` Convention: Coding standard violations.
  - `[W]` Warning: Stylistic or minor programming issues.
  - `[E]` Error: Major programming mistakes (likely bugs).
  - `[F]` Fatal: Errors preventing further processing.
- **Comparison:**
  - `pylint` checks logic (e.g., missing method definitions), while `flake8` focuses on formatting.

#### Iterators and Generators

- **Iterators**:

  - Objects that allow sequential access to elements using `__iter__()` and `__next__()`.
  - Memory efficient as they don’t require all elements to be stored in memory.
  - Example:
    ```python
    class Counter:
        def __init__(self, start, end):
            self.current = start
            self.end = end
        def __iter__(self):
            return self
        def __next__(self):
            if self.current >= self.end:
                raise StopIteration
            value = self.current
            self.current += 1
            return value
    for num in Counter(1, 5):
        print(num)
    ```

- **Generators**:
  - Special functions using `yield` that produce values lazily.
  - More memory efficient than iterators since they generate values only when needed.
  - Example:
    ```python
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    print(list(fibonacci(5)))  # Output: [0, 1, 1, 2, 3]
    ```

#### Collections

- The `collections` module provides advanced data structures beyond built-in types.
- Common types:
  - `namedtuple`: Tuple with named fields, improving readability.
  - `deque`: Double-ended queue for fast appends/pops from both ends.
  - `Counter`: Dictionary subclass for counting elements in an iterable.
  - `defaultdict`: Dictionary with default values to avoid `KeyError`.
  - `OrderedDict`: Maintains insertion order of keys.

```python
from collections import Counter, deque
counter = Counter("mississippi")
print(counter)  # Output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

queue = deque([1, 2, 3])
queue.appendleft(0)
print(queue)  # Output: deque([0, 1, 2, 3])
```

#### Serializer

- Converts Python objects into a format suitable for storage or transmission.
- Used in APIs, caching, and data persistence.
- **Common serializers:**
  - `pickle`: Serializes Python objects into a binary format.
  - `json`: Converts Python objects into a human-readable JSON format.
  - `marshal`: Used internally by Python to serialize code objects.

##### Pickle Serialization Example:

```python
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Bob", 30)
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)
```

- **Deserialization using Pickle**:

```python
with open("person.pkl", "rb") as f:
    loaded_person = pickle.load(f)
print(loaded_person.name, loaded_person.age)  # Output: Bob 30
```

I have watched videos on youtube for each topic and practiced them as well. The links are provided below.

- Venv -

  - Resources - [venv module](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)

- Pylint -

  - Resources - [Pylint](https://www.youtube.com/watch?v=fFY5103p5-cf) | [Blog](https://realpython.com/python-code-quality/) | [Doc - pep 8](https://pep8.org/)
  - Code - [pylint.py](/Advance/pylint.py)
  - Output - [Snapshot](/images/Pylint.png)

- Iterators and Generators -

  - Resources - [Iterators And Generators](https://www.youtube.com/watch?v=jTYiNjvnHZY) | [Our Own Iterators](https://www.youtube.com/watch?v=C3Z9lJXI6Qw) | [Doc - Iterator](https://docs.python.org/3/tutorial/classes.html#iterators) | [Doc - Generator](https://docs.python.org/3/tutorial/classes.html#generators)
  - Code - [iterator&generator.py](/Advance/iterator&generator.py)
  - Output - [Snapshot](/images/IteratorAndGenerator.png)

- Collections -

  - Resources - [Edureka](https://www.youtube.com/watch?v=QswQA1lRIQY) | [Patrick Loeber](https://www.youtube.com/watch?v=UdcPhnNjSEw) | [samer Sallam - Builtin Collections](https://www.youtube.com/watch?v=mgtbt7f_CmY) | [Doc - Collection Module](https://docs.python.org/3/library/collections.html#module-collections)
  - Code - [collection.py](/Advance/collection.py)
  - Output - [Snapshot](/images/Collections.png)

- Serialization/Pickling -

  - Resources - [Simplilearn](https://www.youtube.com/watch?v=Y-QerJs0jMk) | [Sentdex](https://www.youtube.com/watch?v=2Tw39kZIbhs) | [Durga Sir](https://www.youtube.com/watch?v=MsRvqMxOryM)
  - Code - [serialization.py](/Advance/serialization.py)
  - Output - [Snapshot](/images/Serialization.png)

So that's it for today. See you tomorrow!

##### Dt. 19 Feb, 2025.

We'll cover Multithreading, Unit Testing and Request Module today. So let's get started.

#### Multithreading

- Allows concurrent execution of multiple threads in a single process.
- Useful for I/O-bound operations like file handling and network requests.
- Uses `threading` module in Python.
- **Creating a Thread:**

  ```python
  import threading

  def print_numbers():
      for i in range(5):
          print(i)

  thread = threading.Thread(target=print_numbers)
  thread.start()
  thread.join()  # Wait for thread to finish
  ```

- **Thread Synchronization:**
  - Use `Lock` to prevent race conditions when multiple threads modify shared data.
  ```python
  lock = threading.Lock()
  lock.acquire()
  # Critical section
  lock.release()
  ```
- **Global Interpreter Lock (GIL):**
  - Limits Python threads to run one at a time, reducing CPU-bound performance gains.
  - Use multiprocessing for CPU-bound tasks.

#### Request Module

- Used to send HTTP requests in Python.
- Installed using `pip install requests`.
- **Making GET Request:**
  ```python
  import requests
  response = requests.get("https://api.example.com/data")
  print(response.status_code, response.json())
  ```
- **Making POST Request:**
  ```python
  data = {"name": "Alice"}
  response = requests.post("https://api.example.com/data", json=data)
  ```
- **Handling Errors:**
  ```python
  try:
      response = requests.get("https://api.example.com/data", timeout=5)
      response.raise_for_status()
  except requests.exceptions.RequestException as e:
      print("Error:", e)
  ```

#### Unit Testing

- Helps test individual units of code to ensure correctness.
- Uses Python’s built-in `unittest` framework.
- **Creating a Test Case:**

  ```python
  import unittest

  def add(a, b):
      return a + b

  class TestMath(unittest.TestCase):
      def test_add(self):
          self.assertEqual(add(2, 3), 5)

  if __name__ == "__main__":
      unittest.main()
  ```

- **Assertions:**
  - `assertEqual(a, b)`: Check if `a == b`
  - `assertTrue(x)`: Check if `x` is `True`
  - `assertRaises(Exception, func)`: Check if `func` raises `Exception`
- **Running Tests:**
  ```bash
  python -m unittest test_script.py
  ```

I have watched videos on youtube for each topic and practiced them as well. The links are provided below.

- Multithreading -

  - Resources - [Telusko](https://www.youtube.com/watch?v=GqHLztqy0PU) | [Corey Schafer](https://www.youtube.com/watch?v=IEEhzQoKtQU) | [Doc - Multithreading](https://docs.python.org/3/tutorial/stdlib2.html#multi-threading)
  - Code - [multithreading.py](/Advance/multithreading.py)
  - Output - [Threading](/images/Threading.png) | [Img-Download-Threading](/images/Img-Download-Threading.png)

- Request Module -

  - Resources - [Corey Schafer](https://www.youtube.com/watch?v=tb8gHvYlCFs) | [NeuralNine](https://www.youtube.com/watch?v=Xi1F2ZMAZ7Q) | [Doc - Requests](https://requests.readthedocs.io/en/latest/) | [xkcd - Comic](https://xkcd.com/537/) | [httpbin - For cutom requests](https://httpbin.org/)
  - Code - [request.py](/Advance/request.py)
  - Output - [Requests-1](/images/Requests-1.png) | [Requests-2](/images/Requests-2.png)

- Unit testing -

  - Resources - [Corey Schafer](https://www.youtube.com/watch?v=6tNS--WetLI) | [NeuralNine](https://www.youtube.com/watch?v=UL0opWf3DeM) | [Doc - Unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
  - Code - [unit-testing.py](/Unit%20Testing/unit-testing.py) | [test_employee.py](/Unit%20Testing/test_employee.py)
  - Output - [Test Calculator](/images/Test%20Calculator.png) | [Test Class Employee](/images/Test%20Class%20Employee.png)

I have added unit testing, although it is still pending. So I will complete it tomorrow.
See you then! Bye-bye!

##### Dt. 20 Feb, 2025.

We'll be covering some new topics so stay tuned! But before that let's finish our Unit Testing that we started yesterday.

#### Mocking in Unit Testing

- A technique used in unit testing to replace real objects with mock objects.
- Helps simulate dependencies and isolate the code being tested.
- Python’s `unittest.mock` module provides tools for creating mock objects and defining their behavior.
- Useful for testing APIs, databases, and external services without actual interaction.
- Reduces test dependencies and increases reliability of tests.

Okay so I have modified the above resources. Now we will begin Multiprocessing and Emails in python.

#### Multiprocessing

- Enables parallel execution by creating separate processes, bypassing the Global Interpreter Lock (GIL).
- Ideal for CPU-bound tasks like data processing, image manipulation, and machine learning computations.
- Uses the `multiprocessing` module in Python to create and manage processes.
- Supports process pools for efficient execution of multiple tasks.
- Interprocess Communication (IPC) allows data sharing using `Queue` and `Pipe`.
- More efficient than multithreading for CPU-intensive operations.
- Requires careful management of shared resources to avoid deadlocks and race conditions.

##### Context Manager vs Decorator

- **Context Manager:**
  - Used to manage resources efficiently using `with` statements.
  - Ensures proper setup and teardown of resources like files, network connections, and locks.
  - Helps prevent resource leaks and makes code more readable.
- **Decorator:**
  - Used to modify the behavior of functions or classes without modifying their code.
  - Applied using the `@decorator` syntax.
  - Commonly used for logging, authentication, and performance measurement.
- Both enhance code readability and maintainability but serve different purposes.

##### Future Object

- Represents a computation that may not have completed yet.
- Used in concurrent programming to manage asynchronous operations.
- The `concurrent.futures` module provides `Future` objects for handling results of background tasks.
- Helps improve responsiveness in applications by running expensive tasks in parallel.
- Can be used with thread or process pools to efficiently manage concurrent execution.

#### Emails

- Python provides multiple ways to send emails, primarily using the `smtplib` and `email` modules.
- Supports plain text, HTML emails, and file attachments.
- SMTP (Simple Mail Transfer Protocol) is used to send emails through an external server.
- Authentication is required for most SMTP servers.
- MIME (Multipurpose Internet Mail Extensions) is used to format email content.
- Essential for automated reports, notifications, and alerts in applications.

I have watched videos on youtube for each topic and practiced them as well. The links are provided below.

- Multiprocessing -

  - Resources - [Corey Schafer](https://www.youtube.com/watch?v=fKl2JW_qrso) | [Doc - Multiprocessing](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing)
  - Code - [multiprocessing\_.py](/Advance/multiprocessing_.py)
  - Output - [Multiprocessing](/images/Multiprocessing.png) | [Img-Sizing-Multiprocess](/images/Img-Sizing-Multiprocessing.png)

- Emails -

  - Resources - [Telusko](https://www.youtube.com/watch?v=BsVQ_cBmEwg) | [Corey Schafer](https://www.youtube.com/watch?v=JRCJ6RtE3xU) | [Doc - smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib)
  - Code - [emails.py](/Advance/emails.py)
  - Output - [Emails VSCode](/images/Emails-VS-Code.png) | [Emails Debug Server](/images/Emails-Debug-Server.png)

After covering these core concepts, I started DSA by practicing on LeetCode. You can check them out [here](/DSA-Leetcode-75)

We'll solve some more complex DSA problems tomorrow. So stay tuned!

##### Dt. 21 Feb, 2025.

So today, we will be continuing DSA as well as start with Pandas. So let's get started!

## Data Structures

#### Lists

- Dynamic arrays that store ordered elements.
- Support indexing, slicing, and a variety of built-in functions.
- Operations: Append, Insert, Delete, Sort, Reverse.
- Used for general-purpose storage and traversal.

#### Tuples

- Immutable, ordered collections of elements.
- Faster than lists due to immutability.
- Useful for fixed collections like coordinate pairs or database records.

#### Sets

- Unordered collections of unique elements.
- Support mathematical set operations like union, intersection, and difference.
- Ideal for eliminating duplicates and performing membership tests.

#### Dictionaries

- Key-value pairs providing fast lookups.
- Allow efficient data retrieval and storage.
- Commonly used for mappings, caching, and JSON-like data structures.

#### Stack

- Last-In-First-Out (LIFO) data structure.
- Supports operations: Push (insert), Pop (remove), Peek (view top element).
- Used in function calls, undo mechanisms, and depth-first search algorithms.

#### Queue

- First-In-First-Out (FIFO) data structure.
- Supports operations: Enqueue (insert), Dequeue (remove), Peek (view front element).
- Used in scheduling, breadth-first search, and buffering processes.

#### Deque (Double-Ended Queue)

- Allows insertion and removal from both ends.
- More flexible than a regular queue.
- Used in sliding window problems and task scheduling.

#### Priority Queue

- Elements are removed based on priority rather than insertion order.
- Implemented using a heap data structure.
- Used in Dijkstra's algorithm and job scheduling.

#### Advanced Data Structures

- **Trie (Prefix Tree)**: Efficient for searching prefixes in a collection of strings.
- **Heap**: Min-heap and max-heap used in priority queues.
- **Graph (Adjacency List & Matrix)**: Used in networking, social graphs, and pathfinding.
- **Disjoint Set (Union-Find)**: Helps in cycle detection and Kruskal’s algorithm.
- **Segment Tree**: Efficient for range queries like sum, min, and max.
- **Fenwick Tree (Binary Indexed Tree)**: Used for cumulative frequency calculations.
- **Red-Black Tree / AVL Tree**: Self-balancing binary search trees for maintaining order.

## Algorithms

#### Sorting Algorithms

- **Bubble Sort**: Repeatedly swaps adjacent elements.
- **Selection Sort**: Finds the smallest element and places it at the beginning.
- **Insertion Sort**: Builds a sorted array one element at a time.
- **Merge Sort**: Uses a divide-and-conquer approach.
- **Quick Sort**: Selects a pivot and partitions elements around it.
- **Heap Sort**: Utilizes a heap data structure for sorting.
- **Radix Sort**: Efficient for sorting large numbers by digit processing.
- **Counting Sort**: Works efficiently with a known range of integers.

#### Searching Algorithms

- **Linear Search**: Iterates through elements sequentially.
- **Binary Search**: Efficiently searches sorted lists by halving the search space.
- **Hashing**: Uses a hash function for near-instant lookups.
- **Ternary Search**: Variant of binary search used for unimodal functions.

#### Graph Algorithms

- **Breadth-First Search (BFS)**: Explores nodes level by level.
- **Depth-First Search (DFS)**: Explores as deep as possible before backtracking.
- **Dijkstra's Algorithm**: Finds the shortest path in a weighted graph.
- **Floyd-Warshall Algorithm**: Computes shortest paths between all pairs of nodes.
- **Kruskal’s and Prim’s Algorithms**: Used for finding Minimum Spanning Trees (MST).
- **Bellman-Ford Algorithm**: Solves single-source shortest path problems with negative weights.
- **Topological Sorting**: Used in scheduling tasks with dependencies.

#### Dynamic Programming

- Breaks down problems into smaller subproblems and solves each once.
- **Memoization** (Top-down) and **Tabulation** (Bottom-up) approaches.
- Common problems: Fibonacci sequence, Knapsack problem, Longest Common Subsequence.

#### String Algorithms

- **KMP Algorithm**: Efficient substring search.
- **Rabin-Karp Algorithm**: Uses hashing for fast pattern matching.
- **Z Algorithm**: Used for pattern searching in linear time.

## Pandas

- Pandas is a powerful library for data manipulation and analysis.
- Provides data structures like `DataFrame` and `Series`.
- Built on top of NumPy, making it highly efficient for numerical data.
- Commonly used in data science, machine learning, and data wrangling.

### Core Data Structures

#### Series

- A one-dimensional labeled array.
- Supports operations like filtering, aggregation, and indexing.
- Can hold any data type, including integers, floats, and objects.

#### DataFrame

- A two-dimensional table-like data structure.
- Allows row and column operations similar to SQL tables and Excel spreadsheets.
- Supports merging, grouping, and reshaping data.

### Important Operations

#### Data Loading

- Supports CSV, Excel, JSON, SQL, and more.
- `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`, `pd.read_sql()`.

#### Data Cleaning

- Handling missing values: `dropna()`, `fillna()`.
- Removing duplicates: `drop_duplicates()`.
- Data type conversion: `astype()`.

#### Data Manipulation

- Selecting data using `loc[]` and `iloc[]`.
- Filtering rows based on conditions.
- Applying functions with `apply()`.
- Aggregation using `groupby()`.

#### Merging and Joining

- Combining datasets using `merge()`, `concat()`, and `join()`.
- Useful for handling relational data.

#### Visualization

- Integrates with Matplotlib and Seaborn for data visualization.
- `plot()` method allows easy creation of charts and graphs.

### Use Cases

- Data analysis and transformation.
- Financial data processing.
- Machine learning preprocessing.
- Time series analysis and forecasting.

Pandas simplifies data handling, making it a crucial tool for anyone working with structured data.

I have solved few DSA questions on Leetcode. You can have a look here -> [LeetCode DSA](/DSA-Leetcode-75)

Later on I started Pandas by [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) and practiced it alongside. [This directory](/Pandas) is dedicated to that! Well, I did solve Pandas question on Leetcode as well.[Leetcode Pandas](/Pandas/Leetcode_Pandas.py)

Also, I solved some SQL queries on Leetcode. I have commited them in [database repo](https://github.com/Tanishqua-Simform/database)

Alright then! Meet you tomorrow.(Literally!)

##### Dt. 24 Feb, 2025.

Okay, so today I solved the problems given in LMS assignment. Although they need a little refinning so once that is done I will submit them.

Later I watched a video in pandas by [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS) and practiced it as well...

Then I solved a few DSA questions. [LeetCode DSA](/DSA-Leetcode-75)

That is it for today! I will meet you tomorrow!

##### Dt. 25 Feb, 2025.

Hello there! I have my 1st interview scheduled tomorrow! So today I will be revisiting all my repos.

Okay so, I have covered -

- [Git](https://github.com/Tanishqua-Simform/hello-from-git),
- [HTML/CSS/Bootstrap](https://github.com/Tanishqua-Simform/html-css-bootstrap),
- [Javascript](https://github.com/Tanishqua-Simform/javascript) and
- [jQuery](https://github.com/Tanishqua-Simform/jQuery).

Wish me luck for tomorrow! (Also, I won't be considering today's work in Python module.)

##### Dt. 26 Feb, 2025.

Alright! I have my first evaluation today. So I will be covering rest of the repos -

- [Database](https://github.com/Tanishqua-Simform/database)
- [Python](https://github.com/Tanishqua-Simform/python)

I have my interview now, Wish me luck!

Whoo Hoo, my evaluation is done and I must admit it was really fun thinking about what concept can be used in which scenario. Overall, it was a good experience! Let's see what the feedback has to say!

Later on, I continued Pandas! I know it has been ages since we were studying this, but let's get back in python mode now!

I covered below topics in Pandas -

- Index - [Video](https://www.youtube.com/watch?v=W9XjRYFkkyw&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=3&pp=iAQB) | [Code](Pandas/Stackoverflow_Survey.ipynb)
- Filter - [Video](https://www.youtube.com/watch?v=Lw2rlcxScZY&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=4&pp=iAQB) | [Code](Pandas/Stackoverflow_Survey.ipynb)

That's it for today! Hopefully I will complete Pandas tomorrow!
