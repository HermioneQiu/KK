import re

from Utils.File import *


# the List[0][4]is datetime, 
# timeTransferedList[0][0]is [], while timeTransferedList[0][1]is datetime
def DataTimeTransfrom(List):
    timeTransferedList = []
    timeList =  []
    for line in List:
        dateStr = line[-1]
        m = re.findall(r"(\d+)", dateStr)
        monthInt, dayInt = int(m[0]), int(m[1])
        transferedDate = monthInt+dayInt*0.1
        newLine = [line[0:3], transferedDate]
        timeTransferedList.append(newLine)
        timeList.append(transferedDate)
    return timeTransferedList,timeList

