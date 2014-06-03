import copy

from BuildInfluenceMatrix.File import File
from BuildInfluenceMatrix.Utils import *


def findAllPath(influenceMatrix,DiscountR, stopStep, neighborNum, pathListDir):
    nodeNum = len(influenceMatrix)
    pathList = []
    for node_src in range(nodeNum):
        for node_dst in range(nodeNum):
            if node_dst != node_src:
                lastPath, lastpath, srcNeighbors, dstNeighbors = findAPath(node_src, node_dst, influenceMatrix, DiscountR, stopStep, neighborNum)
                pathList.append([[node_src, node_dst],lastpath, srcNeighbors, dstNeighbors])
                print 'one'
                print lastpath
    if pathListDir!=False:
        pathListFile =  File(pathListDir)
        pathListFile.writePathList(pathList)
    return pathList

def findAPath(node_src, node_dst, influenceMatrix, DiscountR, stopStep, neighborNum):
    # find neighbors
    srcNeighbors = findNeighbors(node_src, neighborNum, influenceMatrix)
    dstNeighbors = findNeighbors(node_dst, neighborNum, influenceMatrix)
    
    # find path
    Path = [[[node_src],0]]
    lastPath = []
    #indeluenceList = influenceMatrix[node_src]
    #sortIndexList,sortedList = sortWithIndex(indeluenceList)
    # for every path in the path list
    maxStep = stopStep -2
    while(maxStep<stopStep):
        newPath = []
        for path_i in range(len(Path)):
            path = Path[path_i]
            #new_tmpPath = copy.deepcopy(tmpPath)
            tmpNode_src = path[0][-1]
            node_exist = path[0][0:-1]
            tmpList = influenceMatrix[tmpNode_src]
            for val_i in range(len(tmpList)):
                # need to be modified******
                val = tmpList[val_i]
                if ((val!=0) & (val_i!=node_dst)) & (val_i not in node_exist):
                    tmppath = copy.deepcopy(path[0])
                    tmppath.append(val_i)
                    tmpval = path[1]
                    newval = tmpval+val
                    newlist = [tmppath, newval]
                    newPath.append(newlist)
                if ((val!=0) & (val_i==node_dst)) & (val_i not in node_exist):
                    tmppath = copy.deepcopy(path[0])
                    tmppath.append(val_i)
                    tmpval = path[1]
                    newval = tmpval+val
                    newlist = [tmppath, newval]
                    lastPath.append(newlist)
                         
        Path = copy.deepcopy(newPath)
        if len(Path)<1:
            break
        pathLen = []
        for path in Path:
            path_len = len(path[0])
            pathLen.append(path_len)
        maxStep = max(pathLen)
    if len(lastPath)>0:
        rates = []
        for path in lastPath:
            rates.append(path[-1])
        maxRate = max(rates)
        lastpath = []
        for path in lastPath:
            if path[-1] == maxRate:
                lastpath.append(path)
    else:
        lastpath =[]
    return lastPath, lastpath, srcNeighbors,dstNeighbors

def findNeighbors(node_id, neighborNum, influenceMatrix):
    List = influenceMatrix[node_id]
    newList =[]
    for l in List:
        if l==0.0:
            newList.append(float('inf'))
        else:
            newList.append(l)
    print newList
    indexList, sortedList = sortWithIndex(newList)
    neighbors = indexList[0:neighborNum ]
    return neighbors