"""
Inheritance
1) multi-level inheritance
2) multiple inheritance

In this section,
1) multi-level inheritance
"""

print("1) multi-level inheritance")
print("-"*20)
# --------------

# Assume below class is already available
class Salary:
    def add_salary(self, sal):
        self.salary = sal
    def get_salary(self):
        return self.salary

# Client NEW requirement on Salary class:
# 1) add/get tax methods
# 2) Change functionality of get_salary() method to return (salary-tax)


# Salary: super-class/parent-class
# Employee: sub-class/child-class
class Employee(Salary):
    # 1) add/get tax methods
    def add_tax(self, tax):
        self.tax = tax
    def get_tax(self):
        return self.tax

    # 2) Change functionality of get_salary() method to return (salary-tax)
    # POLYMORPHISM: We can use same name as super class method name
    def get_salary(self):
        # 1-way to access super class method
        # super_sal = super().get_salary()

        # 2-way to access super class method
        # super_sal = Salary.get_salary(self)

        return self.salary - self.tax


e1 = Employee()

e1.add_salary(20000)
e1.add_tax(2000)

print("Salary:", e1.get_salary())
print("Tax:", e1.get_tax())

print("#"*40, end="\n\n")
################################

print("Extend list class")
print("-"*20)
# --------------


class MyList(list):
    def add_my_name(self, my_name):
        self.my_name = my_name

    def get_my_name(self):
        return self.my_name


L = MyList() # [] -> list

L.append(100)
L.append(200)
L.append(300)

print("L :", L)

L.add_my_name("This is my name")
print("Name:", L.get_my_name())

print("#"*40, end="\n\n")
################################


print("Extend list class")
print("-"*20)
# --------------


class MyList(list):
    def add_my_name(self, my_name):
        self.append(my_name)

    def get_my_name(self):
        return self.my_name



L = MyList() # [] -> list

L.append(100)
L.append(200)
L.append(300)


L.add_my_name("This is my name")
print("L :", L)

print("#"*40, end="\n\n")
################################
