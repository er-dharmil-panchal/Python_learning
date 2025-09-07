"""
 📌 Multi-Threading (Some more methods)
"""

import threading
import time


# ========================
# Current Thread Information
# ========================

# current_thread() gives the thread object representing the currently executing thread.
# threading.active_count() → Number of alive threads
# threading.current_thread() → Get currently running thread object
# threading.enumerate() → List all alive threads

def worker():
    print(f"Thread Name: {threading.current_thread().name}")
    time.sleep(2)


# Default thread name is Thread-1 if not specified
t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker, name="CustomName")  # Custom thread name

t1.start()
t2.start()

# Main thread info
print(f"Thread Name: {threading.current_thread().name}")  # Thread Name: MainThread
print(f"Active Threads: {threading.active_count()}")  # Active Threads: 3
print(f"All Threads: {threading.enumerate()}")
# [<_MainThread(MainThread, started 8774443200)>,
#  <Thread(Thread-1 (worker), started 6107000832)>,
#  <Thread(CustomName, started 6123827200)>]

t1.join()
t2.join()


# ========================
# MultiThreading with Loop
# ========================

def worker(num):
    print(f"Worker {num} starting")
    time.sleep(1)
    print(f"Worker {num} done")


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=([i]))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Worker 0 starting
# Worker 1 starting
# Worker 2 starting
# Worker 3 starting
# Worker 4 starting
# Worker 0 done
# Worker 1 done
# Worker 3 done
# Worker 2 done
# Worker 4 done

# Note:
# In most cases, starting of threads will be almost simultaneous,
# but the end of thread execution may vary, there is no fixed sequence.


# ========================
# Thread Return Values (Indirect)
# ========================

# Threads don’t return values directly, but you can store results in a shared list/dict

results = []


def compute_square(n):
    results.append(n * n)


threads = [threading.Thread(target=compute_square, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(results)
