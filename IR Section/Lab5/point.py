class Point:   
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def displayPoint(self):
        print('(',self.x,',',self.y,')')
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

if __name__ == '__main__':
    p = Point()
    print('in class')
    p.displayPoint()
    print(p)


print('Point.__module__',Point.__module__)

