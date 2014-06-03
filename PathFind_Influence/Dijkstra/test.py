from BuildInfluenceMatrix.File import *
from BuildInfluenceMatrix.Utils import *
from Dijkstra import *
from BuildInfluenceMatrix.File import File


if __name__ == "__main__":
    rootDir = "E:\Data\Graph\Friend_Forward"
    influenceMatrixDir = rootDir + "\influenceMatrix.txt"
    influenceMatrixFile = File(influenceMatrixDir)
    influenceMatrix = influenceMatrixFile.readMatrix()
    influenceMatrix = MatrixChar2Float(influenceMatrix)
    print influenceMatrix[2]
    
    print "finished influenceMatrix"
    #get a path
    node_src = 2
    node_dst = 3
    # permanently unused..
    DiscountR =1
    stopStep = 5
    neighborNum = 3
    pathListDir = rootDir + '\paths.list'
    pathList =findAllPath(influenceMatrix,DiscountR, stopStep, neighborNum, pathListDir)
    
    #get all paths
    