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

##### Dunder/Special/Magic Methods

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
- Example:
  ```python
  def greet(name="Guest"):
      print("Hello,", name)
  ```

#### Keyword Arguments

- Arguments are passed using parameter names
- Order of arguments does not matter
- Example:
  ```python
  def greet(name, age):
      print(f"Name: {name}, Age: {age}")
  greet(age=25, name="Alice")
  ```

#### Keyword-Only Arguments

- Specified after `*` in the function definition
- Must be passed using parameter names
- Example:
  ```python
  def greet(*, name):
      print("Hello,", name)
  ```

#### Positional Arguments

- Arguments are passed based on their position in the function call
- Example:
  ```python
  def add(a, b):
      return a + b
  add(2, 3)
  ```

#### Positional-Only Arguments

- Specified before `/` in the function definition
- Cannot be passed as keyword arguments
- Example:
  ```python
  def multiply(a, b, /):
      return a * b
  ```

#### Arbitrary Arguments

- Allows passing a variable number of arguments
- Uses `*args` for positional arguments and `**kwargs` for keyword arguments
- Example:
  ```python
  def func(*args, **kwargs):
      print(args, kwargs)
  ```
  ![alt text](/images/order_of_formal_arguments.jpg)

#### lambda function

- Anonymous functions defined using `lambda`
- Single-line, inline functions
- Example:
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
- Example:
  ```python
  x = 10
  def func():
      y = 5
      print(locals())
      print(globals()["x"])
  ```

#### Function Annotations

- Metadata for function parameters and return values
- Example:
  ```python
  def add(a: int, b: int) -> int:
      return a + b
  ```

#### Modules

- Files containing Python code (functions, variables, classes)
- Can be imported using `import` statement
- Example:
  ```python
  import math
  print(math.sqrt(16))
  ```
- Adding `if __name__ == '__main__'` inside modules, ensures that the script runs only when executed directly, preventing unintended execution when the module is imported elsewhere.

#### Packages

- Collection of related modules stored in a directory
- Contains an `__init__.py` file to mark it as a package
- Example:
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
- Example:
  ```python
  t = (10, 20, 30)
  print(t[0])  # Output: 10
  print(t[-1])  # Output: 30
  ```

#### Update Tuples

- Tuples are immutable; elements cannot be changed directly
- Can create a new tuple by concatenation
- Example:
  ```python
  t = (1, 2, 3)
  t = t + (4, 5)
  print(t)  # Output: (1, 2, 3, 4, 5)
  ```

#### Unpack Tuples

- Assign tuple elements to multiple variables
- Example:
  ```python
  t = (10, 20, 30)
  a, b, c = t
  print(a, b, c)  # Output: 10 20 30
  ```

#### Loop Tuples

- Iterate over tuple elements using loops
- Example:
  ```python
  t = ("apple", "banana", "cherry")
  for item in t:
      print(item)
  ```

#### Join Tuples

- Combine multiple tuples using `+` operator
- Example:
  ```python
  t1 = (1, 2, 3)
  t2 = (4, 5, 6)
  t3 = t1 + t2
  print(t3)  # Output: (1, 2, 3, 4, 5, 6)
  ```
- `sum()` can join tuples by adding them together, but it requires specifying an empty tuple as the starting value to avoid type errors.

- Example:
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
- Example:
  ```python
  fs = frozenset([1, 2, 3])
  print(fs)
  ```

#### Access Set Items

- No indexing (unordered nature)
- Can check existence using `in` keyword
- Example:
  ```python
  s = {1, 2, 3}
  print(2 in s)  # Output: True
  ```

#### Add Set Items

- Use `add()` to add a single item
- Use `update()` to add multiple items
- Example:
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
- Example:
  ```python
  s = {1, 2, 3}
  s.remove(2)
  print(s)  # Output: {1, 3}
  ```

#### Loop Sets

- Iterate using `for` loop
- Example:
  ```python
  s = {"apple", "banana", "cherry"}
  for item in s:
      print(item)
  ```

#### Join Sets

- Use `union()` to combine sets
- Use `update()` to merge sets
- Example:
  ```python
  s1 = {1, 2}
  s2 = {3, 4}
  s3 = s1.union(s2)
  print(s3)  # Output: {1, 2, 3, 4}
  ```

#### Copy Sets

- Use `copy()` method to create a copy
- Example:
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
- Example:
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
- Example:
  ```python
  from collections import defaultdict
  d = defaultdict(int)
  d["a"] += 1
  print(d)  # Output: {'a': 1}
  ```

#### Access Dictionary Items

