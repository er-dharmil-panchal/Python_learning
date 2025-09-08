"""
 📌 Threading with Class (Sub-class Thread)
        - Each thread may need its own data
        - You may want methods tied to the thread’s job
        - Cleaner, object-oriented code
"""

import threading, time


class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()  # Initialize parent Thread class
        self.n = n  # Store thread-specific data
        self.result = None

    def run(self):  # Override run()
        print(f"Thread {self.n} starting")
        time.sleep(1)
        print(f"Thread {self.n} finished\n")
        self.result = self.n * self.n


# NOTE:
# __init__() → lets you pass data to the thread
# run() → code here runs when you call start()

threads = [MyThread(i) for i in range(5)]
# OR threads = MyThread(10)

for n in threads:
    n.start()
for t in threads:
    t.join()

print([t.result for t in threads])


# run() doesn’t return directly, so we store results inside the object.


# ==============================
# Example – Download Simulation
# ==============================

class DownloadFiles(threading.Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        print(f"Downloading {self.filename}...")
        time.sleep(2)
        print(f"Finished {self.filename}")


files = ["file1.zip", "file2.zip", "file3.zip", "file4.zip"]

threads = [DownloadFiles(f) for f in files]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("All downloads completed ✅")

"""
👉🏻 When to Use Class-Based Threads?
    - When tasks are complex (need state, return values, multiple methods)
    - When you want to encapsulate thread logic cleanly
    - In real-world apps like web crawlers, downloaders, worker pools
"""

"""
 📌 Daemon Threads
        - Daemon threads are important for background tasks that shouldn’t block your main program.
        
    What is a Daemon Thread?
        - A daemon thread runs in the background.
        - When the main thread finishes, daemon threads are killed automatically.
        - Opposite: non-daemon (normal) threads → program waits until they finish.
"""


# ==============================
# Normal (Non-Daemon) Thread
# ==============================

def backgroundTask():
    for i in range(5):
        print("Background task running...", i)
        time.sleep(1)


t = threading.Thread(target=backgroundTask)
t.start()
t.join()


# ==============================
# Daemon Thread
# ==============================

# def background_task():
#     for i in range(5):
#         print("Background task running...(With Daemon)", i)
#         time.sleep(1)
# t = threading.Thread(target=background_task, daemon=True)
# t.start()
# print("Main thread finished")
# 👉 The daemon thread is killed instantly when the main program exits.

# Output:
# Background task running... 0
# Main thread finished


# ==============================
# Mixed (Daemon + Non-Daemon)
# ==============================

def daemon_task():
    while True:
        print("Daemon working...")
        time.sleep(1)


def normal_task():
    for i in range(3):
        print("Normal task running", i)
        time.sleep(1)


t1 = threading.Thread(target=daemon_task, daemon=True)
t2 = threading.Thread(target=normal_task)

t1.start()
t2.start()

t2.join()
print("Main thread done ✅")

# Daemon keeps printing in background.
# But as soon as main + normal thread finish, program exits → daemon is killed.

# Output:
# Daemon working...
# Normal task running 0
# Normal task running 1
# Daemon working...
# Normal task running 2
# Daemon working...
# Main thread done ✅


# ==============================
# Checking Daemon Threads
# ==============================

"""
Python gives 2 ways:
    - Property access → t.daemon 
    - Method → t.isDaemon() (older style, same thing internally)
"""

# In Python 3.10+, isDaemon() is deprecated
# print(t1.isDaemon())
# print(t2.isDaemon())
# DeprecationWarning: isDaemon() is deprecated, get the daemon attribute instead

print(t1.daemon)  # True
print(t2.daemon)  # False

"""
IMPORTANT: When to Use Daemon Threads?
    ✔ Logging
    ✔ Monitoring (CPU usage, heartbeats, cleanup)
    ✔ Background auto-save
    ❌ Not for tasks where results matter (they may die before finishing).
"""

"""
 📌 Locks & Synchronization 
"""

# ==============================
# The Problem: Race Condition
# ==============================
# When 2 or more threads try to access the same data at the same time,
# results can become inconsistent.

x = 0  # Shared data


def balance():
    global x
    for _ in range(1000000):
        tmp = x
        time.sleep(0.000001)  # force context switch
        x = tmp + 1  # Not atomic (read + modify + write)


threads = [threading.Thread(target=balance) for _ in range(50)]
# In CPython (default Python), only one thread executes Python bytecode at a time (because of the GIL).
# So even though multiple threads exist, the GIL forces them to run one after another (not truly parallel on CPU).

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Final value of x:", x)

# Expected result = 50 * 1,000,000 = 50,000,000
# 👉 Actual result = ❌ Random number less than 50,000,000 (race condition).
# Example:
# Thread1 reads x = 10
# Thread2 also reads x = 10
# Both write back x = 11 (instead of 12).


# ==============================
# Fix by Lock
# ==============================
# Only one thread at a time can enter this block of code.

x = 0
lock = threading.Lock()


def increment():
    global x
    for _ in range(1000000):
        with lock:  # lock.acquire() + lock.release()
            x += 1


t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final value of x:", x)

# Instead of "with lock:", we can do it manually:
# lock.acquire()
# try:
#     x += 1
# finally:
#     lock.release()


# ==============================
# RLock (Reentrant Lock)
# ==============================
lock1 = threading.RLock()


# Problem: what if the same thread needs the lock multiple times?
# Normal Lock → will deadlock.
# Use RLock instead.

def task():
    with lock1:
        print("First lock acquired")
        with lock1:  # same thread can re-acquire safely
            print("Second lock acquired")


t = threading.Thread(target=task)
t.start()
t.join()

# ==============================
# Semaphore (Limit Access)
# ==============================
# Lock = only 1 thread inside.
# Semaphore(n) = allows n threads inside at once.

sem = threading.Semaphore(2)  # only 2 threads running at a time, others wait.


def worker(name):
    with sem:
        print(f"{name} got access")
        time.sleep(2)
        print(f"{name} released")


for i in range(5):
    threading.Thread(target=worker, args=(f"Thread-{i}",)).start()

# ==============================
# Condition (Wait/Notify)
# ==============================
# Sometimes threads need to wait for a signal.
# Use Condition → e.g. Producer-Consumer Problem.
# Consumer waits until the producer produces the item.

condition = threading.Condition()
data_ready = False


def producer():
    global data_ready
    with condition:
        print("Producing data...")
        data_ready = True
        condition.notify()  # wake up waiting thread


def consumer():
    with condition:
        while not data_ready:
            condition.wait()  # wait until notify
        print("Consumed data!")


t1 = threading.Thread(target=consumer)
t2 = threading.Thread(target=producer)

t1.start()
t2.start()
t1.join()
t2.join()

"""
 📌 Deadlocks
⚠️ If two threads lock resources in opposite order → deadlock.

Example:
    Thread1 → locks A → waits for B
    Thread2 → locks B → waits for A
    Both stuck forever.

👉 Fix:
    - Always lock resources in a consistent order.
    - Use timeout in lock.acquire(timeout=...).
"""


"""
==========================================
📌 SUMMARY – Python Threading Concepts
==========================================

1. Threading with Class
   - Create custom threads by subclassing `threading.Thread`.
   - Override `__init__` to pass data and `run()` to define logic.
   - Store results as object attributes since `run()` cannot return values.

2. Daemon Threads
   - Run in background, killed automatically when main program exits.
   - Normal (non-daemon) threads → block main thread until finished.
   - Use `.daemon` property to check (instead of deprecated `.isDaemon()`).
   - Use daemon only for background tasks (logging, monitoring, autosave).

3. Locks & Synchronization
   - Race condition occurs when multiple threads access shared data.
   - `Lock()` ensures only one thread modifies data at a time.
   - `with lock:` is safer than manual `acquire()`/`release()`.

4. RLock (Reentrant Lock)
   - Allows the same thread to acquire the lock multiple times.
   - Prevents deadlock when recursive locking is needed.

5. Semaphore
   - Controls how many threads can access a resource at the same time.
   - Example: `Semaphore(2)` → max 2 threads inside critical section.

6. Condition
   - Used for signaling between threads.
   - Example: Producer/Consumer problem → consumer waits until producer notifies.

7. Deadlocks
   - Occur if threads wait on each other forever (circular locking).
   - Fix by:
       - Locking resources in consistent order.
       - Using timeout in `lock.acquire(timeout=...)`.

✅ Key Takeaways
   - Use class-based threads for complex jobs needing state.
   - Use daemon threads only for background, non-essential tasks.
   - Always use locks (or higher-level constructs) for shared data.
   - Avoid deadlocks by careful lock ordering or timeouts.
"""
