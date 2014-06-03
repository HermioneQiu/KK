def splitByTime(List, timeList, timeSlot):
    maxTime = max(timeList)
    minTime = min(timeList)
    timeBound = range(int(minTime*100),int(maxTime*100),int(timeSlot*100))
    timeBound = [float(tmp)/100 for tmp in timeBound]
    timeBound.append(maxTime)
    print timeBound
    splitList = [[] for i in range(len(timeBound))]
    splitBrand = [[] for i in range(len(timeBound))]
    splitUser = [[] for i in range(len(timeBound))]
    for line in List:
        time = line[-1]
        for i in range(len(timeBound)-1):
            lowBound = timeBound[i]
            highBound = timeBound[i+1]
            if (time>=lowBound)&(time<highBound):
                splitList[i].append(line)
                splitUser[i].append(line[0][0])
                splitBrand[i].append(line[0][1])
    return splitList, splitUser, splitBrand

# when compareNum is 1, it stands for the comparation between too neighbor
def TimeAnalysis(splitBrand):
    DupliRate = []
    Novelrate = []
    for i in range(len(splitBrand)-1):
        compareLists = splitBrand[i:i+2]
        list1 = set(compareLists[0])
        list1Num = len(list1)
        list2 = set(compareLists[1])
        list2Num =len(list2)
        if list1Num != 0:
            dupliNum = 0
            for brand in list2:
                if brand in list1:
                    dupliNum+=1
            DupliRate.append(float(dupliNum)/list1Num)
            Novelrate.append(float(list2Num-dupliNum)/list1Num)
        else:
            DupliRate.append(0)
            Novelrate.append(0)
    return DupliRate, Novelrate



        