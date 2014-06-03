from KK import *
from utils import *
if __name__ == "__main__":
    '''
    root_dir = r"E:\workspace\DATA\web"
    PathMatrix_file_dir = root_dir + '\PathMatrix.data'
    PathMatrix_file =File(PathMatrix_file_dir)
    PathMatrix = PathMatrix_file.readMatrix()
    PathMatrix = MatrixStr2Int(PathMatrix)
    L0 = 100
    N =3
    LMatrix = initL(PathMatrix, L0,N)
    print LMatrix
    K = 5
    KMatrix = initK(PathMatrix, K, N)
    print KMatrix
    PositionMatrix = initPosition(PathMatrix, L0)
    print PositionMatrix
    '''
    # the range of position
    L = 100
    # the digital precision
    N= 4
    # a parameter of Hooke
    K= 5.0
    # the threshold of stopping iretation
    threshold = 0.2
    # iretate_num
    max_iret_num = 200
    PositionMatrix=KK(L, N, K, threshold, max_iret_num)   
    SavePositionMatrix(PositionMatrix)
    print "finish"
    #******************************************************
    # need to be changed, once input the origin file_path, the result get out automatically