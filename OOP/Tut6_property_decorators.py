# Object-Oriented Programming in Python
## Tutorial 6 - Property Decorators - Getters, Setters & Deleters 

### Version 1
class Employee:
    def __init__(self, first, second):         # using 'self' is a convention inside this constructor
        self.first = first
        self.second = second
        self.email_id = first+'@email.com'
    def full_name(self):
        return '{} {}'.format(self.first, self.second)

    def email(self):
        return '{}@email.com'.format(self.first)
        

employee1 = Employee('Rachit', 'Jain')
employee2 = Employee('Hurray', 'Unknown')

### Suppose I want to change the first name, then the email ID should automatically change.
employee1.first = 'R'
print("\nVersion 1:")
print(employee1.first)                                
print(employee1.email_id)                        # still has the old first name used!

### This could be corrected using a method called email() to take the first and second name and print in the format desired.
### But if what if we want to do it without any method?


### Version 2
class Employee:

    def __init__(self, first, second):         # using 'self' is a convention inside this constructor
        self.first = first
        self.second = second
        
    def full_name(self):
        return '{} {}'.format(self.first, self.second)

    @property
    def email(self):
        return '{}@email.com'.format(self.first)

employee1 = Employee('Rachit', 'Jain')
employee2 = Employee('Hurray', 'Unknown')


### Suppose I want to change the first name, then the email ID should automatically change.
employee1.first = 'R'
print("\nVersion 2:")
print(employee1.email)


### Suppose I want to use the full name and break it down in the class to set the first and the second name.
### Version 3
class Employee:

    def __init__(self, first, second):                      # using 'self' is a convention inside this constructor
        self.first = first
        self.second = second

    @property                                               # This converts the method into a property which can be modified later as well  
    def full_name(self):
        return '{} {}'.format(self.first, self.second)

    @property
    def email(self):
        return '{}@email.com'.format(self.first)

    @full_name.setter                                       # it has the same name as the function it is setting for
    def full_name(self, fullname):                          # same method name but with an extra argument
        first, second = fullname.split(' ')
        self.first = first
        self.second = second

employee1 = Employee('Rachit', 'Jain')
employee2 = Employee('Hurray', 'Unknown')


### Suppose I want to change the first name, then the email ID should automatically change.
employee1.first = 'R'
print("\nVersion 3:")
employee1.full_name = 'Rachit Jain'                         # we can define this since the full_name is a property which has a setter function to split and get the first and the last name.
print(employee1.full_name)