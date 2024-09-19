"""
PACKAGES: If we are developing more and more modules then
we can keep/organize in folders/sub-folders.
these folders are called PACKAGES

In this program, we are importing from 'mypackage' library
"""

print("1-Way of importing library")
print("-"*20)
# --------------

import mypackage.db.mymodule

print("Course Name:", mypackage.db.mymodule.course)

add_result = mypackage.db.mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mypackage.db.mymodule.Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
################################

print("2-Way of importing library")
print("-"*20)
# --------------

import mypackage.db.mymodule as mm

print("Course Name:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
################################

print("3-Way of importing library")
print("-"*20)
# --------------

from mypackage.db.mymodule import course, add, Employee

print("Course Name:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
################################

print("4-Way of importing library")
print("-"*20)
# --------------

from mypackage.db.mymodule import course as c, add as a, Employee as E

print("Course Name:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E()
e1.add_name("emp-1")
print("Name:", e1.get_name())

print("#"*40, end="\n\n")
################################
