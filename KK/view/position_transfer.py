from Dijsktra.File import *
from KK.utils import *

def positiontransfer(in_file_dir, out_file_dir):
    in_file = open(in_file_dir, 'r')
    lines = in_file.readlines()
    out_file = open(out_file_dir,'w')
    out_file.close()
    out_file = open(out_file_dir, 'a')
    refinex = removeTail(650/100.0,3)
    refiney = removeTail(300/100.0,3)
    for line in lines:
        ID, x, y = line.strip().split('\t')
        x = (float(x))*refinex+350
        y = (float(y))*refiney+150
        new_line = "cy.$('#"+str(ID)+"').position({x:"+str(x)+", y:"+str(y)+"});\n"
        out_file.write(new_line)
    in_file.close()
    out_file.close()
    
def getNodeEdge():
    # for node
    root_dir = r"E:\workspace\DATA\web"
    NodeDict_file_dir = root_dir + '\NodeDict.data'
    NodeDict_file = File(NodeDict_file_dir)
    NodeDict = NodeDict_file.readDict()
    Edge = []
    Edge_file_dir = root_dir + '\graph.data'
    Edge_file = File(Edge_file_dir)
    Edge = Edge_file.readGraph()
    return NodeDict, Edge
    
def node_edgetransfer(NodeDict, Edge, out_node_dir, out_edge_dir):
    out_node_file = open(out_node_dir, 'w')
    out_node_file.close()
    out_node_file = open(out_node_dir, 'a')
    for node_i in NodeDict.keys():
        id = str(node_i)
        node = str(NodeDict[node_i])
        line = "{ data: { id: '"+id+"', name:'"+node+"' }},\n"
        out_node_file.write(line)
    inv_NodeDict = dict()
    for node_i in NodeDict.keys():
        node = str(NodeDict[node_i])
        inv_NodeDict[node]=node_i
    out_node_file.close()
    out_edge_file = open(out_edge_dir, 'w')
    out_edge_file.close()
    out_edge_file = open(out_edge_dir, 'a')   
    for edge in Edge:
         s_id = edge[0]
         node_s_i = str(inv_NodeDict[s_id])
         e_id = edge[1]
         node_e_i = str(inv_NodeDict[e_id])
         line = "{ data: { source: '"+node_s_i+"', target: '"+node_e_i+"' }},\n"
         out_edge_file.write(line)
    out_edge_file.close()
    
if __name__ == "__main__":
    root_dir = r"E:\workspace\DATA\web"
    in_file_dir = root_dir + '\PositionList.data'
    out_file_dir = root_dir + '\PositionList_JS.data'
    NodeDict, Edge=getNodeEdge()
    node_num = len(NodeDict)
    positiontransfer(in_file_dir, out_file_dir)
    print "finished 1"
  
    out_node_dir = root_dir + '\Node_JS.data'
    out_edge_dir = root_dir +'\Edge_JS.data'
    node_edgetransfer(NodeDict, Edge, out_node_dir, out_edge_dir)
    print "finished 2"