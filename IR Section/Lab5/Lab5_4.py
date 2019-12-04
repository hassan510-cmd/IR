class Parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'a = %d , b = %d ' % (self.a , self.b)
    
class Child(Parent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        # super(Child,self).__init__(a,b)
        self.c = c
    def __str__(self):
        return super().__str__()+ ' , c = %d'% self.c
        # return super(Child,self).__str__() + ' , c = %d'% self.c


o = Child(2,3,5)
print(o)