""" Explore Python classes and instances. """


# Class is a blueprint to create instances.
class Employee:

    def __init__(self, first, last, pay): 
        """
        When we create method of class then they recieve instace automatically
        as first argument. By convention we call instance as self but you can
        call whatever you want. 
        """
        # __init__ is used to define constuctor or iniatization of any class.
        print(self)
        self.first = first  # self.first, last .. are attributes of class
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):     # class method
        return '{} {}'.format(self.first, self.last)

    """
    Note: In Above method if we will not pass self paramter then it will
    give typeerror like fullname() takes 0 postional argument but one was
    given. So it simply means that when we call fullname method instance 
    automatically passed as argument in fullname so it expect instance in its
    first argument.
    """

emp_1 = Employee('Corey', 'Schafer', 50000)
# Above and Below __init__ method will run automatically.
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())     # It will print return value of method
print(emp_1.fullname)       # It will print method


emp_1.fullname()
print(Employee.fullname(emp_1))

""" 
Note: Both above statement will give the same result. when you call emp_1.fullname(),
it actually do Employee.fullname(emp_1) in the background. 
"""

"""
class Employee:
    pass        # it is used for skiping the thing.

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
"""

# NOte: both emp_1 and emp_2 are employee class objects and both are unique
# and both have have different locations in the memory.

"""
emp_1.first = 'chirag'
emp_1.last = 'kalal'
emp_1.email = 'chirag@gmail.com'
emp_1.salary = 50000

emp_2.first = 'jenish'
emp_2.last = 'patel'
emp_2.email = 'jenish@gmail.com'
emp_2.salary = 70000
"""

# Above we create employee instance and information manually which is obviously 
# not so useful with using classes so rather we can use __init__ method
