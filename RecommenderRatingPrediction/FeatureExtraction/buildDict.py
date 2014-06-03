# transfered List
# [[userId, brandId, mark], dateStr]
def buildUserBrandDict(List):
    userDict = dict()
    brandDict = dict()
    user_i = 0
    brand_i = 0
    for line in List:
        userId, brandId, mark = line[0]
        if userId not in userDict.keys():
            userDict[userId]=user_i
            user_i += 1
        if brandId not in brandDict.keys():
            brandDict[brandId]= brand_i
            brand_i += 1
    return userDict, brandDict

    