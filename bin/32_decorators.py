"""
Decorators:
- it is design pattern
- Using this, we can write a function to keep common functionality
    which we need to use it in other functions
"""

print("Without using decorator")
print("-"*20)
# --------------


def add(a, b):
    print("Result is :")
    print(a+b)
    print("End of the result", end="\n\n")


def sub(a, b):
    print("Result is :")
    print(a-b)
    print("End of the result", end="\n\n")

add(10, 20)
sub(10, 20)

print("#"*40, end="\n\n")
################################

print("Using decorator: PARTIAL IMPLEMENTATION")
print("-"*20)
# --------------


def my_decorator(my_func): # my_func=sub
    def decorated_func(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # sub(10,20)
        print("End of result", end="\n\n")
    return decorated_func


def add(a, b):
    print(a - b)

received_function = my_decorator(add)
# received_function = decorated_func
received_function(10, 20)


def sub(a, b):
    print(a - b)

received_function = my_decorator(sub)
# received_function = decorated_func
received_function(10, 20)

print("#"*40, end="\n\n")
################################

print("Using decorator: FINAL")
print("-"*20)
# --------------


def my_decorator(my_func): # my_func=sub
    def decorated_func(x, y): # x=10, y=20
        print("Result is:")
        my_func(x, y) # sub(10,20)
        print("End of result", end="\n\n")
    return decorated_func


@my_decorator
def add(a, b):
    print(a - b)

add(10, 20)

# @my_decorator will take care of executing below 2 steps
# received_function = my_decorator(add)
# received_function(10, 20)

@my_decorator
def sub(a, b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of executing below 2 steps
# received_function = my_decorator(sub)
# received_function(10, 20)

print("#"*40, end="\n\n")
################################
