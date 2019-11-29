import numpy as np


def fillMatRow(sgn1, sgn2, convMat, index):
    m = len(sgn1)
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


def makePerConv(sgnPer, sgnFin):
    tempArray = makeConv(sgnPer, sgnFin)
    size = len(sgnPer)
    conv = []
    subArray1 = tempArray[:size]
    subArray2 = tempArray[size:]

    if(len(subArray1) != len(subArray2)):
        for i in range(len(subArray1)-len(subArray2)):
            subArray2.append(0)

    for i in range(size):
        conv.append(subArray1[i]+subArray2[i])
    return conv


def perConv(sgnPer, sgnFin):
    conv = []
    result = []
    sum = 0

    tempArray = makeConv(sgnPer, sgnFin)

    size = len(sgnPer)

    while (len(tempArray) % size) != 0:
        tempArray.append(0)

    splitIndex = len(tempArray)/size
    tempArray = np.asarray(tempArray)
    conv = np.split(tempArray, splitIndex)

    for i in range(size):
        for j in range(len(conv)):
            sum = sum+conv[j][i]
        result.append(sum)
        sum = 0
    return(result)
