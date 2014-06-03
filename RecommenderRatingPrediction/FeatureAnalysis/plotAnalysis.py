from FeatureExtraction.com import removeNTail


def accumulateRate(userRateDict,splitN,TailN):
    rateList = []
    rateLen = len(userRateDict)
    clickNoPurchaseNum = 0
    for line in userRateDict:
        if (line[-1] != 0)&( line[1]!= None):
            rateList.append(line[-1])
        else:
            # calculate the clickNoPurchaseNum and rate
            clickNoPurchaseNum+=1
    clickNoPurchaseRate = float(clickNoPurchaseNum)/rateLen
    maxRate = max(rateList)
    minRate = min(rateList)
    step = removeNTail((maxRate-minRate)/splitN,TailN)
    boundList = [minRate+i*step for i in range(splitN+1)]
    intervalNum = [0 for i in range(len(boundList)-1)]
    for i in range(len(boundList)-2):
        for rate in rateList:
            if (rate >= boundList[i])&(rate<=boundList[i+1]):
                intervalNum[i]+=1
    downBound = boundList[-2]
    for rate in rateList:
        if(rate>=boundList[i])&(rate<=boundList[i+1]):
            intervalNum[-1]+=1
    print intervalNum
    accumulateRate = [float(sum(intervalNum[0:i]))/sum(intervalNum) for i in range(len(intervalNum))]
    accumulateRate.append(1)
    return accumulateRate, clickNoPurchaseRate, boundList