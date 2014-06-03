import math

from BuildInfluenceMatrix.Utils import tailDigit


def getInfluenceMatrix(followMatrix, forwardMatrix, digitN, followK, forwardK):
    num = len(followMatrix)
    influenceMatrix = [[0 for i in range(num)] for j in range(num)]
    # for i Matrix[i] stands for his attentions for others... 
    for i in range(num):
        sumAttention = sum(followMatrix[i])
        if sumAttention != 0:
            for j in range(num):
                if followMatrix[i][j]!=0:
                    influenceMatrix[i][j] = math.log(sumAttention/float(followMatrix[i][j]))
                    influenceMatrix[i][j] = tailDigit(influenceMatrix[i][j], digitN)*followK
    print influenceMatrix[3]
    # for i Matrix[i] stands for his attentions for others... 
    for i in range(num):
        sumAttention = sum(forwardMatrix[i])
        if sumAttention != 0:
            for j in range(num):
                if forwardMatrix[i][j]!=0:
                    influenceMatrix[i][j] = math.log(sumAttention/float(forwardMatrix[i][j]))
                    influenceMatrix[i][j] = + tailDigit(influenceMatrix[i][j], digitN)*forwardK
    print influenceMatrix[3]
    return influenceMatrix
                    
    