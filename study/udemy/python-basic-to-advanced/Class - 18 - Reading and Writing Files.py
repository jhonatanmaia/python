"""

    Reading Files

We use the built in function open()

open() -> You can pass only the file name and/or path and function returns
a _io.TestIOWrapper what we are going to work on it.

By standard the file will be opned just for reading. If the file does not
exist will return the error FileNotFoundError

Enconding: like UTF-8

mode r -> Reading Mode

file = open('class18')

print(file)
print(type(file))

print(file.read())

Python use cursor, so you cant print read() two times

read() -> read all the file, not a line

file = open('class18')

ret = file.read()
print(type(ret))
print(ret)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Seek and Cursors

seek() -> Its used to move the cursor in the text receive a paramater to
where to put the cursor

file = open('class18')

print(file.read())

file.seek(0)

print(file.read())

you can read x number of characters
print(file.read(50 or how much you want to))

file.seek(5)

print(file.read())

readline() -> read the file line by line

file.seek(0)

print(readline())
print(readline())
print(readline())
print(readline())
print(readline())

file.seek(0)

ret = readline()

print(type(ret))

readlines() -> return a list of all lines - you can count 

lines = readlines()

print(len(lines))

Streaming -> Its a conexion between the program and the file. We need to
close the cnexion after finishing

file = open('The file you want')

print(file.read())
work with the file

file.closed -> check the file is closed and return True or False
file.close()

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    with command

Its used to creat a work context where the ressource will be closed after

with open('class18') as file:
    print(file.readlines())
    print(file.closed)

print(file.closed)

if you try to access after the block will return a ValueError

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Wrinting in files

when you open a file to read you cant write, and if you open to write
you cant read

-> when you open a file to write, if the file does not exist, it will be
created if the file exists, the content will be losted

with open('class18-2.txt','w') as file:
    file.write('Wrinting something \n')
    file.write('easy \n')
    file.write('last line')
    
write() -> we pass a string, only STRING, to write the file. Otherwise return
a TypeError

with open('class18-2.txt','w') as file:
    file.write('new line \n')
    file.write('hard \n')
    file.write('maybe the last line')

you can use open write and then close to read file, but its not recommended

with open('class18-2.txt','w') as file:
    while True:
        file.write('new line \n'*1000)
        
    
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Files Modes
    
r -> open in read mode - standard
w -> open in write mode - overwrites if the files exists
x -> open in write mode - only if the file does not exist else return 
FileExistsError - Use a try except
a -> open in write mode - append the new content in the last place, if the 
file does not exist, will creat it
+ -> open in update mode - you can use 

save=''

with open('class18-2.txt','r') as file:
    save = file.readlines()

with open('class18-2.txt','w') as file:
    file.write('Trying to add\n')
    for i in save:
        file.write(i)
print(save)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    StringIO

Write files in the memory not in disc

from io import StringIO

mensage= 'String'

its the same as open()
file = StringIO(mensage)

Now with the file we can use for the same things

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    File System and Navigation

To manipulate files in the SO we use the OS module

import os

getcwd() -> current work directory
print(os.getcwd())

chdir('..') -> comeback one directory
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

Absolute is all the path, relative is only a path part
https://docs.microsoft.com/pt-br/dotnet/standard/io/file-path-formats

os.path.isabs('path') -> Return True if the path is absolute
print(os.path.isabs('C:\\Users\\jbcma\\Documents'))
Always use \\ in windows

os.name -> Get the OS name: posix (Linux and Mac), nt (Windows)

os.uname() -> Only available in some systems. get more data from system
system = os.uname()
print(system)

if you want other way use
import platform
platform.platform()
'Windows-10-10.0.18362-SP0'

or

import sys
print(sys.platform)

print(os.getcwd())
os.path.join -> receive two paramaters, first directory actual and
the directory to 'sum'/join

res= os.path.join(os.getcwd(),'geek','testintest')
os.chdir(res)
#os.chdir('..')
print(os.getcwd())

show the directory that have
print(os.listdir())
print(len(os.listdir()))
os.listdir('C:\\')

os.scandir('C:\\') -> show more details
scan = os.scandir('C:\\')
files = list(scan)

print(files)
print(dir(files[0]))
print()
print(files[0].is_file) #is a file?
print()
print(files[0].path) # path to file
print()
print(files[0].stat) #statistics
print()
print(files[0].inode()) #?
print()
print(files[0].is_dir()) # is it a directory?
print()
print(files[0].is_symlink()) # is it a symbolical link?
print()
print(files[0].name) # file name

scan.close() # you need to close

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    OS manipulation
    
# discovering if a file exists

# file
print(os.path.exists('file.txt'))
print(os.path.exists('four.py'))

# directory relatives and absolutes
print(os.path.exists('__pycache__'))
print(os.path.exists('C:\\Users\\jbcma\\Documents\\Python\\Estudo\\Udemy - Python Basic to Advanced'))

# Non usual way to create files

open('creatnewfile.txt','w').close()
open('creatnewfile2.txt','a').close()
with open('creatnewfile3.txt','w') as file:
    pass

# usual way if does not exist
os.mknod('filetest.txt')
os.mknod('You can insert a path too')

# creating directory if does not exist
# absolute or relative paths are allowed
os.mkdir('templates')
#It can return a parmission error

# if you want to creat a long path
os.makedirs('templates/geek', exist_ok=True)
# if exists return an error
# exist_ok=True if exists ignore

# rename a folder
os.rename('test','test2')

# deleting a file
# its not going to trash
os.remove('somethingelse.txt')

# remove a path
os.rmdir('test2')

to send files to trash use send2trash module
from send2trash import send2trash
send2trash('filename.extension')

# temporary path
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    with open(os.path.join(tmp,'temporary.txt'),'w') as file:
        file.write('some text')
    input()

with tempfile.TemporaryFile() as tmp:
    # temporary files can save only binary codes, thats why it has a b''
    tmp.write(b'Somethig')
    tmp.seek(0)
    print(tmp.read())

"""

import os

