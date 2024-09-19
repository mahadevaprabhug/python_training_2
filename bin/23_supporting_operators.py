"""
Implementing __ methods for

1) supporting initialization
2) supporting operators
3) supporting some builtin function
4) supporting iteration

In python, for each operator, few functions there is a special name given

Example:
    for + = __add__
    for len() = __len__

If we want to support for + then we need write __add__ method in our class
"""

print("Supporting + operator")
print("-"*20)
# --------------

class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        result = self.name + other.name
        return result


e1 = Employee("emp-1")
e2 = Employee("emp-2")

# Requirement: If we add 2 employee objects then
# it should concatinated name
concat_result = e1 + e2  # e1.__add__(e2)
print("concat_result:", concat_result)

print("#"*40, end="\n\n")
################################

print("Supporting len() operator")
print("-"*20)
# --------------

# --------------
# When we create objects 2 methods will execute
# 1) __new__ : Constructor
# 2) __init__ : Initializer

class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        result = self.name + other.name
        return result

    def __len__(self): # self=e1
        length = len(self.name)
        return length


e1 = Employee("emp-1")
e2 = Employee("emp-2")

concat_result = e1 + e2
print("concat_result:", concat_result, end="\n\n")

# Requirement: len() should return length of name
print("Length of e1:", len(e1)) # e1.__len__()


print("#"*40, end="\n\n")
################################

print("Supporting iteration")
print("-"*20)
# --------------


class Employee:
    def __init__(self, name):
        self.name = name

    def __add__(self, other): # self=e1, other=e2
        result = self.name + other.name
        return result

    def __len__(self): # self=e1
        length = len(self.name)
        return length

    def __iter__(self): # 1 time & 1st Time & Before starting the iteration
        self.index_no = 0
        return self

    def __next__(self): # Every iteration it will execute, This will return value
        current_index = self.index_no

        if current_index < len(self.name):
            self.index_no = self.index_no + 1
            return self.name[current_index]
        else:
            raise StopIteration # Given in documentation, This is procedure


e1 = Employee("emp-1")
e2 = Employee("emp-2")

concat_result = e1 + e2
print("concat_result:", concat_result, end="\n\n")

# Requirement: len() should return length of name
print("Length of e1:", len(e1)) # e1.__len__()

for i in e1:
    print("Value of i:", i)

for i in e2:
    print("Value of i:", i)

# Expected Output:
# e
# m
# p
# -
# 1

print("e1 In list, ", list(e1))

print("#"*40, end="\n\n")
################################



