n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

def compute(i, j, matrix):
    cnt = 0 
    for a in range(i , i + 3):
        for b in range(j , j + 3):
            if matrix[a][b] == 1:
                cnt += 1
    return cnt

ans = 0 

for i in range(n):
    for j in range(n):
        if i + 2 >= n or j + 2 >= n:
            continue 
        ans = max(ans, compute(i, j, matrix))

print(ans)