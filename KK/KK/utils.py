def MatrixStr2Int(Matrix):
    new_Matrix = [[int(m) for m in mm] for mm in Matrix]
    return new_Matrix
def removeTail(decimal, N):
    tmp = pow(10, N)
    new_decimal = round(decimal*tmp)/tmp
    return new_decimal
def max_PathLen(PathMatrix):
    max_PathLen = 1
    for mm in PathMatrix:
        for m in mm:
            if m>max_PathLen:
                max_PathLen = m
    return max_PathLen     
