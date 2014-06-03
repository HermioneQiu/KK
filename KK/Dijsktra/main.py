from InOut import *
from findPath import *
def main():
    root_dir = r"E:\workspace\DATA\web"
    GraphFile_dir = root_dir  + "\graph.data"
    GraphList = readGraphData(GraphFile_dir)
    GraphMatrix = initGraphMatrix(GraphList)
    #print GraphMatrix
    #GraphMatrix, paths = floyd(GraphMatrix)
    
    PathMatrix, Paths = floyd(GraphMatrix, max_step = 4)
    #print PathMatrix
    #print Paths
    PathMatrix_file_dir = root_dir + "\PathMatrix.data"
    PathMatrix_file = File(PathMatrix_file_dir)
    PathMatrix_file.writeMatrix(PathMatrix)
    Paths_file_dir = root_dir + "\Paths.data"
    Paths_file = File(Paths_file_dir)
    Paths_file.writeListList(Paths)
    print 'finished'
    '''
    node_s_i = 41
    node_e_i = 19
    node_num = len(GraphMatrix)
    PathMatrix= [[0 for i in range(node_num)] for j in range(node_num)]
    PathMatrix, path = singlepath(PathMatrix, GraphMatrix, node_s_i, node_e_i, max_step =5)
    print 'final'
    print path
    '''
if __name__ == "__main__":
    main()