"""
 📌 Multi-Threading (basics)
        - Thread: The smallest unit of a program that can run independently.
        - Multithreading: Running multiple threads concurrently within the same program.
        - Useful for I/O-bound tasks (like file operations, network requests) rather than CPU-bound tasks (due to GIL in CPython).

    When we have to do some task parallely this is the best thing to do
"""
import time
from time import perf_counter

"""
| Feature  | Thread                           | Process               |
| -------- | -------------------------------- | --------------------- |
| Memory   | Shares memory with other threads | Separate memory space |
| Creation | Light-weight, faster             | Heavy-weight, slower  |
| Use case | I/O-bound tasks                  | CPU-bound tasks       |
"""

# There are 2 type of thread module to use
# 1. threading :- high-level, recommended
# 2. _thread :- low-level, not recommended

# ========================
# Threading
# ========================

# Method 1 – Using threading.Thread with a function
import threading

def print_numbers(n):
    print(f"Numbers: {n},going to sleep for {n} seconds...")
    time.sleep(n)

# ------------------------
# Without multithreading :- take 6 sec to finish execution
# ------------------------
time1 = perf_counter()
print_numbers(1)
print_numbers(2)
print_numbers(3)
time2 = perf_counter()
print(f"Time: {time2 - time1} seconds")
# Time: 6.007603915997606 seconds

# Ans:- Numbers: 1,going to sleep for 1 seconds...
#       Numbers: 2,going to sleep for 2 seconds...
#       Numbers: 3,going to sleep for 3 seconds...

# ------------------------
# With Multithreading :- take 3 sec to finish execution
# ------------------------

t1 = threading.Thread(target=print_numbers, args=[1])
t2 = threading.Thread(target=print_numbers, args=[2])
t3 = threading.Thread(target=print_numbers, args=[3])

time1 = perf_counter()
t3.start()
t2.start()
t1.start()
time2 = perf_counter()
print(f"Time: {time2 - time1} seconds without join")
# Time: 0.0006986249973124359 seconds without join
# This is not the time where execution should end ( approx 3 sec should be ans )
# here the main tread keep going forward - so it is not waiting for the tread to finish

# ------------------------
# Using join() to wait for threads to finish
# ------------------------

# join() :- t1.join(), this line will wait until t1 tread finish

t1 = threading.Thread(target=print_numbers, args=[1])
t2 = threading.Thread(target=print_numbers, args=[2])
t3 = threading.Thread(target=print_numbers, args=[3])

time1 = perf_counter()
t3.start()
t2.start()
t1.start()

t1.join()
t2.join()
t3.join()
time2 = perf_counter()
print(f"Time: {time2 - time1} seconds with join")
# Time: 3.00485687499895 seconds with join

# Most use to download from internet,
# If i want to download 5 file , i will not choose to download 1 by 1 , i want to all file download parallely

# ========================
# Some Theoretical knowledge
# ========================

"""
Thread States (we will learn deeply later)
    - New → Thread created but not started
    - Runnable → Thread started, waiting for CPU
    - Running → Thread currently executing
    - Waiting/Blocked → Waiting for resource or sleep
    - Terminated → Finished execution
    
Next major topic in MultiThreading
    - Threading with Classes – Subclassing Thread
    - Daemon Threads – Background threads that exit with the main program
    - Locks and Synchronization – Prevent race conditions
    - Thread-safe Queues – Communication between threads
    - Practical examples – File downloads, web scraping, producer-consumer
"""
