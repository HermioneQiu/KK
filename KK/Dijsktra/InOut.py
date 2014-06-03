from File import *
# read in graph.data, no weight
def readGraphData(file_dir):
    GraphFile = File(file_dir)
    GraphList = GraphFile.readGraph()
    return GraphList
