# Object-Oriented Programming in Python
## Tutorial 3 - Class and Static Methods 

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

    @classmethod                                                # informs that this below method is a class method; these are called decorators
    def set_domain_name(cls, new_domain):                       # 'cls' argument denotes class, just like self denotes the instantiated instance
        cls.domain_name = new_domain                            # modifies the class variable

    @classmethod
    def from_string(cls, emp_str):
        first, second, phone = emp_str.split(',')
        return cls(first, second, phone)                        # 'cls' is used in place of 'Employee' since both represent the same thing here

    @staticmethod                                               # these do not take the objecet or the class as the first variable; they directly take the arguemnts
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

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
Employee.set_domain_name('@comp.com')
print("\nDomain Name: ", Employee.domain_name)
print("Domain Name Emp1: ", employee1.domain_name)
print("Domain Name Emp2: ", employee2.domain_name)


### This class method could also have been run using an instance of the class since the method itself modifies the class variable.
### Class methods can be useful as a different contructor for the same class as well.

emp1_str = 'Rakshit,Jain,997723'
new_emp1 = Employee.from_string(emp1_str)

print("\nDetails for the new Employee are: ", new_emp1.__dict__)


### Static Methods are used when you don't access the instance or the class anywhere within the method.
import datetime
my_date = datetime.date(2021,8,6)
print("\nIs this date a weekday? ", Employee.is_workday(my_date))