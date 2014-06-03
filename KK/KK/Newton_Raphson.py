import math
from utils import *
from Dijsktra.File import *
def DiffX_Y(i,PositionMatrix, KMatrix, LMatrix, N):
    diffx = 0
    diffy = 0
    node_num = len(LMatrix)
    for j in range(node_num):
        if j != i:
            deltax = PositionMatrix[i][0]-PositionMatrix[j][0]
            deltay = PositionMatrix[i][1]-PositionMatrix[j][1]
            deltaxy = math.sqrt(pow(deltax,2)+pow(deltay,2))
            if deltaxy != 0:
                tmp = 1-LMatrix[i][j]/deltaxy
                diffx += removeTail(KMatrix[i][j]*deltax*tmp,N)
                diffy += removeTail(KMatrix[i][j]*deltay*tmp,N)

    return diffx, diffy
def DiffXX_YY(i, PositionMatrix, KMatrix, LMatrix, N):
    diffxx=0
    diffyy=0
    diffxy=0
    diffyx=0
    node_num=len(LMatrix)
    for j in range(node_num):
        if j != i:
            deltax = PositionMatrix[i][0]-PositionMatrix[j][0]
            deltay = PositionMatrix[i][1]-PositionMatrix[j][1]
            deltaxy = pow(pow(deltax,2)+pow(deltay,2), float(3)/2)     
            if deltaxy !=0:                    
                tmpxx = 1-LMatrix[i][j]*pow(deltay,2)/deltaxy
                diffxx += removeTail(KMatrix[i][j]*tmpxx,N)
                tmpyy = 1-LMatrix[i][j]*pow(deltax,2)/deltaxy
                diffyy += removeTail(KMatrix[i][j]*tmpyy,N)
                tmpxy = LMatrix[i][j]*deltax*deltay/deltaxy
                diffxy += removeTail(KMatrix[i][j]*tmpxy,N)
            
    diffyx = diffxy
    return diffxx, diffyy, diffxy, diffyx
def DeltaXY(i, diffx, diffy, diffxx, diffyy, diffxy, diffyx, N):
    tmp = diffxx*diffyy-diffxy*diffyx
    if (diffxx*diffyy-diffxy*diffyx)==0:
        deltax = 0
        deltay = 0
    else:
        deltax = removeTail((diffy*diffxy-diffx*diffyy)/tmp, N)
        deltay = removeTail((diffx*diffyx-diffy*diffxx)/tmp, N)
    return deltax, deltay
def Newton_Raphson(PathMatrix, LMatrix, KMatrix, N, PositionMatrix, threshold,max_iret_num):
    # get the matrix of deltax,deltay
    node_num = len(LMatrix)
    # for test
    root_dir = r"E:\workspace\DATA\web"
    delta_file_dir = root_dir + '\delta.tmp'
    delta_file = File(delta_file_dir)
    for iret_i in range(max_iret_num):
        DeltaList = []
        for i in range(node_num):
            diffx,diffy=DiffX_Y(i,PositionMatrix, KMatrix, LMatrix, N)
            diffxx, diffyy, diffxy, diffyx=DiffXX_YY(i, PositionMatrix, KMatrix, LMatrix, N)
            deltax, deltay=DeltaXY(i, diffx, diffy, diffxx, diffyy, diffxy, diffyx, N)
            DeltaList.append([deltax,deltay])
        delta_file.writetmpList(DeltaList)
        totalenergy = TotalEnergy(KMatrix, LMatrix, PositionMatrix)
        print totalenergy
        # find the delta_value
        max_delta,max_index = findMaxDelta(DeltaList)
        print 'max', max_index
        if max_delta<threshold:
            break
        print iret_i,max_delta
        # update the node which is has the highest delta_value
        PositionMatrix[max_index][0]+=DeltaList[max_index][0]
        PositionMatrix[max_index][1]+=DeltaList[max_index][1]       
    return PositionMatrix
def findMaxDelta(DeltaList):
    tmp_DeltaList = []
    for ll in DeltaList:
        delta = math.sqrt(pow(ll[0],2)+pow(ll[1],2))
        tmp_DeltaList.append(delta)
    max_delta = max(tmp_DeltaList)
    max_index = tmp_DeltaList.index(max_delta)
    return max_delta,max_index
def TotalEnergy(KMatrix, LMatrix, PositionMatrix):
    totalenergy = 0
    node_num = len(KMatrix)
    for i in range(node_num):
        for j in range(i):
            deltax = abs(PositionMatrix[i][0]-PositionMatrix[j][0])
            deltay = abs(PositionMatrix[i][1]-PositionMatrix[j][1])
            distance = math.sqrt(pow(deltax,2)+pow(deltay,2))
            totalenergy += KMatrix[i][j]*pow((distance-LMatrix[i][j]),2)/2.0
    return totalenergy
            
        
    