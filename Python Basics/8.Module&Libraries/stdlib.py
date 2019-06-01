""" Define some usecase of built in std libraries. """

import datetime
import calendar
import random
import os

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

courses = ['python', 'c', 'c++', 'java', 'javascript']
print(random.choice(courses))

print(os.getcwd())

# dunder means __

print(os.__file__)

import antigravity