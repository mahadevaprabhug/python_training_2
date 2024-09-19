"""
Strings:
        -- We have option to store collection of characters like name, email-id etc
        -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store the values?")
print("-"*20)
# --------------

a = 'PERSON'
# Internally it will create object of 'str' class object and store the value

#
b = str('PERSON')

print(a, b, a, b, sep="\n") # sep: put \n between each value

print("#"*40, end="\n\n")
################################

print("Strings PART-2")
print("How to store the values?")
print("-"*20)
# --------------

a = 'PERSON'
b = 'PERSON\'S'
c = "PERSON'S"
d = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
e = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''

# Below line is comment: It is string only but not
# assigned to any variable
'''PERSON'S HEIGHT IS XYZ" (" represents inch)'''

print(a, b, c, d, e, end="\n\n") # In output, It will print each value separated by ONE-SPACE

print(a, b, c, d, e, sep="\n") # put \n between each value

print("#"*40, end="\n\n")
################################

print("Strings PART-3")
print("How to store the values?")
print("-"*20)
# --------------

my_file_path_1 = "C:\newfolder\test.py"
# \n will get replaced with newline
# \t will get replaced with tab-space
print("my_file_path_1=", my_file_path_1, end="\n\n")

my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string where \n\t has no special meanin
print("my_file_path_2=", my_file_path_2, end="\n\n")

# convert already available string into raw format
my_file_path_3 = repr(my_file_path_1)
print("my_file_path_1 in raw format:", my_file_path_3)

print("#"*40, end="\n\n")
################################

print("Strings PART-4")
print("How to store the values?")
print("-"*20)
# --------------

x = 10
y = 20
z = x + y

my_string = f"add of {x} and {y} is {z}"
# f-> format
# f -> will take care of replace {variable_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
################################

print("Strings PART-5")
print("Indexes: We can access each character using index")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("Access 0th character using +ve index number:", my_string[0])
print("Access 0th character using -ve index number:", my_string[-8])

# print("Access 100th character using +ve index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
################################


print("Strings PART-6")
print("Slicing: We can get substring")
print("-"*20)
# --------------

# Refer 5_strings.xlsx

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("substring from index-1 to 6 using +ve index number:", my_string[1:6])
print("substring from index-1 to 6 using -ve index number:", my_string[-7:-2], end="\n\n")
# default behavior: character at end-index will not come

print("substring from index-1 to END using +ve index number:", my_string[1:])
print("substring from index-1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("substring from BEGINNING to 6 using +ve index number:", my_string[:6])
print("substring from BEGINNING to 6 using -ve index number:", my_string[:-2], end="\n\n")

print("#"*40, end="\n\n")
################################

print("Strings PART-7")
print("Step Value: We can skip characters in between")
print("-"*20)
# --------------

# Refer 5_strings.xlsx

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

print("substring from index-1 to 6 using +ve index number:", my_string[1:6:2])
print("substring from index-1 to 6 using -ve index number:", my_string[-7:-2:2], end="\n\n")
# default behavior: character at end-index will not come

print("substring from index-1 to END using +ve index number:", my_string[1::2])
print("substring from index-1 to END using -ve index number:", my_string[-7::2], end="\n\n")

print("substring from BEGINNING to 6 using +ve index number:", my_string[:6:2])
print("substring from BEGINNING to 6 using -ve index number:", my_string[:-2:2], end="\n\n")

print("#"*40, end="\n\n")
################################


print("Strings PART-8")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# --------------

# Refer 5_strings.xlsx

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Example:
# index-6 to 1
# 1) start index should be 6
# 2) end index should be 1
# 3) step value should be -1
# All 3 steps mandatory

print("sub string from index-6 to 1 using +ve index number:", my_string[6:1:-1])
print("sub string from index-6 to 1 using -ve index number:", my_string[-2:-7:-1], end="\n\n")

print("sub string from index-6 to 1 using +ve index number:", my_string[6:1:-2])
print("sub string from index-6 to 1 using -ve index number:", my_string[-2:-7:-2], end="\n\n")

print("#"*40, end="\n\n")
################################

print("Strings PART-9")
print("Methods inside 'str' class")
print("-"*20)
# --------------

my_string = "WEL COME"

# print(dir(my_string))

# OR

print(dir(str))

print("#"*40, end="\n\n")
################################

print("Strings PART-10")
print("Special Names: Ex: __add__")
print("-"*20)
# --------------

# Special names starting with __ and ending __
# - these are system defined
# - these are mapped to some operators/some function

# Example-1: concat 2 string
s1 = "hello"
s2 = "python"
concat_string = s1 + s2 # Here + .mapped-to/calls __add__ which is written inside str class
length_of_s1 = len(s1) # here len function mapped-to __len__ which is written inside str class

print("concat_string:", concat_string)
print("length_of_s1:", length_of_s1)

print("#"*40, end="\n\n")
################################

print("Strings PART-11")
print("'Startswith()' method")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result) # True

print("#"*40, end="\n\n")
################################
