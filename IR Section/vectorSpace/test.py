import numpy as np
import math
from collections import Counter
import random
import string
import os,re
import os, os.path
from flask import Flask ,render_template,request
from datetime import datetime, timedelta
import pygal
import matplotlib.pyplot as plt
import networkx as nx
import shutil


# initialize here :
charPattern=r'^[A-Z]$'
Standard = ["A", "B", "C", "D", "E"]
numOffiles = int(len([name for name in os.listdir(".") if os.path.isfile(name)]))
totalCosSim = {}
document1 = open("1.txt", "r").read().split()
document2 = open("2.txt", "r").read().split()
document3 = open("3.txt", "r").read().split()
document4 = open("4.txt", "r").read().split()
document5 = open("5.txt", "r").read().split()

def GenerateAndWrite(fileName):

    x = [random.choice("ABCDE12345") for _ in range(random.randint(1, 20))]
    myfile = open(fileName + ".txt", "w+")
    myfile.write(" ".join(x))
    myfile.seek(0, 0)
    myfile.close
    return myfile

def getMax(list1):
    j = 0
    max = 0
    for i in list1:
        if re.match(charPattern,i):
            if list1.count(i) > max:
                max = list1.count(i)
                letter = i
    return max

def getTf(list1, filename):
    "take data  from file as list then return the tf for each character"
    TF = {}
    for i in Standard:
        if i in list(set(list1)):
            TF[i] = round(Counter(list1)[i] / getMax(list1), 6)
        else:
            TF[i] = 0
    return TF

def getIDF(queryData):
    "number of how many files this letter appear in it  "
    frequncey = {}
    IDF = {}
    for i in Standard:
        flag = 0
        if i in document1:
            flag += 1
        if i in document2:
            flag += 1
        if i in document3:
            flag += 1
        if i in document4:
            flag += 1
        if i in document5:
            flag += 1
        if i in queryData:
            flag += 1
        frequncey[i] = flag
        IDF[i] = round((math.log2(6 / flag)),6)
    return IDF

def getTotalWieght(queryData):
    totalTF = {}
    for i in range(5):
        W = {}
        for TFkey, TFvalue in getTf(
            open(str(i+1)+".txt", "r").read().split(), str(i + 1)+".txt"
        ).items():
            for IDFkey, IDFvalue in getIDF(queryData).items():
                if TFkey == IDFkey:
                    W[TFkey] = TFvalue * IDFvalue
        totalTF["doc" + str(i + 1)] = W
    # print("totalTF", totalTF)
    # print()
    return totalTF

def getWeightOfQuery(queryData):
    Q = {}
    for TFkey, TFvalue in getTf(queryData, "query").items():
        for IDFkey, IDFvalue in getIDF(queryData).items():
            if TFkey == IDFkey:
                Q[TFkey] = TFvalue * IDFvalue
    return Q

def Run(queryData):
    for nameofDoc, wieghtDicOFDoc in getTotalWieght(queryData).items():
        elmakam = 0
        sqrOfChar = 0
        sqrOfQueryChar = 0
        elbasst = 0
        for (char, charWieght),(querychar, querycharwight) in zip(wieghtDicOFDoc.items() , getWeightOfQuery(queryData).items()):
            elbasst += charWieght * querycharwight
            sqrOfChar += (charWieght) ** 2
            sqrOfQueryChar+= (querycharwight) ** 2
        elmakam = math.sqrt(sqrOfChar * sqrOfQueryChar)
        if elbasst==0:
            elmakam=1
        totalCosSim[nameofDoc] = round(elbasst / elmakam,3)
    list = sorted(totalCosSim.items(), key=lambda kv: (kv[1], kv[0]))
    # print(list)
    return list

def adjMatrix():
    import numpy as np
    import re
    pattern=r'^[1-5]$'

    standardNum=[1,2,3,4,5]
    adj=[[],[],[],[],[]]
    
    for i in range(5):
        file = open(str(i+1)+".txt","r").read().split()
        for j in standardNum :
            if re.match(pattern,str(j)):
                if str(j) != str(i+1):
                    if str(j) in file :
                        adj[i].append(1)
                    else:
                        adj[i].append(0)
                else:
                    adj[i].append(0)
                
            else:
                pass
    # print("adjacentMatrix",adj )
    return adj

def Authority_Hubs(adj):
    dic={}
    standardNum=[1,2,3,4,5]
    initHubVector=np.array([1,1,1,1,1])
    adjT=np.array(adj).T
    AuthorityVector = np.dot(adjT,initHubVector)
    updatedHubVector=np.dot(adj,AuthorityVector)

    for i in range(20) :
        AuthorityVectorNormalized=AuthorityVector/math.sqrt(np.sum(np.square(AuthorityVector)))
        updatedHubVectorNormalized=updatedHubVector/math.sqrt(np.sum(np.square(updatedHubVector)))
        AuthorityVector = np.dot(adjT,updatedHubVectorNormalized)
        updatedHubVector=np.dot(adj,AuthorityVectorNormalized)

    for i in range(5) :
        dic["doc"+str(standardNum[i])]={'H':round(updatedHubVectorNormalized[i],3),
        'A':round(AuthorityVectorNormalized[i],3)}

    result=sorted(dic,key=lambda x : dic[x]['A'])
    finalResult={}
    
    for i in result :
        finalResult[i]=dic[i]
    return finalResult

