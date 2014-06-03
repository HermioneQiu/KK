from Dijsktra.File import *
from utils import *
import random
from Newton_Raphson import *
def KK(L, N, K, threshold, max_iret_num):   
    # input all path_distance
    PathMatrix=initPathMatrix()
    # init PositionMatrix
    PositionMatrix=initPosition(PathMatrix, L)
    # for test
    root_dir = r"E:\workspace\DATA\web"
    initPositionMatrix_file_dir = root_dir +'\initPositionMatrix.data'
    initPositionMatrix_file= File(initPositionMatrix_file_dir)
    initPositionMatrix_file.writeMatrix(PositionMatrix)
    # init L(i,j)
    LMatrix=initL(PathMatrix, L, N)
    # for test
    
    LMatrix_file_dir = root_dir +'\LMatrix.data'
    LMatrix_file = File(LMatrix_file_dir)
    LMatrix_file.writeMatrix(LMatrix)
    # init K(u,v)
    KMatrix=initK(PathMatrix, K, N)
    # for test
    KMatrix_file_dir = root_dir + '\KMatrix.data'
    KMatrix_file = File(KMatrix_file_dir)
    KMatrix_file.writeMatrix(KMatrix)
    # newton_raphson algorithm
    PositionMatrix =Newton_Raphson(PathMatrix, LMatrix, KMatrix, N, PositionMatrix, threshold,max_iret_num)
    # return PositionMatrix
    return PositionMatrix
def initPathMatrix():
    root_dir = r"E:\workspace\DATA\web"
    PathMatrix_file_dir = root_dir + '\PathMatrix.data'
    PathMatrix_file =File(PathMatrix_file_dir)
    PathMatrix = PathMatrix_file.readMatrix()
    PathMatrix = MatrixStr2Int(PathMatrix)
    return PathMatrix
def initL(PathMatrix, L0, N):
    node_num = len(PathMatrix)
    LS = float(L0)/math.sqrt(node_num)
    LS = removeTail(LS, N)
    init_PathLen = max_PathLen(PathMatrix)+2
    LMatrix = [[init_PathLen for i in range(node_num)] for j in range(node_num)]
    for i in range(node_num):
        for j in range(i):
            if PathMatrix[i][j]!=0:
                LMatrix[i][j]=removeTail(float(LS)*PathMatrix[i][j],N)
                LMatrix[j][i]=LMatrix[i][j]
    for i in range(node_num):
        LMatrix[i][i] = 0
    return LMatrix
def initK(PathMatrix, K, N):
    node_num = len(PathMatrix)
    init_K = float(K)/(max_PathLen(PathMatrix)+2)
    init_K = removeTail(init_K, N)
    KMatrix = [[init_K for i in range(node_num)] for j in range(node_num)]
    for i in range(node_num):
        for j in range(i):
            if PathMatrix[i][j]!=0:
               KMatrix[i][j]=removeTail(float(K)/pow(PathMatrix[i][j],2), N) 
               KMatrix[j][i]=KMatrix[i][j]
    for i in range(node_num):
        KMatrix[i][i] = 0
    return KMatrix
def initPosition(PathMatrix, L):
    node_num = len(PathMatrix)
    PositionMatrix = [[random.uniform(0,L),random.uniform(0,L)] for i in range(node_num)]
    return PositionMatrix
def SavePositionMatrix(PositionMatrix):    
    root_dir = r"E:\workspace\DATA\web"
    '''
    NodeDict_file_dir = root_dir+'\NodeDict.data'
    NodeDict_file = File(NodeDict_file_dir)
    NodeDict = NodeDict_file.readDict()
    new_PositionMatrix = []
    for node_i in range(len(PositionMatrix)):
        node = NodeDict[node_i]
        x,y =PositionMatrix[node_i]
        new_PositionMatrix.append([node,x,y])
    '''
    new_PositionMatrix = []
    for node_i in range(len(PositionMatrix)):
        x,y = PositionMatrix[node_i]
        new_PositionMatrix.append([node_i, x, y])
    Position_file_dir = root_dir+'\PositionList.data'
    Position_file = File(Position_file_dir)
    Position_file.writeListList(new_PositionMatrix)
    
    