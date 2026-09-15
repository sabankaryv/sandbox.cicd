import time,threading
# print("1.First Programm")
# print("**"*100)
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
# t1=threading.Thread(target=squares,args=(lst1,))
# t2=threading.Thread(target=cubes,args=(lst1,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end_time=time.time()
# end_time=end_time-start_time
# print(f"Thread Based Programm Completed in {end_time} time")
# print("="*50)
# print("**"*100)

# 2nd Example:

# class MultiThreadingClassBased:
#    def __init__(self):
#       self.result=None
#       self.vowels=0
#       self.consonent=0
   
#    def ReverseString(self,string1):
#       print("*"*50 +" 1.ReverseString "+"*"*50)
#       temp=""
#       print(f"{threading.current_thread().name} is Executing The Reverse Function")
#       for ch in string1:
#           temp=ch+temp
#       self.result=temp
#       print(self.result)

#    def Palindrome(self,string1):
#       print("*"*50 +" 2.Palindrome "+"*"*50)
#       print(f"{threading.current_thread().name} is Executing The Palindrome Function")
#       temp=""
#       string1=string1.lower()
#       for ch in string1:
#          temp=ch+temp
#       if temp==string1:
#          print("Entered String is Palindrome: ")
#       else:
#          print("Entered String is Not Palindrome: ")

#    def VowelsOrConsonentCount(self,string1):
#       print("*"*50 +" 3.VowelsOrConsonentCount "+"*"*50)
#       print(f"{threading.current_thread().name} is Executing The Palindrome Function")
#       for ch in string1:
#          if ch in "aeiou":
#             self.vowels+=1
#          else:
#             self.consonent+=1
#       print(f"The Vowels Count is {self.vowels} And The Consonent Count is {self.consonent}")

#    def inputdata(self):
#            input_string=input("Enter Your String to Reverse: ")
#            return input_string

# m1=MultiThreadingClassBased()
# input_data=m1.inputdata()
# # Threading
# t1=threading.Thread(target=m1.ReverseString,args=(input_data,))
# t2=threading.Thread(target=m1.Palindrome,args=(input_data,))
# t3=threading.Thread(target=m1.VowelsOrConsonentCount,args=(input_data,))
# t1.start()
# print(f"Check Is Thread 1 is Alive:{t1.is_alive()}")
# t2.start()
# print(f"Check Is Thread 2 is Alive:{t2.is_alive()}")
# t3.start()
# print(f"Check Is Thread 3 is Alive:{t3.is_alive()}")
# t1.join()
# t2.join()
# t3.join()
# main_thread=threading.current_thread()
# print(f"Check Is Main Thread  is Alive:{main_thread.is_alive()}")
# print(f"check is ident:{threading.current_thread().ident}") #ident is used to uniquely identify a thread within the Python process.
# print(f"check is native_id:{threading.current_thread().native_id}") #native_id is used to Gets OS-level thread ID
# print(f"check is daemon:{threading.current_thread().daemon}") #Gets/sets daemon status
# print(f"The Reversed String is {m1.result}")



# 3.Daemon Thread:=

# import threading,time


# def task():
#    for i in range(5):
#       print(f"Worker: {i}")
#       time.sleep(2)
# t1=threading.Thread(target=task)
# # t1.daemon=True
# t1.start()
# # t1.join()
# print("Main Thread Completed: ")


# 4.Shared Resource:=Shared resources are data or objects that multiple threads can access or modify at the same time.
# If multiple threads modify the same shared data at the same time, the result may become incorrect.
# A shared resource is data or an object that can be accessed by multiple threads within the same process.
# Race Condition → when multiple threads access/modify shared data at the same time and the result depends on the timing/order of execution.

import threading

balance = 1000

def withdraw():
    global balance
    balance = balance - 500

t1 = threading.Thread(target=withdraw)
t2 = threading.Thread(target=withdraw)
t3 = threading.Thread(target=withdraw)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print(balance)

# 5.Thread Safety 🔥
# Thread safety means making sure shared data remains correct when multiple threads access it at the same time.
"""
Thread 1 ──→ Shared Data ←── Thread 2
                  ↓
            Race Condition

If both threads modify the same data simultaneously, the result can be wrong.
We use synchronization techniques to control access:

Thread Safety
     ↓
Synchronization
     ↓
Lock / RLock / Semaphore / etc.
"""
