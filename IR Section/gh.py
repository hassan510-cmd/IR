from math import sqrt
from math import log2
import numpy
tfd1=[]
tfd2=[]
tfd3=[]
tfd4=[]
tfd5=[]
tfdq=[]
idff=[]
adj=[[],[],[],[],[]]
hvector=[1,1,1,1,1]
char=['a','b','c','d','e']
d1={}
d2={}
d3={}
d4={}
d5={}
dq={}
idf={}
countera=0
counterb=0
counterc=0
counterd=0
countere=0
idfa=0
idfb=0
idfc=0
idfd=0
idfe=0
tfidfd1=[]
tfidfd2=[]
tfidfd3=[]
tfidfd4=[]
tfidfd5=[]
tfidfdq=[]
ttfidfd1={}
ttfidfd2={}
ttfidfd3={}
ttfidfd4={}
ttfidfd5={}
ttfidfdq={}
authority={}
hubvector={}
ff=['file1','file2','file3','file4','file5']
sd1q=0
sd2q=0
sd3q=0
sd4q=0
sd5q=0
sumd1=0
sumd2=0
sumd3=0
sumd4=0
sumd5=0
sumdq=0
def Query():
    data = input('Enter query  ')
    print(data,file=f)
def generate1():
   from random import choice
   s='12345abcde'
    # print("enter char from a b c d e")
    # c=input("enter  your char")
    # print(c,file=f)

   for i in range(n):
       print(choice(s), file=f)
#hena bd5l el character random mn 5lal call l fn
f = open('1.txt', 'w')
n=int(input("enter the size of the first document"))
generate1()
f.close()
f = open('2.txt', 'w')
n=int(input("enter the size of the second document"))
generate1()
f.close()
f = open('3.txt', 'w')
n=int(input("enter the size of the third document"))
generate1()
f.close()
f = open('4.txt', 'w')
n=int(input("enter the size of the fourth document"))
generate1()
f.close()
f = open('5.txt', 'w')
n=int(input("enter the size of the fifth document"))
generate1()
f.close()
#hena 3mlt read l kol file 3shan  a7sb feh  el tf l kol document
f = open("1.txt", "r+")
w=[]
file1=f.read().split()
counta=file1.count('a')
countb=file1.count('b')
countc=file1.count('c')
countd=file1.count('d')
counte=file1.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfd1.append(counta/x)
tfd1.append(countb/x)
tfd1.append(countc/x)
tfd1.append(countd/x)
tfd1.append(counte/x)
print('tfd1=',tfd1)
f.close()
f = open("2.txt", "r+")
w=[]
file2=f.read().split()
counta=file2.count('a')
countb=file2.count('b')
countc=file2.count('c')
countd=file2.count('d')
counte=file2.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfd2.append(counta/x)
tfd2.append(countb/x)
tfd2.append(countc/x)
tfd2.append(countd/x)
tfd2.append(counte/x)
print('tfd2=',tfd2)
f.close()
f = open("3.txt", "r+")
w=[]
file3=f.read().split()
counta=file3.count('a')
countb=file3.count('b')
countc=file3.count('c')
countd=file3.count('d')
counte=file3.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfd3.append(counta/x)
tfd3.append(countb/x)
tfd3.append(countc/x)
tfd3.append(countd/x)
tfd3.append(counte/x)
print('tfd3=',tfd3)
f.close()
f = open("4.txt", "r+")
w=[]
file4=f.read().split()
counta=file4.count('a')
countb=file4.count('b')
countc=file4.count('c')
countd=file4.count('d')
counte=file4.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfd4.append(counta/x)
tfd4.append(countb/x)
tfd4.append(countc/x)
tfd4.append(countd/x)
tfd4.append(counte/x)
print('tfd4=',tfd4)
f.close()
f = open("5.txt", "r+")
w=[]
file5=f.read().split()
counta=file5.count('a')
countb=file5.count('b')
countc=file5.count('c')
countd=file5.count('d')
counte=file5.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfd5.append(counta/x)
tfd5.append(countb/x)
tfd5.append(countc/x)
tfd5.append(countd/x)
tfd5.append(counte/x)
print('tfd5=',tfd5)
f.close()
#hena 5let  l user yd5l el query  whyt7t f document mn 5lal  call l fn
f = open('query.txt', 'w')
Query()
f.close()
#hena 3mlt read ll query eli ana d5lto w7sbtlo el tf bt3to hwa kman
f = open("query.txt", "r+")
w=[]
file6=f.read().split()
counta=file6.count('a')
countb=file6.count('b')
countc=file6.count('c')
countd=file6.count('d')
counte=file6.count('e')
w.append(counta)
w.append(countb)
w.append(countc)
w.append(countd)
w.append(counte)
x=max(w)
tfdq.append(counta/x)
tfdq.append(countb/x)
tfdq.append(countc/x)
tfdq.append(countd/x)
tfdq.append(counte/x)
print('tfdq=',tfdq)
f.close()
#hena 3mlr dic wh7ot kol character m3ah el tf bt3to fe key wvalue 3shan 23rf at3aml m3ahom fel calculations
for i in range(int(len(char))):
    for j in range(int(len(tfd1))):
        if i==j:
            d1[char[i]] = tfd1[j]
