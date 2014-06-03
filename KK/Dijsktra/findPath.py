from File import *
import copy
# +++++++++no direction+++no weight++++++++
def initGraphMatrix(GraphList):
    # get all nodes
    nodes = []
    for line in GraphList:
        node_s,node_e = line
        if node_s not in nodes:
            nodes.append(node_s)
        if node_e not in nodes:
            nodes.append(node_e)
    # get node_dict
    node_num = len(nodes)
    node_dict = dict()
    node_i = 0
    for node in nodes:
        node_dict[node]= node_i
        node_i += 1
    # save dict
    Dict_file_dir = r"E:\workspace\DATA\web\NodeDict.data"
    DictFile = File(Dict_file_dir)
    DictFile.writeDict(node_dict)
    # -----need output this -------
    GraphMatrix = [[0 for node_i in range(node_num)] for node_i in range(node_num)]
    for line in GraphList:
        node_s, node_e = line
        GraphMatrix[node_dict[node_s]][node_dict[node_e]] = 1
        #**** no direction
        GraphMatrix[node_dict[node_e]][node_dict[node_s]] = 1
    return GraphMatrix
def floyd(GraphMatrix, max_step):
    node_num = len(GraphMatrix)
    paths = []
    PathMatrix= [[0 for i in range(node_num)] for j in range(node_num)]
    for node_s_i in range(node_num):
        for node_e_i in range(node_s_i):
                 
            PathMatrix, path = singlepath(PathMatrix, GraphMatrix, node_s_i,node_e_i, max_step)
            if len(path)>0:
                paths.append(path)
    return PathMatrix, paths
def singlepath(PathMatrix, GraphMatrix, node_s_i, node_e_i, max_step):
    node_num = len(GraphMatrix)
    PATH = []
    if GraphMatrix[node_s_i][node_e_i] != 0:  
        PATH = [node_s_i, node_e_i]
        PathMatrix[node_s_i][node_e_i]=1
        PathMatrix[node_e_i][node_s_i]=1
    if GraphMatrix[node_s_i][node_e_i] == 0:
            # if step_num is more than this, take it as INF
            paths = [] 
            paths.append([node_s_i])      
            path_flag = 0
            for iret_i in range(max_step): 
                if len(paths)!=0: 
                    tmp_paths = []                                                                       
                    # if has a path forward                   
                    for path in paths:
                        
                        tmp_node_s_i = path[-1]
                        for node_k_i in range(node_num):
                            if (node_k_i != node_s_i):     
                                #if has a path between the 
                                if (GraphMatrix[node_k_i][node_e_i]!=0)&(GraphMatrix[tmp_node_s_i][node_k_i]!=0):
                                   
                                    new_path = path
                                    new_path.append(node_k_i) 
                                    new_path.append(node_e_i) 
                                    PATH = new_path                                 
                                    PathMatrix[node_s_i][node_e_i] = len(new_path)-1
                                    PathMatrix[node_e_i][node_s_i] = len(new_path)-1
                                    path_flag = 1
                                    break
                                if (GraphMatrix[node_k_i][node_e_i]==0)&(GraphMatrix[tmp_node_s_i][node_k_i]!=0):   
                                                            
                                    new_path = copy.deepcopy(path)
                                    new_path.append(node_k_i)
                                    tmp_paths.append(new_path)
                        if path_flag == 1:
                            break                         
                paths = tmp_paths 
                
                if path_flag ==1 :
                        break     
    if PATH[-1] != node_e_i:
        PATH = []
    return PathMatrix,PATH
#-----path and according node_s, node_e should be stored.