def egdsValue(adj):
    ed=[]
    for filenum in range(5):
        for match in range(5):
            if adj[filenum][match]==1:
                if filenum+1!=match+1:
                    ed.append((str(filenum+1),str(match+1)))
    # print(ed)
    return(ed)


def drawDirectedGraph():
    
    G = nx.DiGraph()
    G.add_edges_from(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
        ])

    nodeColor=['gold']
    edgColor=['black']
    # Specify the edges you want here
    # print()
    # print(adjMatrix())
    red_edges = egdsValue(adjMatrix())
    # print(red_edges)
    edge_colours = ['black' if not edge in red_edges else 'green'
                    for edge in G.edges()]
    black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                        node_color = nodeColor, node_size = 300)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color=edgColor, arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.savefig("simple_path.png")
    shutil.move("/Users/HassanMahmoud/Desktop/IR Section/simple_path.png", "/Users/HassanMahmoud/Desktop/IR Section/vectorSpace/static/simple_path.png")
    plt.clf()
    return 
  

#ــــــــــــــــــــــFLASK start hereـــــــــــــــــــــــ 

app = Flask(__name__)

@app.route('/بتوليد حروف', methods=['GET','POST'])
def form2():
    if request.method == 'POST':
        # print("first",adjMatrix())
        
        document1 = GenerateAndWrite("1").read().split()
        document2 = GenerateAndWrite("2").read().split()
        document3 = GenerateAndWrite("3").read().split()
        document4 = GenerateAndWrite("4").read().split()
        document5 = GenerateAndWrite("5").read().split()
        drawDirectedGraph()

        inputDATAT = request.form['queryinput']
        pattern = r"^([A-E][ ])+$"
        if not(re.match(pattern,inputDATAT)):
            msg="please enter the query like this : A B A A B C"
            result=""
            txt1=""
            txt2=""
            txt3=""
            txt4=""
            txt5=""
            listR={}
        else:
            msg=""
            queryData = str(inputDATAT).split()
            txt1=document1
            txt2=document2
            txt3=document3
            txt4=document4
            txt5=document5
            result = Run(queryData)
            listR=Authority_Hubs(adjMatrix())
            print("third",adjMatrix())

            try:
                line_chart = pygal.Bar()
                line_chart.title = 'Authority and hubness weights' 
                line_chart.x_labels = map(str, range(1,6))
                Authority=[]
                Hubness=[]
                for docname , HAscore in Authority_Hubs(adjMatrix()).items():
                    Authority.append(HAscore['A'])
                    Hubness.append(HAscore['H'])
                line_chart.add('Authority', Authority)
                line_chart.add('Hubness', Hubness)
                graph_data = line_chart.render_data_uri()
            except Exception as e:
                return(str(e))
        return render_template('homePage2.html',query=result,file1=txt1,file2=txt2,file3=txt3,file4=txt4,file5=txt5,error=msg,list=listR , graph=graph_data,dirctedG="simple_path.png",picPath="../static/simple_path2.png")
    return render_template('homePage2.html',query="",error="",list={},graph="",dirctedG="")


@app.route('/منغير توليد حروف', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        drawDirectedGraph()
     
        inputDATAT = request.form['queryinput']
        pattern = r"^([A-E][ ])+$"
        if not(re.match(pattern,inputDATAT)):
            msg="please enter the query like this : A B A A B C"
            result=""
        else:
            msg=""
            queryData = str(inputDATAT).split()
            result = Run(queryData)
            listR=Authority_Hubs(adjMatrix())
            try:
                line_chart = pygal.Bar()
                line_chart.title = 'Authority and hubness weights' 
                line_chart.x_labels = map(str, range(1,6))
                Authority=[]
                Hubness=[]
                for docname , HAscore in Authority_Hubs(adjMatrix()).items():
                    Authority.append(HAscore['A'])
                    Hubness.append(HAscore['H'])
                line_chart.add('Authority', Authority)
                line_chart.add('Hubness', Hubness)
                graph_data = line_chart.render_data_uri()
            except Exception as e:
                return(str(e))
        return render_template('homePage.html',query=result,error=msg,list=listR,graph=graph_data,dirctedG="simple_path.png")
    return render_template('index.html',query="",error="",list={})
if __name__ == '__main__':
	app.debug = True
	app.run()
    
    
