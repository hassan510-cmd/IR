students = {'123423':{'fname':'ahmed','lname':'Ali','CGPA':3.5,'CH':90},
			'124567':{'fname':'Ola','lname':'mohamed','CGPA':3.8,'CH':120},
			'129080':{'fname':'Rowan','lname':'Ali','CGPA':3.0,'CH':90}}

print(('ID').ljust(10),'First_Name'.ljust(10),'Last_Name'.ljust(10),'CGPA'.ljust(10),'Hours'.ljust(10))
for key1, value1 in students.items():
	print(key1.ljust(10),end = ' ')
	for key2, value2 in value1.items():
		print(str(value2).ljust(10),end = ' ')
	print()

#########################################################
# 2 x 3 matrix 
A = [ [ 2, 5, 7 ],[ 4, 7, 9 ] ]
print(A)

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 

print(matrix)
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

mat = [[int(input()) for x in range (C)] for y in range(R)] 
print(mat)

import numpy as np 
entries = list(map(int, input().split())) 
print(entries) 
matrix = np.array(entries).reshape(R, C) 
print(matrix)
print(matrix[0][0])

x = np.array([[1, 2], [4, 5]]) 
y = np.array([[7, 8], [9, 10]]) 
  
# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (np.add(x,y)) 
  
# using subtract() to subtract matrices 
print ("The element wise subtraction of matrix is : ") 
print (np.subtract(x,y)) 
  
# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (np.divide(x,y))

# using multiply() to multiply matrices element wise 
print ("The element wise multiplication of matrix is : ") 
print (np.multiply(x,y)) 
  
# using dot() to multiply matrices 
print ("The product of matrices is : ") 
print (np.dot(x,y)) 

# using sqrt() to print the square root of matrix 
print ("The element wise square root is : ") 
print (np.sqrt(x)) 
  
# using sum() to print summation of all elements of matrix 
print ("The summation of all matrix element is : ") 
print (np.sum(y)) 
  
# using sum(axis=0) to print summation of all columns of matrix 
print ("The column wise summation of all matrix  is : ") 
print (np.sum(y,axis=0)) 
  
# using sum(axis=1) to print summation of all rows of matrix 
print ("The row wise summation of all matrix  is : ") 
print (np.sum(y,axis=1)) 
  
# using "T" to transpose the matrix 
print ("The transpose of given matrix is : ") 
print (x.T) 

print(x.min())
print(x.max())
x = np.array([[4, 5, 6], [8, 1, 10], [7, 12, 5]]) 
print(x[:,2]) # print the 3rd column 
print(x[1,:]) # print the 2nd row
print(x[:,2].min()) # print min value in 3rd column
#####################################################

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

printme("Hello world!")

print('-'*60)
############################################################
#Pass by Reference

def changeme( mylist ):
   print ("Values inside the function before change: ", mylist)
   
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

print('-'*60)
############################################################
#argument is being passed by reference
#and the reference is being overwritten inside the called function.
def changeme2( mylist ):
   mylist = [1,2,3,4] 
   print ("Values inside the function: ", mylist)
   return

mylist = [10,20,30]
changeme2( mylist )
print ("Values outside the function: ", mylist)

print('-'*60)
############################################################
#Keyword Arguments

def printinfo( name, age ):
   #name,age are Required Arguments
   print ("Name: ", name)
   print ("Age ", age)
   return

printinfo( age = 20, name = "ALi" )

print('-'*60)
############################################################
#Default Arguments

def printinfo2( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return


printinfo2( age = 25, name = "Ahmed" )
printinfo2( name = "Ahmed" )
printinfo2( "Ahmed" )

print('-'*60)
############################################################
#Variable-length Arguments

def printinfo3( arg1, *vartuple ):
   print ("Output is: ")
   print (arg1)
   
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo3( 10 )
printinfo3( 70, 60, 50 )

print('-'*60)
############################################################
# Anonymous Functions

sum = lambda arg1, arg2: arg1 + arg2

print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

print('-'*60)
############################################################
#return Statement
def sum2( arg1, arg2 ):
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

total = sum2( 10, 20 )
print ("Outside the function : ", total )

print('-'*60)
############################################################
#Global vs. Local variables

total = 0   # global variable.

def sum3( arg1, arg2 ):
   total = arg1 + arg2 # Here total is local variable.
   #global total
   #total = arg1 + arg2
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum3( 10, 20 )
print ("Outside the function global total : ", total )

print('-'*60)
############################################################
#Modules

from fib import fib
#from fib import *
print(fib(100))














