
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:            #if number will be 3 then print found and break the loop
        print('found!')
        break
    print(num)

for num in nums:
    if num == 3:            #if number will be 3 then print found and skip that entry 
        print('found!')
        continue            #continue will not break the loop but it will skip the entry
    print(num)

for num in nums:            #loop within a loop
    for ch in 'abc':
        print(num, ch)

for num in range(10):       #range give range of values. Here it will give values upto 10 but not 10.
    print(num)

for num in range(1, 11):    #print 1 to 10 using range
    print(num)

x = 0

while x < 10:               #it will go upto 10 values.
    print(x)
    x += 1

# while True:               #It will go into infinite loop
#     print(x)
#     x += 1
