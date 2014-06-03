
class File:
    def __init__(self, file_dir):
        self.file_dir= file_dir
    def readLine(self):
        fp = open(self.file_dir, 'r')
        line = fp.readline()
        return line 
    def read(self):
        fp=open(self.file_dir, 'r')
        lines = fp.readlines()
        return lines
    # List elements are string format
    def readLine2List(self, symbol, head):
        List = []
        if head == False:
            lines = self.read()
            for line in lines:
                parts = line.strip().split(symbol)
                if len(parts)==4:
                    userId, brandId, bhvType, dateStr = parts
                    List.append([userId, brandId, bhvType, dateStr])
                else:
                    List.append(parts)
        elif head == True:
            lines = self.read()
            for line in lines:
                parts = line.strip().split(symbol)
                if len(parts)==4:
                    userId, brandId, bhvType, dateStr = parts
                    if userId == 'user_id':
                        continue;
                    List.append([userId, brandId, bhvType, dateStr])
                else:
                    List.append(parts)
        return List
    def flush(self):
        fp = open(self.file_dir, 'w')
        fp.close()
    def writeMatrix(self, Matrix):
        self.flush()
        fp=open(self.file_dir, 'a')
        for line in Matrix:
            newLine =[str(i) for i in line]
            lineStr = ','.join(newLine)+'\n'
            fp.write(lineStr)
        fp.close()
    def writeDict(self, Dict):
        self.flush()
        fp = open(self.file_dir, 'a')
        for key in Dict.keys():
            lineStr = str(key)+','+str(Dict[key])+'\n'
            fp.write(lineStr)
        fp.close()
    def writeDictDict(self, DictDict):
        self.flush()
        fp = open(self.file_dir, 'a')
        for key1 in DictDict.keys():
            tmpLineStr =''
            for key2 in DictDict[key1].keys():
                tmpLineStr += str(key2)+':'+str(DictDict[key1][key2])+','
            lineStr = str(key1)+':{'+tmpLineStr+'}\n'
            fp.write(lineStr)
        fp.close()
    def writeRateList(self, List):
        self.flush()
        fp = open(self.file_dir, 'a')
        for l in List:
            
            tmpline = ''
            for ll in l:
                tmpline = str(l)+'\t'
            line = tmpline + '\n'
            fp.write(line)
        fp.close()
