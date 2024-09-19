"""
while-loop: We can execute the loop based on the condition
"""
print("While loop example")
print("-"*20)
# --------------

i = 0
while i < 5:
    print("Value of i:", i)
    i = i + 1 # i += 1

print("#"*40, end="\n\n")
################################

print("Like DO-While loop example")
print("-"*20)
# --------------

i = 0
# while True:
while 1:
    print("Value of i:", i)
    i = i + 1 # i += 1
    if i > 5:
        break


print("#"*40, end="\n\n")
################################

# 2 Cases
# Case-1: 'break': How to end for-loop in between
# Case-2: 'continue': How to skip iteration in between

print("# Case-1: 'break': How to end while-loop in between")
print("-"*20)
# --------------

# Requirement: Check any value startswith 'Java'

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')

index_no = 0
while index_no < len(my_list):
    if my_list[index_no].startswith("Java"):
        print("Course 'Java' Found")
        break
    index_no += 1


# for each_course in my_list:
#     if each_course.startswith("Java"):
#         print("Course 'Java' Found")
#         break


print("#"*40, end="\n\n")
################################

print("# Case-2: 'continue': How to skip iteration in between")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')

index_no = 0
while index_no < len(my_list):
    if not my_list[index_no].startswith("Java"):
        index_no += 1
        continue

    # Below code is applicable only for java course
    print("This Java Course Name Is:", my_list[index_no])
    print("This is one version of Java")
    print("This Java course duration is 10 days", end="\n\n")
    index_no += 1


# for each_course in my_list:
#     if not each_course.startswith("Java"):
#         continue
#
#     # Below code is applicable only for java course
#     print("This Java Course Name Is:", each_course)
#     print("This is one version of Java")
#     print("This Java course duration is 10 days", end="\n\n")


# Example: Convert to other type
# my_set_1 = set(my_list)
# my_list_2 = list(my_set_1)

print("#"*40, end="\n\n")
################################


print("while-else block")
print("-"*20)
# --------------

my_list = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_list:", my_list, end='\n\n')

index_no = 0
while index_no < len(my_list):
    print("Course:", my_list[index_no])
    index_no += 1
else:
    print("Reached for-else block")
    print("This block will execute after completing for-loop")
    print("if we are ending 'for-loop' using 'break' then 'else' block will not execute")
    del my_list

# for each_course in my_list:
#     print("Course:", each_course)
# else:
#     print("Reached for-else block")
#     print("This block will execute after completing for-loop")
#     print("if we are ending 'for-loop' using 'break' then 'else' block will not execute")
#     del my_list

print("#"*40, end="\n\n")
################################
