
student = {'name': 'chirag', 'age': 21, 'courses': ['python', 'javascript']}

print(student)

print(student['name'])

print(student['courses'])

#print(student['phone'])    gives 'keyerror' cause phone is not part of student keys

#Note: we can overcome this error by using student.get()

print(student.get('phone'))     #print none value

print(student.get('phone', 'Not Found')) #you can also pass default value in it in second parameter.

student['phone'] = 9989890980   #add item to the (student)dictionary
print(student)

student['name'] = 'sahil'       #update value of key in dict
print(student)

student.update({'name': 'chirag', 'age': 22, 'phone': 9898989898})  #update whole dict
print(student)

del student['phone']    #delete key value pair from dict but does not return value
print(student)

age = student.pop('age')    #pop delete key value pair and also return value
print(student)
print(age)

print(len(student))         #print length of student dict
print(student.keys())       #print key of dict
print(student.values())     #print value of dict
print(student.items())      #print items of dict

#we can iterate each key, value pair using dict.items()

for key, value in student.items():
    print(key, value)