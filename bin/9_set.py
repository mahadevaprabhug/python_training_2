"""
set:
        -- We have option to store collection of values like list of name, list of email-ids etc.
        -- It will keep only UNIQUE VALUES
        -- NO index number to each value
        -- WE can convert to list/tuple to get index number
            OR
            We can iterate using loops
"""

print("set PART-1")
print("how to store the values")
print("-"*20)
# --------------

my_fs_1 = {10, 10, "python", "python"}
print(my_fs_1)

my_fs_1 = set([10, 10, "python", "python"])
print(my_fs_1)

print("#"*40, end="\n\n")
################################

print("set PART-2")
print("methods inside set class")
print("-"*20)
# --------------

print(dir(set))

print("#"*40, end="\n\n")
################################
