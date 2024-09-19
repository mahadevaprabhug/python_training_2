"""
Variable Scopes
1. Local scope
2. Enclosed scope
3. Global scope
4. builtin scope
"""

print("1. Local scope")
print("-"*20)
# --------------

def my_function():
    a = 10 # Local Scope, Within the function we can access
    print("Value of a is:", a)

my_function()

print("#"*40, end="\n\n")
################################


print("2. Enclosed scope")
print("-"*20)
# --------------

def my_function_1():
    a = 10 # Enclosed Scope: current & nested functions can access
    def my_function_2():
        print("Accessing outer function variable:", a)
    my_function_2()

my_function_1()

print("#"*40, end="\n\n")
################################

print("3. Enclosed scope")
print("-"*20)
# --------------
x = 10 # Global Variable
def my_function_1():
    print("In my_function_1 x is:", x)
    def my_function_2():
        print("In my_function2 x is:", x)
    my_function_2()
print("Outside of all functions, x is:", x)

my_function_1()

print("#"*40, end="\n\n")
################################

# How search happens?
# 1st check in local scope
# if not there
# then
# check in enclosed scope
# if not there
# then
# check in global scope
# if not there
# then
# check in builtins