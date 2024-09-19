"""
In this case,
Case-2: How to pass values variables present inside the function

3 ways to pass values
1-way: we can pass only values OR we can pass in key=value format
2-way: only values we can pass
    - Functions with positional arguments
3-way: we can pass using key=value
    - Functions with Keyword or Named arguments
"""

print("1-way: we can pass only values OR we can pass in key=value format")
print("FUNCTION WITH POSITIONAL ARGUMENT OR KEYWORD ARGUMENT")
print("-"*20)
# --------------


# name,company are called ARGUMENTS
# here these arguments are also called POSTIONAL/KEYWORD argument
def employee(name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee("emp-1", "comp-1") # POSITIONAL
print("received_value:", received_value)

received_value = employee(name="emp-2", company="comp-2") # KEYWORD
print("received_value:", received_value)

received_value = employee(company="comp-3", name="emp-3")
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################

print("2-way: only values we can pass")
print("FUNCTION WITH ONLY POSITIONAL ARGUMENT")
print("-"*20)
# --------------


# / is just syntax to tell it is POSITIONAL ARGUMENT function
# / is not counted as argument
# for /, we are not passing any values
def employee(name, company, /):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


received_value = employee("emp-1", "comp-1") # POSITIONAL
print("received_value:", received_value)

# NOT ALLOWED TO PASS LIKE THIS
# received_value = employee(name="emp-2", company="comp-2")
# print("received_value:", received_value)


print("#"*40, end="\n\n")
################################

print("3-way: we can pass using key=value")
print("FUNCTION WITH ONLY KEYWORD ARGUMENT")
print("-"*20)
# --------------


# * is just a syntax to tell it is KEYWORD argument function
# * is not counted argument
# We are not passing any values to *
def employee(*, name, company):
    print("Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}

# PASSING ONLY VALUES ARE NOT ALLOWED
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

received_value = employee(name="emp-2", company="comp-2") # KEYWORD
print("received_value:", received_value)

received_value = employee(company="comp-3", name="emp-3")
print("received_value:", received_value)

print("#"*40, end="\n\n")
################################

