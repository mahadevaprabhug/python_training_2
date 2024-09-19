"""
Conditional Statement 'if': Based on the condition we can execute block of code
"""
print("Only 'if' block")
print("-"*20)
# --------------

x = 10

if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

if x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

if x < 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
################################


print("'if-elif' block")
print("-"*20)
# --------------

x = 10

if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

elif x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

elif x < 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
################################

print("'if-elif-else' block")
print("-"*20)
# --------------

x = 10

if x == 10:
    print("Value of x is equal to 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

elif x > 10:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

else:
    print("Value of x is greater than 10")
    print("Value of x is greater than 0")
    print("Value of x is less than 100")

print("#"*40, end="\n\n")
################################


print("'if' with strings")
print("-"*20)
# --------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

if ("th" in my_string) and ('on' in my_string):
    print("sub string found")

if my_string.startswith("Pyt"):
    print("String is Starting 'pyt'")

if (my_string != "Java") and (my_string != "C++"):
    print("Not C++/Java")

print("#"*40, end="\n\n")
################################


print("'if' with list/tuple/any other collections")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')

if "Java-1" in my_list:
    print("Exact Value 'Java-1' found")

print("#"*40, end="\n\n")
################################

print("'if' with dictionary")
print("-"*20)
# --------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
if 'course' in my_dictionary.keys():
    print("Key 'course' found")

# >>> my_dictionary.values()
# ['python', 10, 'online']
if 'python' in my_dictionary.values():
    print("Value 'python' found")

# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
if ('mode', 'online') in my_dictionary.items():
    print("Item ('mode', 'online') found")

print("#"*40, end="\n\n")
################################
