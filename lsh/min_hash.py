import numpy as np
import random
import hashlib
import sys

bands=20
rows=5

def getMd5Hash(band):
    hashobj=hashlib.md5()
    hashobj.update(band.encode())
    hashValue = hashobj.hexdigest()
    return hashValue

def getHashBuket(sigMatrix,r):
    hashBuckets={}
    begin=0
    end=r
    b_index = 1

    while end <= sigMatrix.shape[0]:
        for colNum in range(sigMatrix.shape[1]):
            band = str(sigMatrix[begin: end, colNum])+str(b_index)
            hashValue=getMd5Hash(band)
            if hashValue not in hashBuckets:
                hashBuckets[hashValue] = [colNum]
            elif colNum not in hashBuckets[hashValue]:
                hashBuckets[hashValue].append(colNum)
        begin += r
        end += r
        b_index += 1
    return hashBuckets

def getSigMatricx(input_matrix, n):
    result = []
    for i in range(n):
        sig = doSig(input_matrix)
        result.append(sig)
    return np.array(result)

def doSig(inputMatrix):
    seqSet = [i for i in range(inputMatrix.shape[0])]
    result = [-1 for i in range(inputMatrix.shape[1])]
    count = 0

    while len(seqSet) > 0:
        randomSeq = random.choice(seqSet)
        for i in range(inputMatrix.shape[1]):
            if inputMatrix[randomSeq][i] != 0 and result[i] == -1:
                result[i] = randomSeq
                count += 1

        if count == inputMatrix.shape[1]:
            break

        seqSet.remove(randomSeq)

    # return a list
    return result

def minhash(dataset, b, r):
    inputMatrix=np.array(dataset).T #将dataset转置一下
    sigMatrix=getSigMatricx(inputMatrix,b*r)#得到签名矩阵
    hashBuket=getHashBuket(sigMatrix,rows)#得到hash字典
    return hashBuket

def __deleteCopy(group,copy,g1):
    for g2 in group:
        if g1 != g2:
            if set(g1) - set(g2) == set():
                copy.remove(g1)
                return

def sepGroup(hashBuket):
    group=set()
    for v in hashBuket.values():
        group.add(tuple(v))

    copy=group.copy()

    for g1 in group:
        __deleteCopy(group,copy,g1)

    return copy


def play(documents):
    hashBuket=minhash(documents,bands,rows)
    groups=sepGroup(hashBuket)  #将相似item聚类起来
    print(groups)



documents=[[1,1,0,1,1,1],[1,1,0,1,1,1],[0,0,1,1,1,0],[1,1,1,0,0,0],[1,1,1,0,1,0],[1,1,1,1,1,0]]

play(documents)


