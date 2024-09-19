"""
Functions: If we want to rewrite/copy-paste same code more than one time
then instead of rewrite/copy-paste, we can keep that code in a block
and reuse it.
"""
print("WITHOUT using function")
print("-"*20)
# --------------

a = 10
b = 20
c = a + b
print("value of c:", c)

a = 10
b = 20
c = a + b
print("value of c:", c)

a = 10
b = 20
c = a + b
print("value of c:", c)

a = 10
b = 20
c = a + b
print("value of c:", c)

print("#"*40, end="\n\n")
################################

print("Using function")
print("-"*20)
# --------------

# Function Definition
def my_func():
    a = 10
    b = 20
    c = a + b
    print("value of c:", c)


# Function call
my_func()
my_func()
my_func()
my_func()

print("#"*40, end="\n\n")
################################