print("document1 with it's tf:",d1)
for i in range(int(len(char))):
    for j in range(int(len(tfd2))):
        if i==j:
            d2[char[i]] = tfd2[j]
print("document2 with it's tf:",d2)
for i in range(int(len(char))):
    for j in range(int(len(tfd3))):
        if i==j:
            d3[char[i]] = tfd3[j]
print("document3 with it's tf:",d3)
for i in range(int(len(char))):
    for j in range(int(len(tfd4))):
        if i==j:
            d4[char[i]] = tfd4[j]
print("document4 with it's tf:",d4)
for i in range(int(len(char))):
    for j in range(int(len(tfd5))):
        if i==j:
            d5[char[i]] = tfd5[j]
print("document5 with it's tf:",d5)
for i in range(int(len(char))):
    for j in range(int(len(tfd1))):
        if i==j:
            dq[char[i]] = tfdq[j]
print("query with it's tf:",dq)
#hena b2h bd2t ashof kol 7rf mwgod f kam file 3shan a2dr ageb el idf l kol character
if "a" in file1:
    countera+=1
if "a" in file2:
    countera+=1
if "a" in file3:
    countera+=1
if "a" in file4:
    countera+=1
if "a" in file5:
    countera+=1
if "a" in file6:
    countera+=1



if "b" in file1:
    counterb+=1
if "b" in file2:
    counterb+=1
if "b" in file3:
    counterb+=1
if "b" in file4:
    counterb+=1
if "b" in file5:
    counterb+=1
if "b" in file6:
    counterb+=1






if "c" in file1:
    counterc+=1
if "c" in file2:
    counterc+=1
if "c" in file3:
    counterc+=1
if "c" in file4:
    counterc+=1
if "c" in file5:
    counterc+=1
if "c" in file6:
    counterc+=1


if "d" in file1:
    counterd+=1
if "d" in file2:
    counterd+=1
if "d" in file3:
    counterd+=1
if "d" in file4:
    counterd+=1
if "d" in file5:
    counterd+=1
if "d" in file6:
    counterd+=1


if "e" in file1:
    countere+=1
if "e" in file2:
    countere+=1
if "e" in file3:
    countere+=1
if "e" in file4:
    countere+=1
if "e" in file5:
    countere+=1
if "e" in file6:
    countere+=1

#hena bd2t ageb l idf l kol character
idfa=log2(6/countera)


idfb=log2(6/counterb)


idfc=log2(6/counterc)


idfd=log2(6/counterd)


idfe=log2(6/countere)

#hena 7tthom f array 3shan 22dr 27thom b3dha  m3a kol character f dic
idff.append(idfa)
idff.append(idfb)
idff.append(idfc)
idff.append(idfd)
idff.append(idfe)

#hena 7tet idf l kol character f dic
for i in range(int(len(char))):
    for j in range(int(len(idff))):
        if i==j:
            idf[char[i]] = idff[j]
print("the character and it's idf=",idf)

for kd1,valued1 in d1.items():
    for kidf,valueidf in idf.items():
        if kd1==kidf:
           tfidfd1.append(float(valued1) *float(valueidf))
print(" tfidf of document1=",tfidfd1)


for kd2,valued2 in d2.items():
    for kidf,valueidf in idf.items():
        if kd2==kidf:
           tfidfd2.append(float(valued2) *float(valueidf))
print(" tfidf of document2",tfidfd2)

for kd3,valued3 in d3.items():
    for kidf,valueidf in idf.items():
        if kd3==kidf:
           tfidfd3.append(float(valued3) *float(valueidf))
