"""
Functions with variable positional arguments
and
Functions with variable keyword arguments
"""

print("Functions with variable positional arguments")
print("-"*20)
# --------------


def add(*a):
    print("Value of a is:", a)
    return sum(a)

add_result_1 = add()
print("add_result_1:", add_result_1, end="\n\n")

add_result_2 = add(10)
print("add_result_2:", add_result_2, end="\n\n")

add_result_3 = add(10, 20, 30, 40, 50, 60)
print("add_result_3:", add_result_3, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Functions with variable keyword arguments")
print("-"*20)
# --------------


def employee_profile_function(**a):
    print("Employee Details:", a, end="\n\n")


employee_profile_function()
employee_profile_function(name="emp-1")
employee_profile_function(name="emp-2", company="comp-2")
employee_profile_function(name="emp-3", company="comp-3", mobile="111111111")

print("#"*40, end="\n\n")
################################

