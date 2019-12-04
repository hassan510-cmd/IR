import numpy as np
import math
import matplotlib.pyplot as plt
import shutil

import plotly.graph_objects as go

import networkx as nx
# from plotly.graph_objects.surface.contours import x
d1=[1,2,4]
d2=[2,3,4,5]
d3=[2,1,5]
d4=[5]
d5=[5,3,1]
standardNum=[1,2,3,4,5]
adj=[[],[],[],[],[]]

adj[0].append(1)
print(adj)
# dic={}
# def Authority_Hubs():
#     import re
#     pattern=r'^[1-5]$'

#     standardNum=[1,2,3,4,5]
#     adj=[[],[],[],[],[]]
#     dic={}

    # for i in range(5):
    #     file = open(str(i+1)+".txt","r").read().split()
    #     for j in standardNum :
    #         if re.match(pattern,str(j)):
    #             if str(j) in file :
    #                 adj[i].append(1)
    #             else:
    #                 adj[i].append(0)
    #         else:
    #             pass
    # print(adj) 
    # return adj

# def egdsValue(adj):
#     ed=[]
#     for filenum in range(5):
#         for match in range(5):
#             if adj[filenum][match]==1:
#                 if filenum+1!=match+1:
#                     ed.append((str(filenum+1),str(match+1)))
#     print(ed)
#     return(ed)



# def drawDirectedGraph():
    # G = nx.DiGraph()
    # G.add_edges_from(
    #     [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
    #     ])

    # nodeColor=['gold']
    # edgColor=['black']
    # # Specify the edges you want here
    # red_edges = egdsValue(Authority_Hubs())

    # edge_colours = ['black' if not edge in red_edges else 'green'
    #                 for edge in G.edges()]
    # black_edges = [edge for edge in G.edges() if edge not in red_edges]

    # # Need to create a layout when doing
    # # separate calls to draw nodes and edges
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
    #                     node_color = nodeColor, node_size = 500)
    # nx.draw_networkx_labels(G, pos)
    # nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color=edgColor, arrows=True)
    # nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    # plt.savefig("simple_path.png") # save as png

    # plt.show()

# shutil.move("aaa.png", "IR Section/vectorSpace/static/")
# Authority_Hubs()
# drawDirectedGraph()
# shutil.move("/Users/HassanMahmoud/Desktop/IR Section/vectorSpace/static/simple_path.png", "/Users/HassanMahmoud/Desktop/IR Section/vectorSpace/static/simple_path.png")
# /Users/HassanMahmoud/Desktop/IR Section/aaa.png

    # initHubVector=np.array([1,1,1,1,1])
    # adjT=np.array(adj).T
    # AuthorityVector = np.dot(adjT,initHubVector)
    # updatedHubVector=np.dot(adj,AuthorityVector)
    # print("AuthorityVector",AuthorityVector)
    # print("updatedHubVector",updatedHubVector)
    # for i in range(21):
    #     AuthorityVector = np.dot(adjT,updatedHubVector)
    #     updatedHubVector=np.dot(adj,AuthorityVector)
    #     print("AuthorityVector"+str(i+1),AuthorityVector)
    #     print("updatedHubVector"+str(i+1),updatedHubVector)
    #     print()
    # for i in range(5) :
    #     dic["doc"+str(standardNum[i])]={'H':updatedHubVector[i],
    #     'A':AuthorityVector[i]}
    # print(dic)
    # # result = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]))
    # result=sorted(dic,key=lambda x : dic[x]['A'])
    # finalResult={}
    
    # for i in result :
    #     finalResult[i]=dic[i]
    # return finalResult


# # for docName , HAscore in Authority_Hubs():
# #     print("DocumentName : ",end=" ")
# #     print(str(docName).ljust(5),end=" ")
# #     print("Hub Score ",str(HAscore['H']).ljust(5),end=" ")
# #     print("Authority Score ",str(HAscore['A']).ljust(5),end=" ")
# #     # HAscore['H']
# #     # print(HAscore)
# #     # for key , value in HAscore.items():
# #     #     print(str(value).ljust(7),end=" ")
# #     #     print("A",end=" ")
# #         # print(h.ljust(7),a,end=" ")
# #     print()
# # ________________________________________________________________________________________________________ 

# initHubVector=np.array([1,1,1,1])
# adjT=np.array([[0,0,1,0],[1,0,0,0],[1,1,0,0],[1,1,1,1]]).T
# AuthorityVector = np.dot([[0,0,1,0],[1,0,0,0],[1,1,0,0],[1,1,1,1]],initHubVector)
# updatedHubVector=np.dot(adjT,AuthorityVector)
# print("AuthorityVector",AuthorityVector)
# print("updatedHubVector",updatedHubVector)
# # print("np.square(AuthorityVector)",np.square(AuthorityVector))
# # print("")
# for i in range(21) :
#     AuthorityVectorNormalized=AuthorityVector/math.sqrt(np.sum(np.square(AuthorityVector)))
#     updatedHubVectorNormalized=updatedHubVector/math.sqrt(np.sum(np.square(updatedHubVector)))
# # l=np.square([1,2,3,4])/np.sum([1,2,3,4])

# print("AuthorityVectorNormalized",AuthorityVectorNormalized)
# print("updatedHubVectorNormalized",updatedHubVectorNormalized)
# # for i in range(21):
# #     AuthorityVector = np.dot(adjT,updatedHubVector)
# #     updatedHubVector=np.dot([[0,0,1,0],[1,0,0,0],[1,1,0,0],[1,1,1,1]],AuthorityVector)
# #     print("AuthorityVector"+str(i+1),AuthorityVector)
# #     print("updatedHubVector"+str(i+1),updatedHubVector)
# #     print()
# # print(AuthorityVector)
# # print(updatedHubVector)

# dic={}
# for i in range(4) :
#     dic["doc"+str(standardNum[i])]={'H':updatedHubVector[i],
#     'A':AuthorityVector[i]}
# # print(dic)
# result=sorted(dic,key=lambda x : dic[x]['A'])
# print(result)

# egds=[
#     ('1','x'),('1','z'),('1',''),('1',''),('1',''),
#     ('1',''),('1',''),('1',''),('1',''),('1',''),
#     ('1',''),('1',''),('1',''),('1',''),('1',''),
#     ('1',''),('1',''),('1',''),('1',''),('1',''),
#     ('1',''),('1',''),('1',''),('1',''),('1',''),
#     ('1',''),('1',''),('1',''),('1',''),('1',''),]


# list=list(egds)
# # for i in range(5) :
# #     for j in range(5):
# #         list[i][j]="x"
# # t=tuple(list)
# list[0][1]="zzzz"
# print(list)


# a=[ 
#     (1,0),
#     (1,1),
#     (0,1)]
# a.append((5,8))
# print(a)