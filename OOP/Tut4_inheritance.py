# Object-Oriented Programming in Python
## Tutorial 4 - Inheritance & Sub-Classes 

### Version 1
class Employee:
    domain_name = '@company.com'
    n_employees = 0

    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone
        Employee.n_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.second)

    def change_domain(self):
        self.email = self.first + self.domain_name 


## Suppoe we want to use the functionalities of the Employee class and do something over and above it, then we can inherit it as the parent class.
class Associate(Employee):                          # Inherited from the Employee Class
    domain_name = '@develop.com'

    # In order to let the repeated parameters be handled as was done in the parent class, we use 'super'
    def __init__(self, first, second, phone, years_exp):
        super().__init__(first, second, phone)
        # Employee.__init__(self, first, second, phone)       # this could also be used
        self.years_exp = years_exp


class Manager(Employee):
    def __init__(self, first, second, phone, employees=None):   # it is recommended not to pass mutable datatypes as arguments in methods!
        super().__init__(first, second, phone)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.full_name())


associate1 = Employee('Rachit', 'Jain', 998811)
associate1.change_domain()                                  # This would use the domain name variable of the Employee Class
associate2 = Associate('Hurray', 'Unknown', 997722, 5)         
associate2.change_domain()                                  # Since the domain name is explicitly defined for the developers, it would use that variable.

print("\n")
print(associate1.email)
print(associate2.email)
print(associate2.years_exp)

# help(Associate)                                       # The Method Resolution Order dictates the paths where Python will look for the methods that can be used by an instance of this class.

manager1 = Manager('Senorita', 'J.', 998821, [associate1])
print("\n")
print(manager1.email)
manager1.add_employee(associate2)
manager1.print_employees()

manager1.del_employee(associate1)
print("\nAfter Deleting one employee")
manager1.print_employees()


## How to check which all classes is the instance related to?
print("\nFor Employee 1:")
print(isinstance(associate1, Employee))
print(isinstance(associate1, Associate))
print(isinstance(associate1, Manager))

print("\nFor Employee 2:")
print(isinstance(associate2, Employee))
print(isinstance(associate2, Associate))
print(isinstance(associate2, Manager))


## How to check for sub-classes?
print("\nSub-Class Associations:")
print(issubclass(Manager, Employee))
print(issubclass(Employee, Associate))


### It is recommended not to pass mutable datatypes as arguments in methods!