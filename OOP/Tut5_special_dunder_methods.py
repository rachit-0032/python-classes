# Object-Oriented Programming in Python
## Tutorial 5 - Special and Dunder Methods 

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

employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 1:", employee1)                                    # gives the unreadable address location that is not of significance ot the user


### Version 2
class Employee:
    domain_name = '@company.com'
    n_employees = 0

    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone
        Employee.n_employees += 1

    def full_name(self) -> str:                         # '->' denotes the return type of the method, but doesn't force the method to return the exact type
        return '{} {}'.format(self.first, self.second)

    def change_domain(self) -> None:
        self.email = self.first + self.domain_name

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.second, self.phone)


### The instances need to be created again so that the new version of class Employee is activated.
employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 2:",employee1)                                    # uses the __repr__ method to return the readable format
print("Version 2:", repr(employee1))


### When printing the instance of a class, it actually find the __str__ dunder method, which is created for a more readable format for the user.
### If it doesn't find it, then it goes up to __repr__ gets information from that. If that's not there either, by default the address location is sent over.

### Version 3
class Employee:
    domain_name = '@company.com'
    n_employees = 0

    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone
        Employee.n_employees += 1

    def full_name(self) -> str:                         # '->' denotes the return type of the method, but doesn't force the method to return the exact type
        return '{} {}'.format(self.first, self.second)

    def change_domain(self) -> None:
        self.email = self.first + self.domain_name

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.second, self.phone)
        
    def __str__(self) -> str:
        return "{} - {}".format(self.first, self.email)

employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 3:",employee1)                                     # uses the __str__ method to return the most readable format
print("Version 3:", repr(employee1))                                # explicitly calling the repr() method



## More dunder methods
### Version 3
class Employee:
    domain_name = '@company.com'
    n_employees = 0

    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone
        Employee.n_employees += 1

    def full_name(self) -> str:                         # '->' denotes the return type of the method, but doesn't force the method to return the exact type
        return '{} {}'.format(self.first, self.second)

    def change_domain(self) -> None:
        self.email = self.first + self.domain_name

    def __repr__(self) -> str:
        return "Employee('{}', '{}', {})".format(self.first, self.second, self.phone)
        
    def __str__(self) -> str:
        return "{} - {}".format(self.first, self.email)

    def __add__(self, other):
        return self.phone + other.phone


employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 4:", employee1 + employee2)                        # The addition symbol uses the __add__ of the 'int' class by default, but not here!                                 # uses the __str__ method to return the most readable format
print("Version 4:", repr(employee1))                                # explicitly calling the repr() method


### Had we not given the __add__ in the class, there is not way two instances can be added and thus, an error would have shown. 