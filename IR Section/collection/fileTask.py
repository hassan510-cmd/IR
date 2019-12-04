class student :
    # def __init__(self, id, fname,lname,cgpa,hours):
    #     # super().__init__(*args, **kwargs)
    #     self.id=id
    #     self.fname=fname
    #     self.lname=lname
    #     self.cgpa=cgpa
    #     self.hours=hours
    def __init__(self, id , arr):
        self.id=id
        self.arr=arr
        # super().__init__(*args, **kwargs)
    
# ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
import numpy as np
def task() :
    myfile = open("Data.txt", "r")
    rowsNum = len(myfile.readlines())
    myfile.seek(0, 0)
    matrix = np.array(myfile.read().strip().split()).reshape(rowsNum, 5)
    dic = {}
    for i in range(len(matrix)):
        l = matrix[i, 0]
        dic[l] = matrix[i, 1:]
    # print("dictinory here",dic)
    for key1, value1 in dic.items():
        print(key1.ljust(15), end=" ")
        for n in value1:
            print(str(n).ljust(15), end=" ")
        print()
    return dic

# ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
listObject=[]
for key , value in task().items():
   obj1=student(key,value)
   listObject.append(obj1)
print("list here \n",listObject)
# for key1, value1 in task.items():
#         print(key1.ljust(15), end=" ")
#         for n in value1:
#             print(str(n).ljust(15), end=" ")
#         print()

