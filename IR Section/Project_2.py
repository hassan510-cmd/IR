from flask import Flask, redirect, url_for, request, render_template
import numpy as np
import math
from random import randint

resultDic = {}


def randomchar():
    s = randint(10, 20)
    str = ""
    for i in range(0, s):
        str += chr(randint(65, 69)) + " "
    return str


def inputstringinfile(filename, x):
    f = open(filename, "w")
    f.write(x)
    f.close()


def readfromfile(filename):
    f = open(filename).read()
    return f


def termfrequency(x):
    d = {}
    for i in range(0, len(x)):
        char = x[i]
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    del d[" "]
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    for i in d:
        d[i] = d[i] / max
    return d


def idf(a={}, b={}, c={}, e={}, f={}, g={}):
    characters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                  "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
                  "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    for i in characters:
        count = 0
        if i in a:
            count += 1
        if i in b:
            count += 1
        if i in c:
            count += 1
        if i in e:
            count += 1
        if i in f:
            count += 1
        if i in g:
            count += 1
        if count == 0:
            characters[i] = 0
        else:
            characters[i] = math.log((6 / count), 2)
    return characters


def idftf(tf={}, idf={}):
    for i in tf:
        if i in idf:
            tf[i] = tf[i] * idf[i]
    return tf


def innerproduct(tf1={}, tf2={}):
    d = 0
    for i in tf1:
        if i in tf2:
            d += tf1[i] * tf2[i]
    return d


def sigmamul(tf1={}):
    d = 0
    for i in tf1:
        d += math.pow(tf1[i], 2)
    return d


def cossim(innerproduct1, multi1, multi2):
    d = (innerproduct1 / (math.sqrt(multi1 * multi2)))
    return d


def main(query):
    dm = []
    for i in range(1, 6):
        dm.append(readfromfile("d" + str(i) + ".txt"))

    for i in range(0, len(dm)):
        dm[i] = termfrequency(dm[i])

    query = termfrequency(query)

    idfd = idf(dm[0], dm[1], dm[2], dm[3], dm[4], query)

    for i in range(0, len(dm)):
        dm[i] = idftf(dm[i], idfd)

    query = idftf(query, idfd)
    file = {}
    for i in range(0, len(dm)):
        file.update({("D" + str(i + 1)): cossim(innerproduct(dm[i], query), sigmamul(dm[i]), sigmamul(query))})
    sorted_score = sorted(file.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_score


def create_matrix_with_val():
    matrix = []
    x = 1
    for i in range(0, 5):
        matrix.append([])
        f = readfromfile("d" + str(x) + ".txt")
        x += 1
        for j in range(1, 6):
            if (i + 1) == j:
                matrix[i].append(0)
            else:
                if str(j) in f:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)

    return matrix


def authority():
    original = create_matrix_with_val()

    hub = np.array([1, 1, 1, 1, 1])

    mx = np.array(original)
    adjacenttranspose = np.array(mx).T
    print(np.array(mx).T)
    A = np.dot(adjacenttranspose, hub)
    hub2 = np.dot(mx, A)

    # print(A)
    

    for i in range(19):
        A_normalized = np.divide(A, math.sqrt(np.sum(np.square(A))))
        hub_normalized = np.divide(hub2, math.sqrt(np.sum(np.square(hub2))))
        A = np.dot(adjacenttranspose, hub_normalized)
        hub2 = np.dot(mx, A_normalized)

       
    print("A_normalized",A_normalized)
    print("hub_normalized",hub_normalized)
    return hub2


# print(create_matrix_with_val())

authority()

# app = Flask(__name__)
#
#
# @app.route('/')
# def home():
#     return render_template('home.html')
#
#
# @app.route('/', methods=['POST', 'GET'])
# def start():
#     if request.method == 'POST':
#         query = request.form['query']
#         return render_template("result.html", list=main(query))
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
