# Multithreading
''' Threading is a technique for decoupling tasks which are not sequentially dependent. 
Threads can be used to improve the responsiveness of applications that accept user 
input while other tasks run in the background. A related use case is running I/O in 
parallel with computations in another thread.

In human language - For tasks that are IO bound we can use Multithreading as it will
provide concurrency to our program and we will be able to finish multiple 
tasks together, rather than going one after the another.

Although for CPU bound tasks this will not be beneficial. Rather it will 
make the program slower due to creation and deletion of threads. 
So for these, we may require multiprocessing.

Conclusion - 
Multithreading - It does not work parallely. Another thread takes up CPU
only when it is in Wait state. It is said to work concurrently.
Multiprocessing - It works parallely and uses multi-core for processing.'''

## Without Threading - Runs in Main Thread one after another.
print('\n-------------------------------Without Threading---------------------------\n')
class Hello:
    def run(self):
        for _ in range(5):
            print('Hello')

class Hi:
    def run(self):
        for _ in range(5):
            print('Hi')

h1 = Hello()
h2 = Hi()

h1.run()
h2.run()


## With Threading - makes 2 threads alongside Main thread
### Method - 1 : Class Objects by Telusko
print('\n-------------------------------Threading - Class Objects--------------------------\n')
from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for _ in range(5):
            print('Hello')
            sleep(0.5) # Makes all the threads to go alternatively.
            

class Hi(Thread): # Inherits from Thread class
    def run(self):
        for _ in range(5):
            print('Hi')
            sleep(0.5)

h1 = Hello()
h2 = Hi()

h1.start() # Starts new thread h1
sleep(0.1) # Makes the 2nd thread after some interval, to avoid collisions
h2.start() # Starts new thread h2

h1.join() # Completes the thread first and then goes to main thread for execution
h2.join()

print('Bye') # This is inside Main Thread


### Method - 2 : Functions by Corey Schafer
print('\n-------------------------------Threading - Functions--------------------------\n')
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    print(f'Done Sleeping...{seconds}')

threads = []

for sec in range(1,6):
    t = threading.Thread(target=do_something, args=[sec])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)}')

### Method - 3 : Thread Pool Executor
print('\n----------------Threading - Functions using Concurrent.futures module-------------------\n')
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} second(s)')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

#Alternatively, but here the return statements are executed together.
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

#     for result in results:
#         print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)}')


## Real-life usage
print('\n----------------Real Life Example - Img Download from Web-------------------\n')
import request
import time
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

### Without Multithreading
print('\n--------------------------Without Multithreading----------------------------\n')
t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = request.get(img_url).content
    img_name = img_url.split('/')[3].split('-')[1]
    img_name = f'{img_name[-3:]}.jpg'
    with open(f'Threading Img Download/{img_name}', 'wb') as img:
        img.write(img_bytes)
        print(f'{img_name} was downloaded...')

t2 = time.perf_counter()

print(f'\nFinished in {round(t2 - t1, 2)} sec(s)')

### With Multithreading
print('\n--------------------------With Multithreading----------------------------\n')
t1 = time.perf_counter()

def img_download(img_url):
    img_bytes = request.get(img_url).content
    img_name = img_url.split('/')[3].split('-')[1]
    img_name = f'{img_name[-3:]}.jpg'
    with open(f'Threading Img Download/{img_name}', 'wb') as img:
        img.write(img_bytes)
        return f'{img_name} was downloaded...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(img_download, img_url) for img_url in img_urls]

    for future in concurrent.futures.as_completed(results):
        print(future.result())

t2 = time.perf_counter()

print(f'\nFinished in {round(t2 - t1, 2)} sec(s)')
