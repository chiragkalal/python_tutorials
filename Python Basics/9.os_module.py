import os
from datetime import datetime

# print(dir(os))        This will print all mehtod and attributed which can apply on os

print(os.getcwd())      #get current directory

os.chdir('/home/trt/Desktop')

print(os.getcwd())

print(os.listdir())
    
# os.mkdir('os-demo')       create single level directory
# os.makedirs('os-demo2/sub-dir')   create multi level directory

# os.rmdir('os-demo')       remove single level directory
# os.removedirs('os-demo2/sub-dir')  remove multi level directory

# os.rename('my_module.py', 'custom_module.py')
# print(os.listdir())

print(os.stat('custom_module.py'))

mod_time = os.stat('custom_module.py').st_mtime     # file modified time stamp
print(mod_time)

print(datetime.fromtimestamp(mod_time))

# for dirpath, dirname, filenames in os.walk('/home/trt/Desktop'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirname)
#     print('Files:', filenames)
#     print()

# Note: os.walk give three things which are directory path, directoryname and list of files.

home = os.environ.get('HOME')      # Get environment value of Home which returns path of home directory.

filepath = os.path.join(home, 'abc.txt')

print(filepath)

print(os.path.basename('/home/trt/Desktop/custom_module.txt'))      # print file name
print(os.path.dirname('/home/trt/Desktop/custom_module.txt'))       # print dir name
print(os.path.split('/home/trt/Desktop/custom_module.txt'))         # print both file and dir

print(os.path.isfile('/home/trt/Desktop/custom_module.py'))         # check file is exist or not
print(os.path.isdir('/home/trt/Desktop'))                           # check dir is exist or not

print(dir(os.path))