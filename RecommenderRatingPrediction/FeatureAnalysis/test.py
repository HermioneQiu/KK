from DataProcess.DataTransform import DataTimeTransfrom
from FeatureAnalysis.TimeFeature import splitByTime, TimeAnalysis
from FeatureAnalysis.bhvAnalysis import sortDictValue, bhvWithPurchase
from FeatureAnalysis.plotAnalysis import accumulateRate
from FeatureExtraction.BhvFeature import bhvFeatureExtract, bhvFeature2Rate
from FeatureExtraction.buildDict import buildUserBrandDict
from Utils.File import *

import matplotlib.pyplot as plt
import numpy as np

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
    #userDict, brandDict = buildUserBrandDict(timeTransferedList)
    Ntail= 4
    DictList, bhvDictList = bhvFeatureExtract(timeTransferedList, Ntail)
    # feature analysis
    clickRateDict, purchasecarRateDict, collectRateDict, purchaseRateDict = DictList
    # the relationship between clickRate  and  purchaseDict
    
    # -------------click plot----------------------------------------
    userClickPreciseRate,userClickRecallRate, userClickRankAvr = bhvWithPurchase(clickRateDict, purchaseRateDict, Ntail)
    '''
    # save Rate val
    bhvWord = '\\click'
    userPreciseRateDir = rootDir + bhvWord+'Precise.list'
    userRecallRateDir = rootDir +bhvWord+ 'Recall.list'
    userRankAvrDir = rootDir +bhvWord+ 'Rank.list'
    userPreciseRateFile = File(userPreciseRateDir)
    userRecallRateFile = File(userRecallRateDir)
    userRankAvrFile = File(userRankAvrDir)
    userPreciseRateFile.writeRateList(userPreciseRate)
    userRecallRateFile.writeRateList(userRecallRate)
    userRankAvrFile.writeRateList(userRankAvr)
    '''
    splitN =8
    TailN = 4
    '''
    accumulateClickPreciseRate, clickNoPurchaseRate,  clickPreciseboundList = accumulateRate(userClickPreciseRate,splitN,TailN)   
    accumulateClickRecallRate, clickNoPurchaseRate, clickRecallboundList = accumulateRate(userClickRecallRate,splitN,TailN)
    accumulateClickRank, clickNoPurchaseRate, clickRankboundList = accumulateRate(userClickRankAvr,splitN,TailN)

    # for plot
    plt.figure('click rate')
    plt.plot(clickPreciseboundList, accumulateClickPreciseRate, label='accuClickPreciseRate')
    plt.plot(clickRecallboundList, accumulateClickRecallRate, label='accuClickRecallRate')
    plt.scatter(clickPreciseboundList, accumulateClickPreciseRate)
    plt.scatter(clickRecallboundList, accumulateClickRecallRate)
    plt.xlabel('ClickPreciseRate/ClickRecallRate')
    plt.ylabel('accumulateClickPreciseRate/accumulateClickRecallRate')
    plt.title('the relationship between Click and Purchase')
    plt.legend()

    plt.figure('click rank')
    plt.plot(clickRankboundList, accumulateClickRank, label='accuClickRank')
    plt.scatter(clickRankboundList, accumulateClickRank)
    plt.xlabel('Rank of clickBrand')
    plt.ylabel('accumulateRate of clickBrand rank')
    plt.legend()
    print 'click clickNoPurchaseRate: '
    print clickNoPurchaseRate
    '''
    # ------purchasecar----------------------
    userPurchasecarPreciseRate,userPurchasecarRecallRate, userPurchasecarRankAvr = bhvWithPurchase(purchasecarRateDict, purchaseRateDict, Ntail)
    accumulatePurchasecarPreciseRate, PurchasecarNoPurchaseRate, PurchasecarPreciseboundList = accumulateRate(userPurchasecarPreciseRate,splitN,TailN)   
    accumulatePurchasecarRecallRate, PurchasecarNoPurchaseRate, PurchasecarRecallboundList = accumulateRate(userPurchasecarRecallRate,splitN,TailN)   
    accumulatePurchasecarRank, PurchasecarNoPurchaseRate, PurchasecarRankboundList = accumulateRate(userPurchasecarRankAvr,splitN,TailN)   
    print userPurchasecarPreciseRate
    print PurchasecarPreciseboundList
    print userPurchasecarRecallRate
    print PurchasecarRecallboundList
    # for plot
    plt.figure('purchasecar rate')
    plt.plot(PurchasecarPreciseboundList, accumulatePurchasecarPreciseRate, label='accuPurPreciseRate')
    plt.plot(PurchasecarRecallboundList, accumulatePurchasecarRecallRate,label='accuPurRecallRate')
    plt.scatter(PurchasecarPreciseboundList, accumulatePurchasecarPreciseRate)
    plt.scatter(PurchasecarRecallboundList, accumulatePurchasecarRecallRate)
    plt.xlabel('purchasecarPreciseRate/purchasecarRecallRate')
    plt.ylabel('accumulatepurchasecarPreciseRate/accumulatepurchasecarRecallRate')
    plt.title('the relationship between purchasecar and Purchase')
    plt.legend()

    plt.figure('purchasecar rank')
    plt.plot(PurchasecarRankboundList, accumulatePurchasecarRank, label='accuPurcarRank')
    plt.scatter(PurchasecarRankboundList, accumulatePurchasecarRank)
    plt.xlabel('Rank of purchasecarBrand')
    plt.ylabel('accumulateRate of purchasecarBrand rank')
    plt.legend()
    print 'purchasecar purchasecarNoPurchaseRate: '
    print PurchasecarNoPurchaseRate
    '''
    # -------------collect--------------
    userCollectPreciseRate,userCollectRecallRate, userCollectRankAvr = bhvWithPurchase(collectRateDict, purchaseRateDict, Ntail)
    accumulateCollectPreciseRate, collectNoPurchaseRate, collectPreciseboundList = accumulateRate(userCollectPreciseRate,splitN,TailN)   
    accumulateCollectRecallRate, collectNoPurchaseRate, collectRecallboundList = accumulateRate(userCollectRecallRate,splitN,TailN)   
    accumulateCollectRank, collectNoPurchaseRate, collectRankboundList = accumulateRate(userCollectRankAvr,splitN,TailN)   
    print collectRateDict['10944750']
    print collectPreciseboundList
    print collectRecallboundList
    print userCollectPreciseRate
    print userCollectRecallRate
    # for plot
    plt.figure('Collect rate')
    plt.plot(collectPreciseboundList, accumulateCollectPreciseRate,label='accuCollPreciseRate')
    plt.plot(collectRecallboundList, accumulateCollectRecallRate, label='accuCollRecallRate')
    plt.scatter(collectPreciseboundList, accumulateCollectPreciseRate)
    plt.scatter(collectRecallboundList, accumulateCollectRecallRate)
    plt.xlabel('collectPreciseRate/collectRecallRate')
    plt.ylabel('accumulatecollectPreciseRate/accumulatecollectRecallRate')
    plt.title('the relationship between collect and Purchase')
    plt.legend()

    plt.figure('collect rank')
    plt.plot(collectRankboundList, accumulateCollectRank, label='accuCollRank')
    plt.scatter(collectRankboundList, accumulateCollectRank)
    plt.xlabel('Rank of collectBrand')
    plt.ylabel('accumulateRate of collectBrand rank')
    plt.legend()
    print 'collect collectNoPurchaseRate: '
    print collectNoPurchaseRate
    '''
    plt.show()
    