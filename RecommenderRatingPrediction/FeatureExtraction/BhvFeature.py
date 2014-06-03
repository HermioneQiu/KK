# ignore the time factor, see the time  as a filter factor
# List[0]---[[userId, brandId, mark], dateNum]
import copy
from com import removeNTail

# main
def bhvFeatureExtract(List,Ntail):
    clickDict = {}
    purchaseDict = {}
    collectDict = {}
    purchasecarDict = {}
    for line in List:
        userId, brandId, mark = line[0]
        # click
        if mark == '0':
            clickDict = buildDict(userId, brandId, clickDict)
        # purchase
        if mark == '1':
            purchaseDict = buildDict(userId, brandId, purchaseDict)
        # collect
        if mark == '2':
            collectDict = buildDict(userId, brandId, collectDict)
        # purchasecar
        if mark == '3':
            purchasecarDict = buildDict(userId, brandId, purchasecarDict)
    click2RateDict = bhv2Rate(clickDict, Ntail)
    purchasecar2RateDict = bhv2Rate(purchasecarDict, Ntail)
    collect2RateDict = bhv2Rate(collectDict, Ntail)
    purchase2RateDict = bhv2Rate(purchaseDict, Ntail)
    DictList = click2RateDict, purchasecar2RateDict, collect2RateDict, purchase2RateDict 
    bhvDictList = clickDict, purchasecarDict, collectDict, purchaseDict
    return DictList, bhvDictList
# main
def bhvFeature2Rate(DictList, weightList, userDict, brandDict):
    clickDict, purchaseDict, collectDict, purchasecarDict = DictList
    # rateMatrix
    userNum = len(userDict)
    brandNum = len(brandDict)
    rateMatrix = initRateMatrix(userNum, brandNum)
    # update rateMatrix
    for i in range(len(DictList)):
        weight = weightList[i]
        Dict = DictList[i]
        for userId in Dict.keys():
            for brandId in Dict[userId].keys():
                user_i = userDict[userId]
                brand_i = brandDict[brandId]
                rateMatrix[user_i][brand_i] += Dict[userId][brandId]*weightList[i]
        
    return rateMatrix
# function
def buildDict(userId, brandId, Dict):
    if userId not in Dict.keys():
        Dict[userId] = {brandId:1}
    else:
        if brandId not in Dict[userId]:
            Dict[userId][brandId]=1
        else:
            Dict[userId][brandId]+=1
    return Dict
# function
# change the {userId{brandId:times;...}}
# to the {userId{brandId:score;....}}
# ******* need improvement********
def bhv2Rate(bhvDict,Ntail):
    bhv2RateDict = copy.deepcopy(bhvDict)
    for userId in bhvDict.keys():
        times =[]
        for brandId in bhvDict[userId].keys():
            times.append(bhvDict[userId][brandId])
        maxTimes = max(times)
        minTimes = min(times)
        for brandId in bhvDict[userId].keys():
            if(maxTimes == minTimes):
                rating = 1
            else:
                TimesLen = maxTimes - minTimes
                minTimes = minTimes - TimesLen/float(5)
                rating = float(bhvDict[userId][brandId]-minTimes)/(maxTimes-minTimes)
                rating = removeNTail(rating, Ntail)
            bhv2RateDict[userId][brandId] = rating
    return bhv2RateDict
# function
def initRateMatrix(userNum, brandNum):
    rateMatrix = [[0 for i in range(brandNum)] for j in range(userNum)]
    return rateMatrix
    

    

 
        
