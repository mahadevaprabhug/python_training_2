"""
Numbers:
    -- We have option to store numbers like int, float etc
"""

print("Numbers Example")
print("How to store numbers?")
# print("-------------")
# OR
print("-"*20)
# -------------

a = 10
# Internally, It will create object of builtin class 'int' and store the value

# We can also store like this
b = int(10) # Same as b = 10

print(a, b)

print("#"*40, end="\n\n")
#############################

print("How numbers are IMMUTABLE")
print("-"*20)
# -------------

a = 10
print("Value of 'a':", a)
print("Ref ID of 'a':", id(a))

a = 100
print("Value of 'a':", a)
print("Ref ID of 'a':", id(a))

print("#"*40, end="\n\n")
#############################
