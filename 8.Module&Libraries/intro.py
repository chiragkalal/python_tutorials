import sys
sys.path.append('/home/trt/Desktop')

from my_module import find_index, test      #import fiunction and var from my_module
# from my_module import *                   import everything or wild card import

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Physics')      #Access func which is imported
print(index)
print(test)

print(sys.path)
