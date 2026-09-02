"""
1. Shallow Copy
================
==> Copies the outer object, but inner/nested objects are still shared.
==> Creates a new outer object, but nested/mutable objects inside it are shared.
==> The memory address of the outer object is different, but inner objects
    refer to the same objects.
==> Changes made to shared inner objects are reflected in both
    the original and copied objects.
2. Deep Copy
=============
==> Creates a new outer object as well as new inner/nested objects.
==> Creates a completely independent copy of the original object.
==> Changes made to nested objects in the copied object do not
    affect the original object.
"""

import copy
from copy import deepcopy
a=[[1,2],[3,4]]
print(a[0]) #[1, 2]
print(a[0][0]) #1
print(a[0][1])#2
# 1.Shallow Copy
b=copy.copy(a)

print(a,id(a))  #Outer Objects Having different memeory address
print(b,id(b))  #Outer Objects Having different memeory address

print(a[0],id(a[0]))    # but Inner Objects Having the same memory address
print(b[0],id(b[0]))    # but Inner Objects Having the same memory address

a[0].append([10,20])
print("we appended in object a :",a)    # we appended in object a : [[1, 2, [10, 20]], [3, 4]]
print("we appended in object a but also updated in object b as well: ",b)   # we appended in object a but also updated in object b as well:  [[1, 2, [10, 20]], [3, 4]]

# 2.Deep Copy
c=[[100,200],[300,400]]
d=deepcopy(c)
print(c,id(c))
print(d,id(d))
print(c[0],id(c[0]))    #2230066453120
print(d[0],id(d[0]))    #2230066453376
# Above both are completely independent object using deep copy

