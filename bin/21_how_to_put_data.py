"""
How to put data?

In this section:
1. CLASS Variables
2. INSTANCE Variables
"""

print("Creating objects")
print("-"*20)
# --------------

class Employee:
    pass


e1 = Employee()
e2 = Employee()

# Total 3 objects: 1) Employee 2) e1 3) e2
print("#"*40, end="\n\n")
################################


print("Store the data")
print("-"*20)
# --------------

Employee.company_name= "XYZ Company"
# Internally it create new variable 'company_name' inside 'Employee' object
# and store the value
e1.name = "emp-1"
# Internally it create new variable 'name' inside 'e1' object
# and store the value
e2.name = "emp-2"
# Internally it create new variable 'name' inside 'e2' object
# and store the value

print("#"*40, end="\n\n")
################################

print("DATA present in BRADNEW objects")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee.company_name)
print("DATA present inside instance object 'e1':", e1.name)
print("DATA present inside instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
################################
