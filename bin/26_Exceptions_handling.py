"""
Exception Handling:
"""

# print("Without handling Exception")
# print("-"*20)
# # --------------
#
# a = 10
# b = 0
# result = a / b # Program will terminate here abruptly
# print('result:', result)
#
# print("#"*40, end="\n\n")
# ################################

print("Handling Exception")
print("-"*20)
# --------------

# try:
#     pass
# except:
#     pass
# if try block fails then 'Except' block will execute
# if try block success then 'Except' block will be skipped

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate here, Instead control will be passed to 'except' block
    print('result:', result)
except:
    print("Reached 'except' block")
    print("if try block fails then 'Except' block will execute")
    print("if try block success then 'Except' block will be skipped")
    print("So finally, here we are writing logic to solve problem occurred in try")

print("#"*40, end="\n\n")
################################

print("Handling Exception using class names in 'except' block")
print("-"*20)
# --------------

# About exception classes
# --------------
# - We need to have classes for each exception type
# - We have few exception classes in builtins
# - apart from these builting classes, we need to write
#   our own classes for other exception types
# - When we are using libraries, libraries will provide exception classes
#   for the error occurs while using that library

try:
    a = 10
    b = 0
    result = a / b # Program will NOT terminate here, Instead control will be passed to 'except' block
    print('result:', result)
except ZeroDivisionError:
    print("It is ZDE Block")
except NameError as ne:
    print("It is NE Block and captured object:", ne)

print("#"*40, end="\n\n")
################################

print("try-except-else")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open("xyz.txt", "w")
except:
    print("Reached except block")
    print("Here handling only file open error")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
    my_file_handle.close()


# if 'try' block success then execute 'else' block and skip 'except' block
# if 'try' block failed then execute 'except' block and skip 'else' block
#
# So, we can say, 'else' block is continuation of 'try'

print("#"*40, end="\n\n")
################################

print("try-except-else-finally")
print("-"*20)
# --------------

try:
    print("Reached try block")
    my_file_handle = open("xyz.txt", "w")
except:
    print("Reached except block")
    print("Here handling only file open error")
else:
    print("Reached else block")
    my_file_handle.write("Hello")
finally:
    print("Reached finally block")
    try:
        my_file_handle.close()
        print("File handle closed")
    except:
        print("Not able to close file handle")

# if 'try' success/failed, finally will execute
# if 'except' success/failed, finally will execute
# if 'else' success/failed, finally will execute
#
# So, finally block will always execute

print("#"*40, end="\n\n")
################################

print("User defined exception class example - 1")
print("-"*20)
# --------------

# Mandatory Step: our class should be subclass of 'Exception' class
# OR if some classes are already subclass of 'Exception' then
# we can also extend those classes as well
# Example: Builtin exception classes are already extending 'Exception' class
#   so we can use any class to create our exception class


class MyError(Exception):
    pass
# It is valid Exception class, means, we can use this class to handle exception

try:
    x = 10

    if x == 10:
        raise MyError
        # raise ZeroDivisionError
    if x > 10:
        raise MyError

    if x < 10:
        raise MyError
except MyError:
    print("Reached Except Block. It is MyError")

print("#"*40, end="\n\n")
################################

print("User defined exception class example - 2")
print("-" * 20)
# --------------

# Requirement: Send some message while raising error

class MyError(Exception):
    def __init__(self, m):
        self.error_message = m


try:
    x = 10

    if x == 10:
        raise MyError("Here value of x is 10 so raising MyError")
        # raise ZeroDivisionError
    if x > 10:
        raise MyError("Here value of x is gt 10 so raising MyError")

    if x < 10:
        raise MyError("Here value of x is lt 10 so raising MyError")

except MyError as me:
    print("Reached Except Block. It is MyError and Details", me.error_message)

print("#" * 40, end="\n\n")
################################
