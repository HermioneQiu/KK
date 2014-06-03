
from BuildInfluenceMatrix.File import *
from BuildInfluenceMatrix.Utils import *

def readAFollow(followFileDir):
    followFile = File(followFileDir)
    followList = followFile.readList()
    return followList

def readAForward(forwardFileDir):
    forwardFile = File(forwardFileDir)
    forwardList = forwardFile.readList()
    return forwardList
def getACommunity(communityFileDir):
    communityDict = dict()
    communityFile = File(communityFileDir)
    communityList = communityFile.readList()
    index = 0
    for node in communityList:
        node =node[0]
        communityDict[node]=index
        index+=1
    return communityList, communityDict
def getACommunityFollowForward(followList,forwardList,communityDict, followK, forwardK):
    communityList_num = len(communityDict)
    followMatrix = [[0 for i in range(communityList_num)] for j in range(communityList_num)]
    forwardMatrix = [[0 for i in range(communityList_num)] for j in range(communityList_num)]
    followRelationshipDict = parseFollowDict(followList, communityDict);
    forwardRelationshipDict = parseForwardDict(forwardList, communityDict)
    for src_i in followRelationshipDict.keys():
        dst_i_s = followRelationshipDict[src_i]
        for dst_i in dst_i_s:
            followMatrix[src_i][dst_i] = followK
    for src_i in forwardRelationshipDict.keys():
        dst_i_s = forwardRelationshipDict[src_i]
        for dst in dst_i_s:
            dst_i = dst[0]
            dst_val = dst[1]
            forwardMatrix[src_i][dst_i] = forwardK*dst_val
    return followMatrix, forwardMatrix