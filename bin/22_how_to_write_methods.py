"""
How to write methods?
"""

print("Creating objects")
print("-"*20)
# --------------


class Employee:
    def store_employee_name(self, n):
        self.name = n

    def get_employee_name(self):
        return self.name

    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

    @classmethod
    def get_company_name(cls):
        return cls.company_name

e1 = Employee()
e2 = Employee()


print("#"*40, end="\n\n")
################################

print("Store the data")
print("-"*20)
# --------------

Employee.store_company_name("comp-1")
# Internally class object 'Employee' passed to 'cls'
# 'cls' to store/keep CLASS OBJECT

e1.store_employee_name("emp-1")
# Internally instance object 'e1' passed to 'self'
# 'self' to store/keep INSTANCE OBJECT

e2.store_employee_name("emp-2")
# Internally instance object 'e2' passed to 'self'
# 'self' to store/keep INSTANCE OBJECT

print("#"*40, end="\n\n")
################################

print("DATA present in BRADNEW objects")
print("-"*20)
# --------------

print("DATA present inside class object 'Employee':", Employee.get_company_name())
# Internally class object 'Employee' passed to 'cls'
# 'cls' to store/keep CLASS OBJECT

print("DATA present inside instance object 'e1':", e1.get_employee_name())
# # Internally instance object 'e1' passed to 'self'
# # 'self' to store/keep INSTANCE OBJECT

print("DATA present inside instance object 'e2':", e2.get_employee_name())
# Internally instance object 'e2' passed to 'self'
# 'self' to store/keep INSTANCE OBJECT

print("#"*40, end="\n\n")
################################
