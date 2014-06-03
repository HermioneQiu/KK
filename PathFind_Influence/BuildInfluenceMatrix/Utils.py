
def parseFollowDict(List, Dict):
    FollowDict = dict()
    tmp = []
    if len(List[0])==3:
        for line in List:
            srcNode = line[0]
            dstNode = line[1]
            val = line[2]
            if val == '1':
                if Dict[srcNode] in FollowDict.keys():
                    FollowDict[Dict[srcNode]].append(Dict[dstNode])
                else:
                    FollowDict[Dict[srcNode]] = [Dict[dstNode]]
            else:
                if Dict[srcNode] in FollowDict.keys():
                    FollowDict[Dict[srcNode]].append(Dict[dstNode])
                else:
                    FollowDict[Dict[srcNode]] = [Dict[dstNode]]
                if Dict[dstNode] in FollowDict.keys():
                    FollowDict[Dict[dstNode]].append(Dict[srcNode])
                else:
                    FollowDict[Dict[dstNode]] = [Dict[srcNode]]
    return FollowDict
def parseForwardDict(List, Dict):
    forwardDict = dict()
    tmp = []
    if len(List[0])==3:
        for line in List:
            srcNode = line[0]
            dstNode = line[1]
            val = line[2]
            if Dict[srcNode] in forwardDict.keys():
                forwardDict[Dict[srcNode]].append([Dict[dstNode], int(val)])
            else:
                forwardDict[Dict[srcNode]] = [[Dict[dstNode], int(val)]]
    return forwardDict
def tailDigit(Digit, N):
    tailDigit = int(Digit*pow(10,N))/float(pow(10,N))
    return tailDigit

def MatrixChar2Float(Matrix):
    Matrix_len = len(Matrix)
    floatMatrix = [[float(l) for l in line] for line in Matrix]
    return floatMatrix
'''
def parseMatrix2RevList(Matrix):
    for 
'''
def sortWithIndex(List):
    List_len = len(List)
    Dict = dict()
    for i in range(List_len):
        Dict[i] = List[i]
    sortedList = sorted(List)
    indexList = []
    for val in sortedList:
        for key in Dict.keys():
            if val == Dict[key]:
                if key not in indexList:
                    indexList.append(key)             
    return indexList, sortedList       
    