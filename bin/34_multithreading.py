"""
multithreading: One process can be splitted into multiple pieces and run.
each pieces are called threads

In Python, multithreading is not PARALLEL?
which means, There is lock called GLOBAL INTERPRETER LOCK (GIL)
which allow only one thread to execute at a time

It is equal to sequential execution then what is the use of multithreading?
- if one thread is waiting for some resource then during that waiting time
it will execute another thread
"""

print("WITHOUT using multithreading")
print("-"*20)
# --------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Total time taken:", end_time-start_time)

print("#"*40, end="\n\n")
################################

print("Using multithreading")
print("-"*20)
# --------------

from threading import Thread

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)


L = [10, 20, 30, 40]

thread_my_square_function = Thread(target=my_square_function, args=(L,))
thread_my_cube_function = Thread(target=my_cube_function, args=(L,))

# start both the threads
thread_my_square_function.start()
thread_my_cube_function.start()

# start() method will just start the thread and goto next line of the program
# start() will not wait for out function execution to complete

thread_my_square_function.join()
thread_my_cube_function.join()
# join() will make both the threads to wait till it completes execution
# so that we will get proper end time

end_time = time.time()

print("Total time taken:", end_time-start_time)

print("#"*40, end="\n\n")
################################

print("WITH DELAY: WITHOUT using multithreading")
print("-"*20)
# --------------

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]

my_square_function(L)
my_cube_function(L)

end_time = time.time()

print("Total time taken:", end_time-start_time)

print("#"*40, end="\n\n")
################################

print("WITH DELAY: Using multithreading")
print("-"*20)
# --------------

from threading import Thread

import time

start_time = time.time()

def my_square_function(my_list):
    for i in my_list:
        print("Square:", i*i)
        time.sleep(0.1)


def my_cube_function(my_list):
    for i in my_list:
        print("Cube:", i*i*i)
        time.sleep(0.1)


L = [10, 20, 30, 40]

thread_my_square_function = Thread(target=my_square_function, args=(L,))
thread_my_cube_function = Thread(target=my_cube_function, args=(L,))

# start both the threads
thread_my_square_function.start()
thread_my_cube_function.start()

# start() method will just start the thread and goto next line of the program
# start() will not wait for out function execution to complete

thread_my_square_function.join()
thread_my_cube_function.join()
# join() will make both the threads to wait till it completes execution
# so that we will get proper end time

end_time = time.time()

print("Total time taken:", end_time-start_time)

print("#"*40, end="\n\n")
################################
