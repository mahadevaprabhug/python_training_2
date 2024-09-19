"""
Tuple:
        -- We have option to store collection of values like list of name, list of email-ids etc.
        -- It will keep DUPLICATE VALUES
        -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("how to store the values")
print("-"*20)
# --------------

my_tuple_1 = (10, 12.5, "python", "java", (100, 200))
# Internally it will create object of builtin-class 'tuple' and store the values

# OR
my_tuple_2 = tuple((10, 12.5, "python", "java", (100, 200)))

print(my_tuple_1, my_tuple_2, sep="\n")

print("#"*40, end="\n\n")
################################

print("Tuple PART-2")
print("Indexes: Indexes are similar to string")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "java", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")


print("Course Name:", my_tuple[2]) # "python"
print("2nd character in Course Name:", my_tuple[2][1], end="\n\n") # "y"

print("Inner tuple:", my_tuple[-1]) # (100, 200)
print("Last value in Inner tuple:", my_tuple[-1][-1], end="\n\n")

print("#"*40, end="\n\n")
################################


print("Tuple PART-3")
print("Methods inside 'tuple' class")
print("-"*20)
# --------------

print(dir(tuple))

print("#"*40, end="\n\n")
################################
