"""
How to get or create objects
- Answer: using class, we can create n number objects

In this section:
1. CLASS OBJECT
2. INSTANCE OBJECT
"""

print("Creating objects")
print("-"*20)
# --------------


class Employee:
    pass

# 'pass': Use dummy keyword 'pass' to keep any block empty like if-block, for-block etc
# here, eventhough it is empty class, it is complete class, valid class, which means using this class we can create objects

# Create object
e1 = Employee()
e2 = Employee()

# Total 3 objects we have here
# 1. CLASS OBJECT: 'Employee' which is automatically getting created with class name
# 2. INSTANCE OBJECTS: 'e1' & 'e2' which we create

print("#"*40, end="\n\n")
################################

print("DATA present in BRADNEW objects")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee)
print("DATA present inside instance object 'e1':", e1)
print("DATA present inside instance object 'e2':", e2)

print("#"*40, end="\n\n")
################################

print("METHODS/VARIABLES present in BRADNEW objects")
print("-"*20)
# --------------

print("METHODS/VARIABLES present inside class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present inside instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################

# About 'object' class
# - super class
# - it has many methods including __new__ & __init__ which will create object
# - by default 'object' will be linked to all our classes
#   also everything in 'object' class will be available in
#   our class: INHERITANCE
