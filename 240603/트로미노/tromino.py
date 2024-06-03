n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = 0 

def L(i, j):
    cur = 0 

    if 0 <= i - 1 and j + 1 < m:
        cur = max(cur, matrix[i][j] + matrix[i-1][j] + matrix[i][j+1])

    if 0 <= i - 1 and 0 <= j - 1:
        cur = max(cur, matrix[i][j] + matrix[i-1][j] + matrix[i][j-1])

    if i + 1 < n and j + 1 < m:
        cur = max(cur, matrix[i][j] + matrix[i+1][j] + matrix[i][j+1])

    if i + 1 < n and 0 <= j - 1:
        cur = max(cur, matrix[i][j] + matrix[i+1][j] + matrix[i][j-1])

    return cur


def I(i, j):
    cur = 0 

    if j + 2 < m:
        cur = max(cur, matrix[i][j] + matrix[i][j+1] + matrix[i][j+2])
    
    if j - 2 >= 0:
        cur = max(cur, matrix[i][j] + matrix[i][j-1] + matrix[i][j-2])
    
    if i + 2 < n:
        cur = max(cur, matrix[i][j] + matrix[i+1][j] + matrix[i+2][j])
    
    if i - 2 >= 0:
        cur = max(cur, matrix[i][j] + matrix[i-1][j] + matrix[i-2][j])    

    return cur


for i in range(n):
    for j in range(m):
        tmpL = L(i, j)
        tmpI = I(i, j)

        ans = max(ans, tmpL, tmpI)

print(ans)