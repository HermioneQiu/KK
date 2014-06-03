from DataProcess.DataTransform import DataTimeTransfrom
from FeatureAnalysis.TimeFeature import splitByTime, TimeAnalysis
from FeatureExtraction.BhvFeature import bhvFeatureExtract, bhvFeature2Rate
from FeatureExtraction.buildDict import buildUserBrandDict
from Utils.File import *


if __name__=="__main__":
    
    rootDir = 'E:\\workspace\\DATA\\Reco'
    
    rawDataDir = rootDir + '\\all.data'
    rawDataFile = File(rawDataDir)
    # the symbol that split elements in a line
    symbol = ','
    head = True
    List = rawDataFile.readLine2List(symbol, head)
    timeTransferedList,timeList = DataTimeTransfrom(List)
    print timeTransferedList[0]
    # for rate building process
    userDict, brandDict = buildUserBrandDict(timeTransferedList)
    # save userDict and brandDict
    userDictDir = rootDir + '\\user.dict'
    brandDictDir = rootDir + '\\brand.dict'
    userDictFile = File(userDictDir)
    brandDictFile = File(brandDictDir)
    userDictFile.writeDict(userDict)
    print 'writting userDict'
    brandDictFile.writeDict(brandDict)
    print 'writting brandDict'
    # save dict
    print len(userDict), len(brandDict)
    Ntail =4
    DictList, bhvDictList = bhvFeatureExtract(timeTransferedList, Ntail)

    # save rateDictList
    DictListDir = [rootDir+'\\clickRate.dict',
                   rootDir+'\\purchasecarRate.dict',
                   rootDir+'\\collectRate.dict',
                   rootDir+'\\purchaseRate.dict']
    for i in range(len(DictListDir)):
        DictFile = File(DictListDir[i])
        DictFile.writeDictDict(DictList[i])
    print len(DictList)
    # save bhvDictList
    bhvDictListDir = [rootDir+'\\clickTimes.dict',
                   rootDir+'\\purchasecarTimes.dict',
                   rootDir+'\\collectTimes.dict',
                   rootDir+'\\purchaseTimes.dict']
    for i in range(len(bhvDictListDir)):
        DictFile = File(bhvDictListDir[i])
        DictFile.writeDictDict(bhvDictList[i])
    print len(DictList)
    
    weightList = [1,1,1,2]
    rateMatrix = bhvFeature2Rate(DictList, weightList, userDict, brandDict )
    # save rate Matrix
    rateMatrixDir = rootDir + '\\rate.matrix'
    rateMatrixFile = File(rateMatrixDir)
    rateMatrixFile.writeMatrix(rateMatrix)
    print 'finished'
    
    