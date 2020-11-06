import numpy as np
import random

def getHash(v,x,b,w):
    return (v.dot(x)+b)//w

def dealOneBuket(dataSet):
    dataSet=np.array(dataSet)

    k = dataSet.shape[1]
    b = random.uniform(0, w)
    x = np.random.random(k)
    buket=[]
    for data in dataSet:
        h=getHash(data,x,b,w)
        buket.append(h)
    return buket

def dealMoreBuket(dataSet,n):
    for _ in range(n):
        print(dealOneBuket(dataSet))


dataSet=[[8,7,6,4,8,9],[7,8,5,8,9,7],[3,2,0,1,2,3],[3,3,2,3,3,3],[21,21,22,99,2,12],[1,1,1,0,1,0],[1,1,1,1,1,0]]
dataSet=np.array(dataSet)

w = 4
n=6
dealMoreBuket(dataSet,n)