class File:
    def __init__(self, file_dir):
        self.file_dir= file_dir
    def read(self):
        fp=open(self.file_dir, 'r')
        lines = fp.readlines()
        return lines
    def readGraph(self):
        GraphList = []
        lines = self.read()
        for line in lines:
            node_s, node_e = line.strip().split('\t')
            GraphList.append([node_s, node_e])
        return GraphList
    def readMatrix(self):
        Matrix = []
        lines = self.read()
        for line in lines:
            ll = line.strip().split('\t')
            Matrix.append(ll)
        return Matrix
    def readDict(self):
        Dict = dict()
        lines = self.read()
        for line in lines:
            ll = line.strip().split(':')
            key = ll[1]
            value = ll[0]
            Dict[int(key)]=int(value)
        return Dict
    def flush(self):
        fp = open(self.file_dir, 'w')
        fp.close()
    def writeDict(self, Dict):
        self.flush()
        fp = open(self.file_dir, 'a')
        for key in Dict.keys():
            value = Dict[key]
            line = str(key) + ':' +str(value)+'\n'
            fp.write(line)
        fp.close()
    def writeListList(self, List):
        self.flush()
        fp= open(self.file_dir, 'a')
        List = [[str(l) for l in ll] for ll in List]
        for ll in List:
            line = '\t'.join(ll)
            line = line +'\n'
            fp.write(line)
        fp.close()
    def writeMatrix(self, Matrix):
        self.flush()
        fp = open(self.file_dir, 'a')
        Matrix = [[str(m) for m in mm] for mm in Matrix]
        for ll in Matrix:
            line = '\t'.join(ll)
            line = line + '\n'
            fp.write(line)
        fp.close()
    def writetmpList(self,List):
        fp = open(self.file_dir,'a')
        List = [[str(l) for l in ll] for ll in List] 
        LineList = []
        for ll in List:
            line = ','.join(ll)
            LineList.append(line)
        line = '\t'.join(LineList)+'\n'
        fp.write(line)
        fp.close()
        