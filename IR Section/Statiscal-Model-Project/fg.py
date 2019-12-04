import numpy
# li = '<A:0.2;B:0.9;D:0.8>'
# print(2 & 1)
# li.replace("A", "x")
# print("string after replacement :", li.replace(
#     ";", " ").replace("<", "").replace(">", ""))
# query = li.replace(
#     ";", ":").replace("<", "").replace(">", "").split(":")
# li1 = li.split(';')
# li2 = li1.copy()
# print(query)
# dic = {}
# for index, key in enumerate(query):
#     if not index & 1:
#         oldkey = key
#         # print("index", index)
#         # print("va", key)
#         dic[oldkey] = ""
#     else:
#         dic[oldkey] = key

# print(dic)


# def Machine(li):
#     dic = {}
#     query = li.replace(
#         ";", ":").replace("<", "").replace(">", "").split(":")
#     for index, key in enumerate(query):
#         if not index & 1:
#             oldkey = key
#             # print("index", index)
#             # print("va", key)
#             dic[oldkey] = ""
#         else:
#             dic[oldkey] = key
#     x = numpy.array(dic).reshape(1, 1)
#     # print("fdgd", x)
#     return dic


# aa = [1, 2, 3, 4, 5, 6, 7]
# for i in Machine('<A:0.2;B:0.9;D:0.8>'):
#     print(Machine('<A:0.2;B:0.9;D:0.8>')[i])
#     print(Machine('<A:0.2;B:0.9;D:0.8>')[i])
# lo = []
# for i in li1:
#     if i.isnumeric:
#         lo.append(i)
#     else:
#         print("no")
# print("fdgdfgd", lo)

# dic = {
#     "mem04": 5,
#     "mem2": 2,
#     "mem45": 12,
#     "mem2": 18,
#     "mem7": 200,
#     "mem6": 7,
#     "mem1": 1800,
# }
# print(dic)/

list = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]))
print(list)

# for i in dic:
#     list.append(i)
# list.sort(reverse=True)
# print(list)
# for k in list:
#     print(dic[k], k)


# oppo = []
# max = di['a']
# for key in l:
#         if qq[key] > max:
#             max = qq[key]
#             k = key
#             oppo.append(str(max)+':'+k)
# list = [1,2,5,4,1,3,6,2,8,2,1,9,5,1,7,2,3,5,1,5]
# max =list[0]
# for i in list :
#     if i>max:
#         max =i
