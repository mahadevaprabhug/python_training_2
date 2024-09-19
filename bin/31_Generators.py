"""
Generators: We can create objects whenever we need the value/object
instead of storing in some collection like list/tuple etc.
- In short, we can create objects on the fly
"""
print("WITHOUT using generator")
print("-"*20)
# --------------


def my_square_function(my_list):
    squared_my_list = []
    for i in my_list:
        squared_my_list.append(i*i)
    return squared_my_list


L = [10, 20, 30, 40]
squared_list = my_square_function(L)

for j in squared_list:
    print("Square:", j)

# ASSUME our final requirement is to
#   "print each squared value"


print("#"*40, end="\n\n")
################################

# About above requirement
# --------------
# - requirement is to print square of each value
# - one value at a time needed
# - BUT, currently 1st we are squaring all the values and keeping
#   in list : which occupies some memory.
#
# Requirement: Instead of keeping squared values in list
#   IF any option to provide ONE squared value when we request
#   then we can save memory
################################

print("Using Generator")
print("-"*20)
# --------------


def generator_my_square_function(my_list):
    for i in my_list:
        yield i * i

L = [10, 20, 30, 40]
generator_object = generator_my_square_function(L)

for j in generator_object:
    print("Square:", j)

# One time use

print("#"*40, end="\n\n")
################################
