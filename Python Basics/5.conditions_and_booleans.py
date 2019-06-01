# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

language = 'python'

if language == 'python':
    print('Language is Python')
elif language == 'java':
    print('Language is Java')
elif language == 'javascript':
    print('Language is JavaScript')
else:
    print('No match')

'''
Note: 
    In Python there is no switch case. python belives that switch case is implement with if and elif
    so there is no need of switch case.
'''

user = 'Admin'
logged_in = 'True'

if user == 'Admin' and logged_in:
    print('welcome')
else:
    print('Please log in')

logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('welcome')

a = [1,2,3]
b = [1,2,3]

print(a == b)   #comapre value of a and b
print(a is b)   #comapre object of a and b

#Note: Here a and b are different object which saved in memory. We can see that objs using ids.

print(id(a))
print(id(b))

b = a
print(a is b)   #here we assign a into b. so it does not make diffrent object.
print(id(a), id(b))