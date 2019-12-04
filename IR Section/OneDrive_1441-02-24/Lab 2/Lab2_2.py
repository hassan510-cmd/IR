#Files I/O
##############################################################
#access_mode:
#r    Opens a file for reading only.
#     The file pointer is placed at the beginning of the file.
#     This is the default mode.
#rb   Opens a file for reading only in binary format.
#     The file pointer is placed at the beginning of the file.
#r+   Opens a file for both reading and writing.
#     The file pointer placed at the beginning of the file.
#rb+  Opens a file for both reading and writing in binary format.
#     The file pointer placed at the beginning of the file.
#w    Opens a file for writing only.
#     Overwrites the file if the file exists.
#     If the file does not exist, creates a new file for writing.
#wb   Opens a file for writing only in binary format.
#     Overwrites the file if the file exists.
#     If the file does not exist, creates a new file for writing.
#w+   Opens a file for both writing and reading.
#     Overwrites the existing file if the file exists.
#     If the file does not exist, creates a new file for reading and writing.
#wb+  Opens a file for both writing and reading in binary format.
#     Overwrites the existing file if the file exists.
#     If the file does not exist, creates a new file for reading and writing.
#a    Opens a file for appending.
#     The file pointer is at the end of the file if the file exists.
#     That is, the file is in the append mode.
#     If the file does not exist, it creates a new file for writing.
#ab   Opens a file for appending in binary format.
#     The file pointer is at the end of the file if the file exists.
#     That is, the file is in the append mode.
#     If the file does not exist, it creates a new file for writing.
#a+   Opens a file for both appending and reading.
#     The file pointer is at the end of the file if the file exists.
#     The file opens in the append mode.
#     If the file does not exist, it creates a new file for reading and writing.
#ab+  Opens a file for both appending and reading in binary format.
#     The file pointer is at the end of the file if the file exists.
#     The file opens in the append mode.
#     If the file does not exist, it creates a new file for reading and writing.
#########################################################################
#write
f = open("file1.txt", "w")
print ("Name of the file: ", f.name)
print ("Closed or not : ", f.closed)
print ("Opening mode : ", f.mode)
f.write("Python is a great language.\nYeah its great!!\n")
f.close()

#read
f = open("file1.txt", "r+")
str = f.read(10)
print ("Read String is : ", str)
line = f.readline()
print ("Read Line: %s" % (line))
s =  f.readlines()
print(s)
f.close()
#########################################################################
#File Positions
#The tell() method tells you the current position within the file;
#in other words, the next read or write will occur at that many bytes
#from the beginning of the file.
#
#The seek(offset[, from]) method changes the current file position.
#The offset argument indicates the number of bytes to be moved.
#The from argument specifies the reference position from where
#the bytes are to be moved.
#The position is computed from adding offset to a reference point;
#the reference point is selected by the from_what argument.
# 0 (default)measures from the beginning of the file,
# 1 uses the current file position,
# 2 uses the end of the file as the reference point.
#


# Open a file
f = open("file1.txt", "r+")
str = f.read(10)
print ("Read String is : ", str)

# Check current position
position = f.tell()
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = f.seek(0, 0)
str = f.read(10)
print ("Again read String is : ", str)

# Close opened file
f.close()
######################################################################
# Renaming and Deleting Files

import os

# Rename a file from test1.txt to test2.txt
os.rename( "file1.txt", "test.txt" )
# Delete file test2.txt
os.remove("test.txt")

#create a directory test in the current directory 
os.mkdir("test")
# remove a directory
os.rmdir('test')
#display the current working directory
print(os.getcwd())
#change the current directory
os.chdir("D:/Sections/DL/python/dir")
print(os.getcwd())
#Moving up one directory
#os.chdir("..")
# or
os.chdir(os.path.pardir)
print(os.getcwd())



#######################################################################


