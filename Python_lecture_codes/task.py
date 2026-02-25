matrix  = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
top = 0 
bottom = len(matrix) -1
left = 0
right = len(matrix[0])-1
result  = []
while top<=bottom and left<=right:
    for i in range(left,right+1):
        result.append(matrix[top][i])
    top = top + 1
    for i in range(top,bottom+1):
        result.append(matrix[i][right])
    right = right - 1
   
    for i in range(right,left-1,-1):
        result.append(matrix[bottom][i])
    bottom = bottom -1
    for i in range(bottom,top - 1,-1):
        result.append(matrix[i][left])
    left = left +1
print(result)

