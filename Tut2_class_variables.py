# Object-Oriented Programming in Python
## Tutorial 2 - Class Variables

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
        self.email = self.first + self.domain_name              # using self.domain_name makes sure that we only use that employee 
                                                                # specific domain name if there was any earlier modification done to the same
        # self.email = self.first + Employee.domain_name        # Both would serve the same purpose

employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print('Employee 1 | Email: ', employee1.email)
employee1.change_domain()
print('Employee 1 | Updated Email: ', employee1.email)

print(employee1.__dict__)               # gives detail about Employee 1 and its variables; in the namespace
print(Employee.__dict__)                # gives a list of all class variables; domain_name would exist here!

## To understand how class variable is different from an instance variable, we update it multiple ways and print it.
print("\nDomain Name: ", Employee.domain_name)
print("Domain Name Emp1: ", employee1.domain_name)
print("Domain Name Emp2: ", employee2.domain_name)

## Changing the Class variables changes it throughout all the instances since the instance also use the class to get to that variable.
Employee.domain_name = '@comp.com'
print("\nDomain Name: ", Employee.domain_name)
print("Domain Name Emp1: ", employee1.domain_name)
print("Domain Name Emp2: ", employee2.domain_name)

## Changing it specifically for an instance would result otherwise.
employee2.domain_name = '@company.com'
print("\nDomain Name: ", Employee.domain_name)
print("Domain Name Emp1: ", employee1.domain_name)
print("Domain Name Emp2: ", employee2.domain_name)
print("\nNumber of Employees: ", Employee.n_employees) 