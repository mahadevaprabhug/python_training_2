"""
list:
        -- We have option to store collection of values like list of name, list of email-ids etc.
        -- It will keep DUPLICATE VALUES
        -- Automatically index number will be assigned to each value
"""

print("list PART-1")
print("how to store the values")
print("-"*20)
# --------------

my_list_1 = [10, 12.5, "python", "java", (100, 200)]
# Internally it will create object of builtin-class 'list' and store the values

# OR
my_list_2 = list((10, 12.5, "python", "java", (100, 200)))

print(my_list_1, my_list_2, sep="\n")

print("#"*40, end="\n\n")
################################

print("list PART-2")
print("Indexes: Indexes are similar to string")
print("-"*20)
# --------------

my_list = [10, 12.5, "python", "java", (100, 200)]
print("my_list:", my_list, end="\n\n")


print("Course Name:", my_list[2]) # "python"
print("2nd character in Course Name:", my_list[2][1], end="\n\n") # "y"

print("Inner list:", my_list[-1]) # (100, 200)
print("Last value in Inner list:", my_list[-1][-1], end="\n\n")

print("#"*40, end="\n\n")
################################


print("list PART-3")
print("Methods inside 'list' class")
print("-"*20)
# --------------

print(dir(list))

print("#"*40, end="\n\n")
################################
