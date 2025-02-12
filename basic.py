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

memoryFunctioning()

def dataTypes():
    print('\nModifying list inside tuple example - ')
    names = (1, 2, 3, 4, ['a', 'b'])
    print(names)
    names[4][0] = 'haha'
    print(names)
    names[4].insert(2, [12, 13, 14, 15, 16])
    print(names)

    print('Modifying tuple list inside list example - ')
    cars = ['Ferrari', 'Merc', 'BMW', ('Lamborgini', 'McLaren')]
    print(cars)
    cars[3] = 'laz'
    print(cars)

    print('Boolean')
    print('1' == True, '0' == False, 1 == True, 0 == False)
    print('None - ', bool(None))

dataTypes()