from FeatureExtraction.com import *
def bhvWithPurchase(bhvRateDict, purchaseRateDict, tailN):
    # calculate the correct rate
    userPreciseRate = []
    userRecallRate = []
    userRankAvr = []
    for userId in bhvRateDict.keys():
        preciseNum = 0
        bhvLine = bhvRateDict[userId]
        if userId in purchaseRateDict.keys():
            purchaseLine = purchaseRateDict[userId]
            for brandId in bhvLine.keys():
                if brandId in purchaseLine.keys():
                    preciseNum += 1
            preciseRate = float(preciseNum)/len(purchaseLine)
            preciseRate = removeNTail(preciseRate, tailN)
            recallRate = float(preciseNum)/len(bhvLine)
            recallRate = removeNTail(recallRate, tailN)
        else:
            preciseRate = 0
            recallRate = 0
        userPreciseRate.append([userId,preciseRate])
        userRecallRate.append([userId,recallRate])
    for userId in bhvRateDict.keys():
        bhvLine = bhvRateDict[userId]
        if userId in purchaseRateDict.keys():
            sortDict = sortDictValue(bhvLine)
            rankSum = 0
            rankNum = 0
            for brandId in bhvLine.keys():
                rankNum += 1
                rankSum += sortDict[brandId][-1]
            rankAvr = float(rankSum)/rankNum
            rankAvr = removeNTail(rankAvr, tailN)
        else:
                rankAvr = None
        userRankAvr.append([userId,rankAvr])
    return userPreciseRate, userRecallRate, userRankAvr
def sortDictValue(Dict):
    sortDict = dict()
    valList = []
    for key in Dict.keys():
        valList.append(Dict[key])
    sortValList = sorted(valList,reverse=True)
    tmpList = []
    # 1 stands for the highest rank
    tmpIndex =0
    tmpVal = 0
    for val in sortValList:
        for key in Dict.keys():
            if (val == Dict[key]) &(key not in tmpList):
                tmpList.append(key)
                if (tmpVal!=val):
                    tmpIndex += 1
                sortDict[key]=[val,tmpIndex]
                tmpVal = val
    return sortDict