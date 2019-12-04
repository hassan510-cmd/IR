#OOP
# Creating Classes
# class ClassName:
#    'Optional class documentation string'
#    class_suite
# The class has a documentation string,
# which can be accessed via ClassName.__doc__.
# The class_suite consists of all the component statements
# defining class members, data attributes and functions.


# The variable empCount is a class variable 
# whose value is shared among all the instances of this class.
# This can be accessed as Employee.empCount from inside the class 
# or outside the class.

# The first method __init__() is a special method,
# which is called class constructor or initialization method 
# that Python calls when you create a new instance of this class.

# You declare other class methods like normal functions with 
# the exception that the first argument to each method is self.
# Python adds the self argument to the list for you;
# you do not need to include it when you call the methods.

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
   
    def displayCount(self):
        print( "Total Employee %d" % (Employee.empCount))

    def displayEmployee(self):
        print( "Name : ", self.name,  ", Salary: ", self.salary)
    
    def __str__(self):
        return  "Employee Name : "+ self.name+ ",Employee Salary: "+ str(self.salary)
 

print(Employee.empCount)
print(Employee.__doc__)

emp1 = Employee("Ali", 2000)
emp2 = Employee("Ola", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print(emp1)

print ("Total Employee %d" % Employee.empCount)
emp1.salary = 7000
emp1.displayEmployee()

del emp1.salary
#emp1.displayEmployee() # error

emp1.age=20 #add age attribute 
print(emp1.age)

# The getattr(obj, name[, default]) 
# − to access the attribute of object.
# The hasattr(obj,name) 
# − to check if an attribute exists or not.
# The setattr(obj,name,value) 
# − to set an attribute. If attribute does not exist,
#  then it would be created.
# The delattr(obj, name) 
# − to delete an attribute.

print(hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print(getattr(emp1, 'age') )   # Returns value of 'age' attribute
setattr(emp1, 'salary', 8000)  # Set attribute 'salary' to 7000
delattr(emp1, 'age')           # Delete attribute 'age'
emp1.displayEmployee()

# Built-In Class Attributes:
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )


