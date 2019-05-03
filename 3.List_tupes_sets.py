
courses = ['history', 'math', 'pysics', 'programming']

print(courses)
print(len(courses))

print(courses[0])
print(courses[-1])

print(courses[0:2])
print(courses[:])

courses.append('art')   #add element at the end
print(courses)

courses.insert(0, 'chemistry')  #add element at specific location
print(courses)

courses2 = ['python', 'java', 'c']
courses.insert(0, courses2)
print(courses)
courses.remove(courses2)

courses.extend(courses2)
print(courses)

courses.remove('math')
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [3, 6, 9, 2, 56, 7]
nums.sort()
print(nums)

courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

sort_courses = sorted(courses)
print(sort_courses)

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('chemistry'))
print('math' in courses)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)

#NOTE: list are mutable(changeble) and tuples are immutable

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets
cs_courses = {'History', 'Math', 'Pysics', 'CompSci', 'Math'}

other_courses = {'Chemistry', 'Art', 'Python', 'Pysics'}

print(cs_courses)
print(cs_courses.intersection(other_courses))
print(cs_courses.union(other_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()
