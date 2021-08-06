# Object-Oriented Programming in Python
## Tutorial 1 - Classes and Instances

### Classes come in handy when we need to scale up the code and use the same thing multiple times, with repeated instances of the same thing.
### Each unique object of a class is known as its instance.


###### Version 1

## Example: Employee Class
class Employee:
    pass

employee1 = Employee()
employee2 = Employee()

print(employee1)
print(employee2)                # at a different location --> different instance

### Suppose you want to add the detail of 2 employees.
employee1.first_name = 'Rachit'
employee1.second_name = 'Jain'
employee1.email = 'rachit@ymail.com'
employee1.phone = 998811

employee2.first_name = 'Hurray'
employee2.second_name = 'Unknown'
employee2.email = 'hurray@ymail.com'
employee2.phone = 997722

print("\nVersion 1")
print(employee1.email)
print(employee2.email)

### These are instance variables since they are created for each instance individually.
### Since these are same for all 100k employees I want to store the data for, I do not need to do it again and again.


###### Version 2
class Employee:
    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone

employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 2")
print(employee1.email)
print(employee2.email)
print('Employee 1 | Full Name: {} {}'.format(employee1.first, employee1.second))        # {} act as placeholder


### But what if we need to print out the full name multiple times, maybe for each employee. We can create a 'method' in the class itself.

###### Version 3
class Employee:
    def __init__(self, first, second, phone):         # using 'self' is a convention inside this constructor
        self.first= first
        self.second = second
        self.email = first + '@ymail.com'
        self.phone = phone

    # All methods within a class take the first argument as the instance itself
    def full_name(self):
        return '{} {}'.format(self.first, self.second)

employee1 = Employee('Rachit', 'Jain', 998811)
employee2 = Employee('Hurray', 'Unknown', 997722)

print("\nVersion 3")
print('Employee 1 | Full Name: ', employee1.full_name())
print('Employee 2 | Full Name: ', Employee.full_name(employee2))

### If we run the method using the class, we need to tell as to which instance of the class is to be used.
### On the other hand, if we are directly using the instance, it automatically sends in 1 position argument which is the instance variable itself.
### Hence, the argument 'self' is needed in all the methods of the class.


### Instance Variables are the ones that are unique for each instance, like first, second, email here phone here
### Class Variables are the ones that are same for each instance. For Example, annual bonus can be same for all employees.
