"""
for-loop: Iterate any collection
"""

print("for-loop to iterate string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Value of i is:", i)

print("#"*40, end="\n\n")
################################

print("'for-loop' with list/tuple/any other collections")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')

for i in my_list:
    print("Value of i is:", i)

print("#"*40, end="\n\n")
################################

print("'for-loop' with dictionary")
print("-"*20)
# --------------

my_dictionary = {"course": "python", "duration": 10, "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Iterating Keys")
# -------------
# >>> my_dictionary.keys()
# ['course', 'duration', 'mode']
for each_key in my_dictionary.keys():
    print("Each Key:", each_key)
    print("Value:", my_dictionary[each_key])

print("\n\n")
########################

print("iterating Values()")
# >>> my_dictionary.values()
# ['python', 10, 'online']
# -------------
for each_value in my_dictionary.values():
    print("Each Value:", each_value)

print("\n\n")
########################

print("Iterating Items()")
# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
for each_item in my_dictionary.items():
    print('Each Item:', each_item)
    print("Key:", each_item[0])
    print("Value:", each_item[1])
print("\n\n")
########################

print("Iterating Items()")
# >>> my_dictionary.items()
# [('course', 'python'), ('duration', 10), ('mode', 'online')]
for each_key, each_value in my_dictionary.items():
    print("Key:", each_key)
    print("Value:", each_value)

print("\n\n")
########################

print("#"*40, end="\n\n")
################################

# 2 Cases
# Case-1: 'break': How to end for-loop in between
# Case-2: 'continue': How to skip iteration in between

print("# Case-1: 'break': How to end for-loop in between")
print("-"*20)
# --------------

# Requirement: Check any value startswith 'Java'

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')


for each_course in my_list:
    if each_course.startswith("Java"):
        print("Course 'Java' Found")
        break


print("#"*40, end="\n\n")
################################

print("# Case-2: 'continue': How to skip iteration in between")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')


for each_course in my_list:
    if not each_course.startswith("Java"):
        continue

    # Below code is applicable only for java course
    print("This Java Course Name Is:", each_course)
    print("This is one version of Java")
    print("This Java course duration is 10 days", end="\n\n")


print("#"*40, end="\n\n")
################################

print("for-else block")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')


for each_course in my_list:
    print("Course:", each_course)
else:
    print("Reached for-else block")
    print("This block will execute after completing for-loop")
    print("if we are ending 'for-loop' using 'break' then 'else' block will not execute")
    del my_list

print("#"*40, end="\n\n")
################################
