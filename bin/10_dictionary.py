"""
Dictionary:
        -- We have option to store collection of values like list of name, list of email-ids etc.
        -- It will keep DUPLICATE VALUES
        -- Automatically INDEX number WILL not be assigned
            INSTEAD
            we need to provide index to each value
"""

print("Dictionary PART-1")
print("how to store the values")
print("-"*20)
# --------------

my_dictionary_1 = {0:"python", 1:10, 2:"online"}
# Internally it will create object of 'dict' class and store the values

# OR we can also create using class name
my_dictionary_2 = dict({0:"python", 1:10, 2:"online"})

# FOR KEYS: We can use any IMMUTABLE VALUES like numbers, string, tuple
my_dictionary_3 = {"course":"python", "duration":10, "mode":"online"}

# FOR VALUES: values can anything
my_dictionary_4 = {
    "duration": 10,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)
print("my_dictionary_4:", my_dictionary_4)

print("#"*40, end="\n\n")
################################

print("Dictionary PART-2")
print("Access each value using KEY")
print("-"*20)
# --------------

my_dictionary = {
    "duration": 10,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course Name:", my_dictionary["course"]) # 'python'
# x = my_dictionary["course"]
# x[1]
print("2nd character in Course Name:", my_dictionary["course"][1], end="\n\n") # 'python'

print("Mode:", my_dictionary["mode"]) # ["online", "offline"],
print("2nd value in Mode:", my_dictionary["mode"][1]) # "offline"
print("4th character in 2nd value in Mode:", my_dictionary["mode"][1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("lname of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("last character in lname of the Trainer:", my_dictionary["trainer"]["lname"][-1]) # "z"

print("#"*40, end="\n\n")
################################

print("Dictionary PART-3")
print('methods inside "dict" class')
print("-"*20)
# --------------

print(dir(dict))

print("#"*40, end="\n\n")
################################

print("Dictionary PART-4")
print("ADD/UPDATE Values: 1- WAY")
print("-"*20)
# --------------

my_dictionary = {"course":"python", "duration":10, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

my_dictionary["location"] = "India"
# If key present then UPDATE else add new value
print("my_dictionary after adding/updating 'locaton':", my_dictionary)

print("#"*40, end="\n\n")
################################

print("Dictionary PART-5")
print("ADD/UPDATE Values: 2- WAY")
print("-"*20)
# --------------

my_dictionary = {"course":"python", "duration":10, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

another_dictionary = {"location": "India"}
# If key present then UPDATE else add new value
my_dictionary.update(another_dictionary) # Merge

# my_dictionary["location"] = "India"
# If key present then UPDATE else add new value
print("my_dictionary after adding/updating 'locaton':", my_dictionary)

print("#"*40, end="\n\n")
################################


print("Dictionary PART-6")
print("ADD/UPDATE Values: Another Example")
print("-"*20)
# --------------

my_dictionary = {
    "duration": 10,
    "course": "python",
    "mode": ["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

# Add/Update 'Exp' = 5
my_dictionary["trainer"]["exp"] = 5
# OR
new_value = {"x": 105}
my_dictionary["trainer"].update(new_value)

print("my_dictionary after adding/updating 'Exp':", my_dictionary)

print("#"*40, end="\n\n")
################################


print("Dictionary PART-7")
print("Remove values from dictionary")
print("-"*20)
# --------------

my_dictionary = {"course":"python", "duration":10, "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")


removed_value = my_dictionary.pop("course")
print("After removing 'course' using pop():", my_dictionary)
print("Removed Value using pop():", removed_value)

removed_value = my_dictionary.popitem()
print("After removing 'course' using popitem():", my_dictionary)
print("Removed Value using popitem():", removed_value)

print("#"*40, end="\n\n")
################################
