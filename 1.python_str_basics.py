''' Learn basic string functionalities '''

message = "it's my world."
print(message)
message = 'it\'s my world.'
print(message)
message = """ it's my world and i Know how to save
            and live in this world."""
print(message)
message = 'hello world'

print(message)

print(message[0]) #returns first letter of str(slicing[start_include:end_exclude:difference])

print(dir(message)) #returns all methods that can apply on str

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('w'))
print(message.find('universe'))
new_msg = message.replace('world', 'universe')
print(new_msg)
# print(help(str)) #retuns all string methds descriptions and 
# print(help(str.lower)) #you can also specify specific method name like str.lower()