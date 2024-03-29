import numpy as np


def fillMatRow(sgn1, sgn2, convMat, index):
    m = len(sgn1)
    n = len(sgn2)
    for i in range(m):
        convMat[index][i+index] = sgn1[i]*sgn2[index]
    return convMat


def fillMat(sgn1, sgn2, convMat):
    for i in range(len(sgn2)):
        fillMatRow(sgn1, sgn2, convMat, i)
    return convMat


def makeConv(sgn1, sgn2):
    convMat = np.zeros((len(sgn2), len(sgn1)+len(sgn2)-1))
    convMat = fillMat(sgn1, sgn2, convMat)
    convArray = []
    sum = 0
    for i in range(len(sgn1)+len(sgn2)-1):
        for j in range(len(sgn2)):
            sum = sum + convMat[j][i]
        convArray.append(sum)
        sum = 0
    return convArray
