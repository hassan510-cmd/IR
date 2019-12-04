print("Hello, World!")
#print("This is a
#multiline string.")
print("""This is a 
multiline string.""")

print('-'*50)
########################################################
#Multiple Assignment
a = b = c = 1
print(a)
print(b)
print(c)
a,b,c =1,2,"john"
print(a,b,c)

print('-'*50)
########################################################
#Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z)
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)

print('-'*50)
########################################################
#String
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string (index 0)
print (str[2:7])     # Prints characters starting from index 2 to index 6 ( [2:7) )
print (str[2:])      # Prints string starting from 3rd character
print (str[:2])      # Prints first two characters
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

a = " Hello, World! "
print(a.strip()) #strip() method removes any whitespace from the beginning or the end
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(",")) # returns ['Hello', ' World!']
#split() method splits the string into substrings if it finds instances of the separator

print("Enter your name:")
x = input()
print("Hello, " + x)

print('-'*50)
########################################################
#Arithmetic Operators
# + - * / % ** //
# **    Exponentiation	x ** y	 
# //	Floor division  x // y
#Assignment Operators
# = += -= *= /= %= //= **=
# &= |= ^= >>= <<=
#Comparison Operators
# == != > < >= <=
#Logical Operators
# and or not
# not(x < 5 and x < 10)
#Identity Operators
# is       Returns true if both variables are the same object
# is not   Returns true if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

print(x == y)
# returns True because x is equal to y


x[0] = "orange"
print(x)
print(z)
z=x[:]
print(x is z)
z[0] = "apple"
print(x)
print(z)

#Membership Operators
# in        Returns True if a sequence with the specified value is present in the object
# not in
print("banana" in x)

#Bitwise Operators
# & | ^ ~ << >>

print('-'*50)
########################################################
#List
List = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (List)          # Prints complete list
print (List[0])       # Prints first element of the list
print (List[-1])      # prints last element of the list
print (List[1:3])     # Prints elements starting from 2nd till 3rd 
print (List[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (List + tinylist) # Prints concatenated lists

print (List[::1])
print (List[::-1])
print (List[::2])
print (List[::-2])
print (List[1::2])

List[0] = 222
print (List)
# for x in rang(start,end,step)
for x in List:
  print(x)
  
print(len(List))

List.append("orange")
print(List)

List.insert(1, "orange")
print(List)

List.remove("orange") 
#  remove first match 
print(List)

List.pop()  
# last element
print(List)

List.pop(0)
print(List)

del List[0]
print(List)

List.clear()
print(List)
List.append(1)
del List
#print(List)
#List.append(2)

#list() Constructor

thislist = list(("apple", "banana", "cherry"))
print(thislist)

print(thislist.count("apple"))

cars = ['Ford', 'BMW', 'Volvo']
thislist.extend(cars)
print(thislist)

points = (1, 4, 5, 9)
thislist.extend(points)
print(thislist)

x = thislist.index("cherry")
print(x)

thislist.reverse()
print(thislist)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
cars.sort(reverse=True, key=myFunc)
print(cars)

L = [3,5,1,7,9,0]
print(min(L))
print(max(L))
print(sum(L))

print('-'*50)
########################################################
#Tuples
#A tuple is a collection which is unchangeable
#Tuples can be thought of as read-only lists
t1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (t1)           # Prints complete tuple
print (t1[0])        # Prints first element of the tuple
print (t1[1:3])      # Prints elements starting from 2nd till 3rd 
print (t1[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (t1 + tinytuple) # Prints concatenated tuple
#tuple[0] = 222         #error

for x in t1:
  print(x)
  
print(len(t1))

for x in (1,2,3) :
    print (x)
for x in (1,2,3) :
    print (x, end = ' ')
print()

tup1 = ()
#To write a tuple containing a single value you have to include a comma, even though there is only one value −
tup1 = (50,)
print(tup1)
print(type(tup1))

t = (50)
print(type(t)) #int


tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

del tup1
#print(tup1) #error

#tuple() Constructor
thistuple = tuple((1, 3, 7, 8, 7, 5, 4, 6, 8, 5))
print(thistuple)
x = thistuple.count(5)
print(x)
x = thistuple.index(8)
print(x)
x=min(thistuple)
print(x)

print('-'*50)
########################################################
#Sets
#A set is a collection which is unordered and unindexed
thisset = { "banana", "apple","cherry"}
print(thisset)
for x in thisset:
  print(x)

print("banana" in thisset)

#print(thisset[0])  #error

thisset.add("orange")
print(thisset)

thisset.update(["orange", "mango", "grapes","banana"])
print(thisset)

print(len(thisset))

thisset.remove("banana")
#If the item to remove does not exist, remove() will raise an error.
print(thisset)

thisset.discard("banana")
#If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

#The clear() method empties the set:
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
del thisset
#print(thisset)  #error

#set() Constructor
thisset = set(("apple", "banana", "cherry")) 
print(thisset)

print('-'*50)
########################################################
#Dictionary
dict = {}


dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict)
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

print('-'*50)
########################################################
#



