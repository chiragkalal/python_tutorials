# def hello():
#     pass

# print(hello())      #It will print None because nothing is mentioned in hello function.


def hello_world():
    return 'hello world'

print(hello_world())
print(hello_world().upper())    #It will print return values and convert it into upper case

def hello_func(greetings):
    return '{} function'.format(greetings)

print(hello_func('Hey'))

def hello_func2(greetings, name='You'):
    return '{} {}'.format(greetings, name)

print(hello_func2('Hey'))
print(hello_func2('Hey', 'chirag'))


# positional Arguments: 'math', 'science', 'any string', {'name':'chirag'}, ['test'], 1, 5
# keyword Arguments: name='chirag', Age=21
# you can use dict as kwargs by giving argument *any_dict

# NOTE = you can specify anything in place of args or kwargs but this is just naming conventions that
# is followed by all developers so that code can be eaily understanble by others.

def student_info(*args, **kwargs):      # *args=positional args, **kwargs=keyword args
    print(args)                         # It will give result in tuples
    print(kwargs)                       # It will give result in dict

#NOTE: Make sure you are printing args and kwargs without using * symbol other wise you may face type errors.

student_info('python', 'java', name='chirag', age=21)

courses = ['python', 'java']
info = {'name': 'chirag', 'Age':21}

student_info(courses, info)
student_info(*courses, **info)      # you need to unpack value if want to use variable in args & kwargs.


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]