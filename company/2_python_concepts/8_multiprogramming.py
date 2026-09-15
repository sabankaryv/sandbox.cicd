"""
                 CONCURRENCY
                     │
          ┌──────────┴──────────┐
          │                     │
    Multithreading          Async I/O
          │                     │
      Threads              Event Loop
          │                     │
      I/O tasks             Coroutines
                                │
                           async / await


                 PARALLELISM
                     │
               Multiprocessing
                     │
                 Processes
                     │
                CPU Cores

1.Process:=
== A process is a program that is currently running.
== a running instance of a program with its own memory and resources.

For example, when you run:

python app.py

your operating system creates a process to run app.py.

Think of it like this
Program (file)
     ↓
   Run it
     ↓
Process
     ↓
CPU + Memory + Resources

A process has its own memory space:

Process 1
 ├── Code
 ├── Variables
 ├── Stack
 ├── Heap
 └── Resources

Process 2
 ├── Code
 ├── Variables
 ├── Stack
 ├── Heap
 └── Resources

So Process 1 and Process 2 are generally isolated from each other.

Process vs Thread

This is very important for your next topic:

PROCESS
   │
   ├── Thread 1
   ├── Thread 2
   └── Thread 3

A process can contain multiple threads.

| Process                 | Thread                        |
| ----------------------- | ----------------------------- |
| Running program         | Execution unit inside process |
| Has separate memory     | Shares process memory         |
| Heavyweight             | Lightweight                   |
| Communication is harder | Communication is easier       |
| `multiprocessing`       | `threading`                   |

"""
# 1.
import threading
import time

def task(name):
    print(f"Start the task: {name}")
    time.sleep(2)
    print(f"End The Task: {name}")


t1=threading.Thread(target=task,args=('yogesh',))
t2=threading.Thread(target=task,args=('rohit',))
"""
1.
t2=threading.Thread(target=task,args=('rohit',))
Python creates a Thread object.
Important: the thread has NOT started yet.

2.
t2.start()
Now you are telling Python:
Start t2 and schedule it for execution.
The operating system/runtime creates and schedules the new thread.

3.
t2.join()
Now:
t2.join()
means:
Main thread waits until t1 finishes.
It does not mean "start t1."

                 PROCESS
                    │
          ┌─────────┼─────────┐
          │         │         │
          ↓         ↓         ↓
       Main       Thread 1  Thread 2
       Thread        │         │
          │          ↓         ↓
          │      task("yogesh")
          │                task("rohit")
          │
          │
       t1.start()
          │
       t2.start()
          │
       t1.join()
          │
          ├──── WAIT until t1 finishes
          │
       t2.join()
          │
          ├──── WAIT until t2 finishes
          │
          ↓
       Program continues
Thread() creates a thread object but doesn't start it.
start() schedules the thread for execution, causing the target function to run in that thread.start() creates and starts a new thread, and that new thread internally executes the thread's run() method, which ultimately calls the target function.
join() blocks the calling thread until the specified thread completes.


3.Thread LifeCycle:=
==================
             Thread()
                ↓
             CREATED
                ↓
             start()
                ↓
       RUNNABLE / RUNNING
          ↙          ↘
      WAITING      RUNNING
          ↘          ↙
             RUNNING
                ↓
          target() ends
                ↓
           TERMINATED
Point-to-point:

Created → Thread object is created using Thread().
Started → start() is called to start the thread.
Running → The thread executes the target function.
Waiting/Blocked → It may temporarily wait for I/O, a lock, another thread, etc.
Terminated → The target function finishes and the thread ends.
"""


t1.start()
t2.start()

t1.join()
t2.join()
print("All The Task Completed")


# 2nd Example
def fun1():
   print(f"I am From Function 1 and executed by:{threading.current_thread().name}")
def fun2():
   print(f"I am From Function 2 and executed by:{threading.current_thread().name}")
def fun3():
   print(f"I am From Function 3 and executed by:{threading.current_thread().name}")
def fun4():
   print(f"I am From Function 4 and executed by:{threading.current_thread().name}")



#main Programm
print("*"*50)
print("Main Programm Execution Started...")
thread_name=threading.current_thread().name
print(f"Name Of the main thread in the main programm:{thread_name}")
fun1()
print("Main Thread Came to function 1 to complete the execution of function 1")
fun2()
print("Main Thread Came to function 2 to complete the execution of function 2")
fun3()
print("Main Thread Came to function 3 to complete the execution of function 3")
fun2()
print("Main Thread Came to function 4 to complete the execution of function 4")
print("Programm Execution Completed:")

# # 3.Third Example
# import time
# def squares(lst):
#    print(f"Name Of The Thread to came to complete the execution of the square function:{threading.current_thread().name}")
#    for i in lst:
#       print("square({})={}".format(i,i**2))
#       time.sleep(2)

# def cubes(lst):
#    print(f"Name Of The Thread to came to complete the execution of the cubes function:{threading.current_thread().name}")
#    for i in lst:
#       print("cubes ({})={}".format(i,i**3))
#       time.sleep(2)

# #Main Programm
# print("="*50)
# start_time=time.time()
# print(start_time)
# lst1=[1,2,3,4,5]
# squares(lst1)
# cubes(lst1)
# end_time=time.time()
# end_time=end_time-start_time
# print(f"Programm Completed in {end_time} time")
# print("="*50)

# 4.Fourth Example using threading
import time
def squares(lst):
   print(f"Name Of The Thread to came to complete the execution of the square function:{threading.current_thread().name}")
   for i in lst:
      print("square({})={}".format(i,i**2))
      time.sleep(2)

def cubes(lst):
   print(f"Name Of The Thread to came to complete the execution of the cubes function:{threading.current_thread().name}")
   for i in lst:
      print("cubes ({})={}".format(i,i**3))
      time.sleep(2)

#Main Programm
print("="*50)
start_time=time.time()
print(start_time)
lst1=[1,2,3,4,5]
t1=threading.Thread(target=squares,args=(lst1,))
t2=threading.Thread(target=cubes,args=(lst1,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time=time.time()
end_time=end_time-start_time
print(f"Thread Based Programm Completed in {end_time} time")
print("="*50)


