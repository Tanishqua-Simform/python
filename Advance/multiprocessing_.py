# Multiprocessing
''' multiprocessing is a package that supports spawning processes using an API 
similar to the threading module. It is used for parallel programming. 
CPU Bound task can be performed efficiently using multiprocessing.

For large number of items, processes become more performant than threads.

Conclusion - 
For CPU Bound Tasks that do a lot of number crunching use multiprocessing
For I/O Bound Tasks such as disk and network operations use threading.
'''

## Without Multiprocessing
print('\n-------------------------------Without Multiprocessing---------------------------\n')
import time

start = time.perf_counter()

def do_something():
    print(f'Sleeping for 1 second')
    time.sleep(1)
    print(f'Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

## With Multiprocessing
### Method - 1 : Using Multiprocessing module
print('\n-------------------------------With Multiprocessing---------------------------\n')
import multiprocessing

start = time.perf_counter()

def do_something():
    print(f'Sleeping for 1 second')
    time.sleep(1)
    print(f'Done Sleeping...')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

#### 1000 processes together
print('\n-------------------------------1000 processes together---------------------------\n')
import multiprocessing

start = time.perf_counter()

def do_something():
    time.sleep(1)
    
processes = []
for _ in range(1000):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

''' We can also pass arguments to functions using args parameter.
For reference look at multithreading.py module (Method - 2)'''

### Method - 2 : Process Pool Executor
print('\n-------------------------------Process Pool Executor---------------------------\n')
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    # # For single process
    # f1 = executor.submit(do_something, 1)
    # print(f1.result())
    
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

    # # Alternatively, but here the return statements are executed together.
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     results = executor.map(do_something, secs)

    #     for result in results:
    #         print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')

''' Interesting note in the output - As we have 4 core processor, the process for
5, 4, 3, and 2 got started in first batch and then after 2 got completed it got 
replaced with 1. And hence the output is as such - 2, 3, 1, 4, 5

try it for - 
secs = [1, 2, 3, 4, 5] -> finish time will be 6 secs
secs = [2, 2, 3, 4, 5] -> finish time will be 7 secs
secs = [3, 3, 3, 4, 5] -> finish time will be 8 secs
'''

## Real-life usage
print('\n----------------Real Life Example - Img Download from Web-------------------\n')
import time
import concurrent.futures
from PIL import Image, ImageFilter # Pillow library is for image processing

img_names = [
    '878.jpg',
    '734.jpg',
    '589.jpg',
    '768.jpg',
    '576.jpg',
    '083.jpg',
    '953.jpg',
    '374.jpg',
    '265.jpg',
    '927.jpg',
    '062.jpg',
    '520.jpg'
]

### Without Multiprocessing
print('\n--------------------------Without Multiprocessing----------------------------\n')
t1 = time.perf_counter()

size = (1200, 1200)

for img_name in img_names:
    img = Image.open(f'Threading Img Download/{img_name}')
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'Multiprocessing Img Size/{img_name}')
    print(f'{img_name} was processed...')

t2 = time.perf_counter()

print(f'\nFinished in {round(t2 - t1, 2)} sec(s)')


### With Multiprocessing
print('\n--------------------------With Multiprocessing----------------------------\n')
t1 = time.perf_counter()

size = (1200, 1200)

def process_img(img_name):
    img = Image.open(f'Threading Img Download/{img_name}')
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'Multiprocessing Img Size/{img_name}')
    return f'{img_name} was processed...'

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(process_img, img_name) for img_name in img_names]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

t2 = time.perf_counter()

print(f'\nFinished in {round(t2 - t1, 2)} sec(s)')
