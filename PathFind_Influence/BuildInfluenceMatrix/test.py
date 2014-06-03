from BuildInfluenceMatrix.File import *
from BuildInfluenceMatrix.getRelationshipMatrix import *
from BuildInfluenceMatrix.getInfluenceMatrix import *

if __name__ == "__main__":
    rootDir = r"E:\Data\Graph\Friend_Forward"
    followFileDir = rootDir + "\Follow0.txt"
    followList = readAFollow(followFileDir)
    forwardFileDir = rootDir + "\Forward0.txt"
    forwardList = readAForward(forwardFileDir)
    communityFileDir = rootDir + "\Community0.txt"
    communityList,communityDict = getACommunity(communityFileDir)
    # set weight of differen factor, can be defined
    followK = 1
    forwardK = 1
    
    followMatrix, forwardMatrix = getACommunityFollowForward(followList,forwardList,communityDict,followK, forwardK)
    print "finished Matrix building"
    followMatrixDir = rootDir + "\\followMatrix.txt"
    followMatrixFile = File(followMatrixDir)
    followMatrixFile.writeMatrix(followMatrix)
    forwardMatrixDir = rootDir + "\\forwardMatrix.txt"
    forwardMatrixFile = File(forwardMatrixDir)
    forwardMatrixFile.writeMatrix(forwardMatrix)    
    digitN = 6
    influenceMatrix = getInfluenceMatrix(followMatrix, forwardMatrix, digitN, followK, forwardK)
    influenceMatrixFileDir = rootDir + "\\influenceMatrix.txt"
    influenceMatrixFile = File(influenceMatrixFileDir)
    influenceMatrixFile.writeMatrix(influenceMatrix)
    