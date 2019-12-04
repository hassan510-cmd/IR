import random
import string
from flask import Flask ,render_template,request



def Machine(li):
    "'convert query from string to dictionary'"
    dic = {}
    query = li.replace(";", ":").replace("<", "").replace(">", "").split(":")
    for index, key in enumerate(query):
        if not index & 1:
            oldkey = key
            # print("index", index)
            # print("va", key)
            dic[oldkey] = ""
        else:
            dic[oldkey] = key
    # print(dic)
    return dic

def GenerateAndWrite(fileName):

    x = [random.choice("ABCDE") for _ in range(random.randint(1, 10))]
    myfile = open(fileName + ".txt", "w+")
    # print(x)
    myfile.write(" ".join(x))
    myfile.seek(0, 0)
    myfile.close
    return myfile

def StatiscalModel(fileName, QueryStatment):
    arr = GenerateAndWrite(fileName).read().split()
    totalNum = len(arr)

    dictWeight = {}
    result = {}
    D = 0
    k = 0
    Doc1Score = 0

    # print(("Letter").ljust(15), ("D").ljust(15), ("Q").ljust(15))
    # propability calculations :
    for i in list(set(arr)):
        dictWeight[i] = float((arr.count(i) / totalNum))

    # wieght calculations :

    for i in list(set(arr)):
        for j in dictWeight:
            if i == j:
                for key, value in Machine(QueryStatment).items():
                    if key == j:
                        # print(
                        #     i.ljust(15),
                        #     str((dictWeight[j])).ljust(15),
                        #     Machine(QueryStatment)[key],
                        # )

                        Doc1Score += dictWeight[j] * (
                            float(Machine(QueryStatment)[key])
                        )
    # print()
    # print(fileName + " Score :", Doc1Score)
    # print("ـــــــــــــــــــــــــــــــــــــــــــ")

    result[Doc1Score] = fileName

    return Doc1Score

def Run(numOfFiles, fileNameSeq, QueryStatment):

    list = []
    cont = {}
    for i in range(numOfFiles):
        oppo = StatiscalModel(fileNameSeq + str(i + 1), QueryStatment)
        cont[oppo] = fileNameSeq + str(i + 1)

    for f in cont:
        list.append(f)
    list.sort(reverse=True)

    for k in list:
        print(cont[k], k)
    return cont


# Run(int(input("Enter the num of file :")),input("enter the sequance :"), input("enter the query"))


#ــــــــــــــــــــــFLASK start hereـــــــــــــــــــــــ 
app = Flask(__name__)

@app.route('/بتوليد حروف', methods=['GET','POST'])
def form2():
    # print("herefromeh")
    if request.method == 'POST':
        inputDATAT = request.form['queryinput']
        numoffilez = request.form['numoffiles']
        sequanceinput=request.form['sequanceFileName']
        # document1 = GenerateAndWrite("doc1").read().split()
        # document2 = GenerateAndWrite("doc2").read().split()
        # document3 = GenerateAndWrite("doc3").read().split()
        # document4 = GenerateAndWrite("doc4").read().split()
        # document5 = GenerateAndWrite("doc5").read().split()
        # inputDATAT = request.form['queryinput']
        # queryData = str(inputDATAT).split()
        # print(queryData)
        # txt1=document1
        # txt2=document2
        # txt3=document3
        # txt4=document4
        # txt5=document5
        result = Run(int(numoffilez),sequanceinput,inputDATAT)
        return render_template('homePage2.html',query=result)
    return render_template('homePage2.html',query="")


@app.route('/منغير توليد حروف', methods=['GET','POST'])
def form():
    print("herefromeh")
    if request.method == 'POST':
        inputDATAT = request.form['queryinput']
        queryData = str(inputDATAT).split()
        print(queryData)
        result = Run(queryData)
        return render_template('homePage.html',query=result)
    return render_template('homePage.html',query="")
if __name__ == '__main__':
    app.debug = True
    app.run()
