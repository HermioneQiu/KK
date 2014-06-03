import re

from DataProcess.DataTransform import DataTimeTransfrom
from FeatureAnalysis.TimeFeature import splitByTime, TimeAnalysis
from Utils.File import *

import matplotlib.pyplot as plt
import numpy as np


if __name__=="__main__":
    
    root_dir = 'E:\\workspace\\DATA\\Reco'
    rawDataDir = root_dir + '\\all.data'
    rawDataFile = File(rawDataDir)
    # the symbol that split elements in a line
    symbol = ','
    head = True
    List = rawDataFile.readLine2List(symbol, head)
    timeTransferedList,timeList = DataTimeTransfrom(List)
    timeSlot = 0.3
    splitList, splitUser, splitBrand = splitByTime(timeTransferedList, timeList, timeSlot)
    # for brand
    print 'user:'
    userDupliRate, userNovelRate = TimeAnalysis(splitUser)
    print userDupliRate
    print userNovelRate
    # plot
    timeSeries = [i for i in range(len(userDupliRate))]
    plt.figure('user time feature')
    plt.plot(timeSeries, userDupliRate,label='userDupliRate')
    plt.scatter(timeSeries, userDupliRate)
    plt.plot(timeSeries, userNovelRate, label ='userNovelRate')
    plt.scatter(timeSeries, userNovelRate)
    plt.xlabel('timeSeries')
    plt.ylabel('userDupliRate/userNovelRate')
    plt.legend()
    # for user
    print 'brand:'
    brandDupliRate, brandNovelRate = TimeAnalysis(splitBrand)
    print brandDupliRate
    print brandNovelRate
    # plot
    timeSeries = [i for i in range(len(brandDupliRate))]
    plt.figure('brand time feature')
    plt.plot(timeSeries, brandDupliRate, label='brandDupliRate')
    plt.scatter(timeSeries, brandDupliRate)
    plt.plot(timeSeries, brandNovelRate,label='brandNovelRate')
    plt.scatter(timeSeries, brandNovelRate)
    plt.xlabel('timeSeries')
    plt.ylabel('brandDupliRate/brandNovelRate')
    plt.legend()
    plt.show()