print(" tfidf of document3=",tfidfd3)

for kd4,valued4 in d4.items():
    for kidf,valueidf in idf.items():
        if kd4==kidf:
           tfidfd4.append(float(valued4) *float(valueidf))
print(" tfidf of document4=",tfidfd4)

for kd5,valued5 in d5.items():
    for kidf,valueidf in idf.items():
        if kd5==kidf:
           tfidfd5.append(float(valued5) *float(valueidf))
print(" tfidf of document5=",tfidfd5)

for kdq,valuedq in dq.items():
    for kidf,valueidf in idf.items():
        if kdq==kidf:
           tfidfdq.append(float(valuedq) *float(valueidf))
print(" tfidf of query=",tfidfdq)

#hena bd2t ageb el array  wa7otha f shkl en kol col feh l idf*tf w7ttha f dic m3a kol character

for i in range(int(len(char))):
    for j in range(int(len(tfidfd1))):
        if i==j:
            ttfidfd1[char[i]] = tfidfd1[j]
print("the character and it's tfidf of document1=",ttfidfd1)

for i in range(int(len(char))):
    for j in range(int(len(tfidfd2))):
        if i==j:
            ttfidfd2[char[i]] = tfidfd2[j]
print("the character and it's tfidf of document2=",ttfidfd2)

for i in range(int(len(char))):
    for j in range(int(len(tfidfd3))):
        if i==j:
            ttfidfd3[char[i]] = tfidfd3[j]
print("the character and it's tfidf of document3=",ttfidfd3)

for i in range(int(len(char))):
    for j in range(int(len(tfidfd4))):
        if i==j:
            ttfidfd4[char[i]] = tfidfd4[j]
print("the character and it's tfidf of document4=",ttfidfd4)

for i in range(int(len(char))):
    for j in range(int(len(tfidfd5))):
        if i==j:
            ttfidfd5[char[i]] = tfidfd5[j]
print("the character and it's tfidf of document5=",ttfidfd5)

for i in range(int(len(char))):
    for j in range(int(len(tfidfdq))):
        if i==j:
            ttfidfdq[char[i]] = tfidfdq[j]
print("the character and it's tfidf of query=",ttfidfdq)


#hena bd2t ageb l similarity
for kd1,valued1 in ttfidfd1.items():
    for kq,valueq in ttfidfdq.items():
        if kd1==kq:
           sd1q+=(float(valued1) *float(valueq))
print("the similarity of document1 with query=",sd1q)

for kd2,valued2 in ttfidfd2.items():
    for kq,valueq in ttfidfdq.items():
        if kd2==kq:
           sd2q+=(float(valued2) *float(valueq))
print("the similarity of document2 with query=",sd2q)

for kd3,valued3 in ttfidfd3.items():
    for kq,valueq in ttfidfdq.items():
        if kd3==kq:
           sd3q+=(float(valued3) *float(valueq))
print("the similarity of document3 with query=",sd3q)

for kd4,valued4 in ttfidfd4.items():
    for kq,valueq in ttfidfdq.items():
        if kd4==kq:
           sd4q+=(float(valued4) *float(valueq))
print("the similarity of document4 with query=",sd4q)

for kd5,valued5 in ttfidfd5.items():
    for kq,valueq in ttfidfdq.items():
        if kd5==kq:
           sd5q+=(float(valued5) *float(valueq))
print("the similarity of document5 with query=",sd5q)

#hgeb l sum l kol colums 3ndy (sum all ellements of tf-idf of ech document)to get the cosin similarity
for keyd1, valued1 in ttfidfd1.items():
    sumd1 += (valued1 * valued1)
print(" document1 and it's element ^2=",sumd1)

for kd2, valued2 in ttfidfd2.items():
    sumd2 += (valued2 * valued2)
print(" document2 and it's element ^2=",sumd2)

for kd3, valued3 in ttfidfd3.items():
    sumd3 += (valued3 * valued3)
print(" document3 and it's element ^2=",sumd3)

for kd4, valued4 in ttfidfd4.items():
    sumd4 += (valued4 * valued4)
print(" document4 and it's element ^2=",sumd4)

for kd5, valued5 in ttfidfd5.items():
    sumd5 += (valued5 * valued5)
print(" document5 and it's element ^2=",sumd5)

for kdq, valueq in ttfidfdq.items():
    sumdq += (valueq * valueq)