- Use `dict[key]` to get value (raises KeyError if key does not exist)
- Use `get()` to avoid errors and return a default value
- Example:
  ```python
  d = {"name": "Alice", "age": 25}
  print(d["name"])  # Output: Alice
  print(d.get("city", "Unknown"))  # Output: Unknown
  ```

#### Change Dictionary Items

- Modify value using `dict[key] = new_value`
- Example:
  ```python
  d = {"name": "Alice"}
  d["name"] = "Bob"
  print(d)  # Output: {'name': 'Bob'}
  ```

#### Add Dictionary Items

- Assign value to a new key
- Example:
  ```python
  d = {"name": "Alice"}
  d["age"] = 25
  print(d)  # Output: {'name': 'Alice', 'age': 25}
  ```

#### Remove Dictionary Items

- Use `pop(key)` to remove key-value pair and return value
- Use `del dict[key]` to delete a key
- Use `popitem()` to remove and return the last inserted pair
- Example:
  ```python
  d = {"name": "Alice", "age": 25}
  d.pop("age")
  print(d)  # Output: {'name': 'Alice'}
  ```

#### Dictionary View Objects

- `keys()`, `values()`, `items()` return dynamic views of dictionary content
- Example:
  ```python
  d = {"name": "Alice", "age": 25}
  print(d.keys())  # Output: dict_keys(['name', 'age'])
  print(d.values())  # Output: dict_values(['Alice', 25])
  print(d.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])
  ```

#### Loop Dictionaries

- Iterate over keys, values, or key-value pairs
- Example:
  ```python
  d = {"name": "Alice", "age": 25}
  for key, value in d.items():
      print(key, "->", value)
  ```

#### Copy Dictionaries

- Use `copy()` to create a shallow copy
- Example:
  ```python
  d = {"name": "Alice"}
  d_copy = d.copy()
  print(d_copy)
  ```

#### Nested Dictionaries

- Dictionaries within dictionaries
- Example:
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
- Example:
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
- Example:
  ```python
  print(arr[0])  # Output: 1
  ```

#### Add Array Items

- Use `append()` to add at the end
- Use `insert()` to add at a specific index
- Example:
  ```python
  arr.append(6)
  arr.insert(2, 10)
  ```

#### Remove Array Items

- Use `remove()` to delete a specific value
- Use `pop()` to remove an item by index
- Example:
  ```python
  arr.remove(3)
  arr.pop(1)
  ```

#### Loop Arrays

- Use a `for` loop to iterate over array elements
- Example:
  ```python
  for num in arr:
      print(num)
  ```

#### Copy Arrays

- Use `copy()` method or list slicing
- Example:
  ```python
  arr_copy = arr[:]
  ```

#### Reverse Arrays

- Use `reverse()` method
- Example:
  ```python
  arr.reverse()
  ```

#### Sort Arrays

- Use `sorted()` for a new sorted array
- Use `sort()` for in-place sorting
- Example:
  ```python
  arr.sort()
  ```

#### Join Arrays

- Use `+` operator to concatenate two arrays
- Example:
  ```python
  arr2 = array.array('i', [6, 7, 8])
  arr3 = arr + arr2
  ```

## File Handling

- Allows reading, writing, and managing files in Python
- Uses built-in `open()` function to handle files
- Example:
  ```python
  file = open("example.txt", "r")
  content = file.read()
  file.close()
  ```

#### Write to File

- Use `w` mode to overwrite or `a` mode to append
- Example:
  ```python
  with open("example.txt", "w") as file:
      file.write("Hello, World!")
  ```

#### Read Files

- Use `read()`, `readline()`, or `readlines()`
- Example:
  ```python
  with open("example.txt", "r") as file:
      content = file.read()
  ```

#### Renaming and Deleting Files

- Use `os.rename()` to rename files
- Use `os.remove()` to delete files
- Example:
  ```python
  import os
  os.rename("old.txt", "new.txt")
  os.remove("new.txt")
  ```

#### Directories

- Use `os.mkdir()` to create a directory
- Use `os.rmdir()` to remove an empty directory
- Example:
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

[login.py](/login.py) -> [Output](/images/Login.png)
[inheritance.py](/inheritance.py) -> [Output](/images/Inheritance.png)
[polymorphism.py](/polymorphism.py) -> [Output](/images/Polymorphism.png)
[abstraction.py](/abstraction.py) -> [Output](/images/Abstraction.png)

I also read this blog - [Abstract Classes and Abstract Methods in Python](https://medium.com/@prashampahadiya9228/abstract-classes-and-abstract-methods-in-python-e632ea34bc79), it explains the concept using real-life scenarios.

Calling it a day! See you on Monday!
