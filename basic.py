# Must write code-snippet for any programming language ;)
print("hello World\n")

def memoryFunctioning():
    # The memory reference of object(value assigned in our case) is same any identifier at first.
    print('id of "May" is - ', id('May'))
    month = 'May'
    print('id of Month variable is - ', id(month))

    num1 = 2678 # This is a literal
    num2 = 2678
    num3 = 2679
    print('\nnum1 is num2', num1 is num2)
    print(f'num2 is num3', num2 is num3)
    num2 = 2679
    print(f'\nAfter re-assignment of num2 with 2679')
    print(f'num2 is num3', num2 is num3)
    num2 -= 1 # Not a literal
    print(f'\nBut now after decrementing, id of num1 and num2 should be same but they are not.')
    print(f'num1 is num2', num1 is num2)

    # The memory of literals from 1 to 256 are fixed and increment by 4 bytes
    print()
    for i in range(0,310,50):
        if i >= 257:
            print('See the memory changes from 257')
            i = 257
        print(id(i), i)

    # After that the memory location of i alternates between 2 places only. To save memory.
    print()
    print('For loop - i alternates')
    for i in range(num1, num1+8):
        print(id(i))

    # Same applies for any loop
    print('While loop - i alternates except 1st time')
    i = 260
    while i < 270:
        print(id(i))
        i += 1
    
    # Memory of None object
    empty = None
    print('\nid of None datatype', id(empty))

    # List and tuple literal
    a = [501,502,503] 
    b = [501,502,503]
    print('a is b - ', a is b)
    print('a[0] is b[0] - ', a[0] is b[0])
    print('a[1] is b[1] - ', a[1] is b[1])
    print('a[2] is b[2] - ', a[2] is b[2])
    print('\nThis is because List/Tuple only contains the memory location of items and not the items themselves.')

# memoryFunctioning()

def dataTypes():
    print('\nModifying list inside tuple example - ')
    names = (1, 2, 3, 4, ['a', 'b'])
    print(names)
    names[4][0] = 'haha'
    print(names)
    names[4].insert(2, [12, 13, 14, 15, 16])
    print(names)

    print('\nModifying tuple list inside list example - ')
    cars = ['Ferrari', 'Merc', 'BMW', ('Lamborgini', 'McLaren')]
    print(cars)
    cars[3] = 'laz'
    print(cars)

    print('\nBoolean')
    print('1' == True, '0' == False, 1 == True, 0 == False)
    print('None - ', bool(None))

    print('\nTuples')
    tup0 = (50,) # tup0 = (50) will give error in for loop 
    print(type(tup0))
    tup1 = (50)
    print(type(tup1))
    tup2 = ('a', 'b', 'c')
    tup2 = (1, 2, 3) # Possible to reassign value but not change any item inside tuple.
    print(tup2)

    print('\nUnpacking in tuple')
    tup3 = (1, 2, 3, 4, 5, 6)
    x, y, *z = tup3
    print('x, y, *z = ', x, y, z)
    x, *y, z = tup3
    print('x, *y, z = ', x, y, z)
    *x, y, z = tup3
    print('*x, y, z = ', x, y, z)

    print('\nList')
    print(id([1,2,3]))
    l1 = [1,2,3]
    print(id(l1))
    print(id([1,2,3]))
    l2 = [1,2,3]
    print(id(l2))
    print(id([1,2,3]))

    print('\nList copy with slice')
    l3 = l2[1:]
    print('l3 is l2', l3 is l2)
    print('l3[0] is l2[1]', l3[0] is l2[1])

# dataTypes()

def memoryInFunctions():

    print('\nFor immutable datatypes like numeric\n')
    def testfunction(arg):
        print ("ID inside the function:", id(arg))
        arg = arg + 1
        print ("new object after increment", arg, id(arg))

    var=10
    print ("ID before passing:", id(var))
    testfunction(var)
    print ("value after function call", var)

    print('\nFor mutable datatypes like list, dict\n')
    def testfunction(arg):
        print ("Inside function:",arg)
        print ("ID inside the function:", id(arg))
        arg=arg.append(100)
    
    var=[10, 20, 30, 40]
    print ("ID before passing:", id(var))
    testfunction(var)
    print ("list after function call", var)

# memoryInFunctions()

def boolInt():
    a = [True, 0, 1, False, True, 2]
    b = 0
    c = 0
    for i in a:
        if isinstance(i, bool):
            b += 1
        elif isinstance(i, int):
            c += 1

    print(b, c)
    
    print(id(1))
    print(id(bool(1)))
    num = 1
    numBool = bool(1)
    print(id(num))
    print(id(numBool))


    print(isinstance(1.0, float))
    print(isinstance(1, float))
    print(1 == 1.0)

    print(isinstance(True, int))
    print(type(isinstance(1, int)))

    print(issubclass(bool, int))
    print(issubclass(int, bool))

boolInt()