print("query and it's element ^2=",sumdq)
print('********************************************')
mkam1=sqrt(sumd1*sumdq)
mkam2=sqrt(sumd2*sumdq)
mkam3=sqrt(sumd3*sumdq)
mkam4=sqrt(sumd4*sumdq)
mkam5=sqrt(sumd5*sumdq)
mkam=[]
summ=[]
mkam.append(mkam1)
mkam.append(mkam2)
mkam.append(mkam3)
mkam.append(mkam4)
mkam.append(mkam5)

summ.append(sumd1)
summ.append(sumd2)
summ.append(sumd3)
summ.append(sumd4)
summ.append(sumd5)

result=[]
for i in range(int(len(summ))):
    for j in range(int(len(mkam))):
        if i==j:
            if mkam[j]==0:
                result.append("not defined")
            else:
                result.append(summ[i]/mkam[j])
print("cosin similarity",result)

document=['D1','D2','D3','D4','D5']
coisnsimilarity={}

for i in range(int(len(document))):
    for j in range(int(len(result))):
        if i==j:
            coisnsimilarity[document[i]] = result[j]
print(coisnsimilarity)
sorted_cosinsimilarity= sorted(coisnsimilarity.items(),key=lambda kv: kv[1])
print("the arranged cosinsimilarity=",sorted_cosinsimilarity)



   
if "1"  in file1:
    adj[0].append(0)
else:
    adj[0].append(0)
if "2"  in file1:
    adj[0].append(1)
else:
    adj[0].append(0)
if "3"  in file1:
    adj[0].append(1)
else:
    adj[0].append(0)
if "4"  in file1:
    adj[0].append(1)
else:
    adj[0].append(0)
if "5"  in file1:
    adj[0].append(1)
else:
    adj[0].append(0)

if "1"  in file2:
    adj[1].append(1)
else:
    adj[1].append(0)
if "2"  in file2:
    adj[1].append(0)
else:
    adj[1].append(0)
if "3"  in file2:
    adj[1].append(1)
else:
    adj[1].append(0)
if "4"  in file2:
    adj[1].append(1)
else:
    adj[1].append(0)
if "5"  in file2:
    adj[1].append(1)
else:
    adj[1].append(0)

if "1"  in file3:
    adj[2].append(1)
else:
    adj[2].append(0)
if "2"  in file3:
    adj[2].append(1)
else:
    adj[2].append(0)
if "3"  in file3:
    adj[2].append(0)
else:
    adj[2].append(0)
if "4"  in file3:
    adj[2].append(1)
else:
    adj[2].append(0)
if "5"  in file3:
    adj[2].append(1)
else:
    adj[2].append(0)


if "1"  in file4:
    adj[3].append(1)
else:
    adj[3].append(0)
if "2"  in file4:
    adj[3].append(1)
else:
    adj[3].append(0)
if "3"  in file4:
    adj[3].append(1)
else:
    adj[3].append(0)
if "4"  in file4:
    adj[3].append(0)
else:
    adj[3].append(0)
if "5"  in file4:
    adj[3].append(1)
else:
    adj[3].append(0)


if "1"  in file5:
    adj[4].append(1)
else:
    adj[4].append(0)
if "2"  in file5:
    adj[4].append(1)
else:
    adj[4].append(0)
if "3"  in file5:
    adj[4].append(1)
else:
    adj[4].append(0)
if "4"  in file5:
    adj[4].append(1)
else:
    adj[4].append(0)
if "5"  in file5:
    adj[4].append(0)
else:
    adj[4].append(0)

print(adj)

transpose=numpy.array(adj).T
print("Transposed adj matrix=")
print(transpose)

for i in range(11):
    a=numpy.dot(transpose,hvector)
    print("a=",a)
    hvector=numpy.dot(adj,a)
    print("h=",hvector)

for i in range(int(len(ff))):
    for j in range(int(len(a))):
        if i==j:
            authority[ff[i]] = a[j]
print("Authority=",authority)

for i in range(int(len(ff))):
    for j in range(int(len(hvector))):
        if i==j:
            hubvector[ff[i]] = hvector[j]
print("Hubvector=",hubvector)

sorted_authority= sorted(authority.items(),key=lambda kv: kv[1])
print("the arranged Authority=",sorted_authority)

sorted_hubvector= sorted(hubvector.items(),key=lambda kv: kv[1])
print("the arranged hubvector=",sorted_hubvector)

