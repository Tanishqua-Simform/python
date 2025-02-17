# # Advance Concepts

# ## Lambda Function
# print('\n--------------------LAMBDA FUNCTION--------------------\n')
# sqr = lambda x: x**2
# print('The square of 8 is :', sqr(8))

# ## Map Function
# print('\n----------------------MAP FUNCTION---------------------\n')

# ### Using Lambda Function
# nums = [1, 2, 3, 4, 5, 6, 7]
# squares = list(map(sqr, nums))
# print('The squares of nums are :', squares)

# ### Using normal function
# def cube(n):
#     return n ** 3

# cubes = list(map(cube, nums))
# print('The cubes of nums are :', cubes)

# ## Filter Function
# print('\n--------------------FILTER FUNCTION--------------------\n')
# odds = list(filter(lambda x: x % 2 == 0, nums))
# print('The odd no.s in nums are :', odds)

# ## Reduce Function
# print('\n--------------------REDUCE FUNCTION--------------------\n')
# from functools import reduce
# product = reduce(lambda x, y: x*y, nums)
# print('The product of nums is :', product)


# ## Python Debugger PDB
# print('\n--------------------Python Debug PDB--------------------\n')
# ''' It is used to debug python code in command line. Some of the commands are -
# l               - list 3 statements before and after current breakpoint
# n               - Execute next line
# c               - Continues to next breakpoint.
# s               - Steps inside a function call
# p               - Prints something in CL
# <variable-name> - Print its value (except for variable named as n)
# b               - List all the breaks
# b <line-number> - Puts a break on that line.
# b <func-name>   - Puts a break on that function.
# cl              - Clears all the breaks.
# '''
# import pdb

# def transform(x, y):
#     y = y**2
#     x *= 2
#     z = x+y
#     return z

# x = 50
# y = 60
# z = 5
# n = 1000

# pdb.set_trace()
# transform(5, 10)
# print('z = ', z)
# n = transform(2, 3)
# print('n = ', n)

##  AsyncIO and the Event Loop
print('\n-----------------------AsyncIO----------------------\n')
''' AsyncIO is not Multithreading or Multiprocessing.
It is concurrent programming '''
import asyncio

async def main():
    task = asyncio.create_task(other())
    print('A')
    await asyncio.sleep(5)
    print('B')
    await task # It forces the program to wait for a call to finish executing.

async def other():
    print('1')
    await asyncio.sleep(2)
    print('2')

asyncio.run(main())

# When other function returns a value
print('\nTrying with return value\n')
async def main1():
    task = asyncio.create_task(other1())
    print('A')
    await asyncio.sleep(5)
    print('B')
    return_value = await task    # This is a Future. Similar to promises in JS.
    print('The return value of other function is {}'.format(return_value))

async def other1():
    print('1')
    await asyncio.sleep(2)
    print('2')
    return 10

asyncio.run(main1())
