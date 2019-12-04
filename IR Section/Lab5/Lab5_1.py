#############################################################
a,b = 6,0
#print(a/b)
try:
    g = a/b
    print(g)
except ZeroDivisionError as s:
    print (s)
##################################
try:
    g = a/b
except ZeroDivisionError:
    print ("This is a DIVIDED BY ZERO error")
##################################
a=10
b=2

try:
    g = a/b
except ZeroDivisionError as s:
    print (s)
else:
	print(g)
###################################
try:
   f = open("testfile", "w")
   f.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
finally:
   f.close()
print(f.closed)
###################################
try:
   f = open("testfile", "r")
   f.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
finally:
	f.close()
print(f.closed)
####################################
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

temp_convert("xyz")
#####################################
def functionName( level ):
   if level <1:
      raise Exception(level,'Invalid Level')
   return level
# print(functionName(0))
try:
   l = functionName(-10)
   print ("level = ",l)
except Exception as e:
   print ("error in level argument",e.args[0])
################################################


