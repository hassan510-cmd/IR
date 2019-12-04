import point
p1 = point.Point()
p1.displayPoint()

p2 = point.Point(2,4)
print(p2)
#############################################
class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")

    def parentMethod(self):
        print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)

    def Method(self):
   		print("Parent method") 

class Child(Parent): # define child class
    def __init__(self):
        print ("Calling child constructor")

    def childMethod(self):
        print ('Calling child method')
    def Method(self):
   		print("Child method")

c = Child()        
c.childMethod()   
c.parentMethod()  
c.setAttr(200)      
c.getAttr()   
      

p = Parent()
p.getAttr()

print(issubclass(Child,Parent ))
print(isinstance(p, Parent))

#Overriding Methods
p.Method()
c.Method()
################################################
#Overloading Operators
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
   
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
v3 = v1 + v2
print (str(v3))
print (v3)
##############################################
#Data Hiding
class JustCounter:
    __secretCount = 0  
  
    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
# print (counter.__secretCount) #error
print (counter._JustCounter__secretCount)
