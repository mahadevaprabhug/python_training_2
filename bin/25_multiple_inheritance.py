"""
Here,
2) multiple inheritance

We can extend from multiple classes
"""

print("2) multiple inheritance")
print("-"*20)
# --------------


# Assume this is existing class-1
class Salary:
    def add_salary(self, sal):
        self.salary = sal

    def get_salary(self):
        return self.salary

# Assume this is existing class-2
class Tax:
    def add_tax(self,tax):
        self.tax = tax
    def get_tax(self):
        return self.tax

# Client Requirement: Write class with below functionalities
# 1. add/get salary
# 2. add/get tax
# 3. add/get name


class Employee(Salary, Tax):
    def add_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


e1 = Employee()

e1.add_tax(2000)
# Tax.add_tax(e1, 2000)
e1.add_name("emp-1")
e1.add_salary(20000)

print("Name:", e1.get_name())
print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())

print("#"*40, end="\n\n")
################################
