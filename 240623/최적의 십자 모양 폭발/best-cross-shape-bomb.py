n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

next_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def is_valid(r,c):
    return 0 <= r < n and 0 <= c < n 

def pang(r, c):
    num = grid[r][c]

    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]

    # 폭발 
    for i in range(num):
        if is_valid(r+i, c):
            next_grid[r+i][c] = 0 
    
    for i in range(num):
        if is_valid(r-i, c):
            next_grid[r-i][c] = 0 
    
    for i in range(num):
        if is_valid(r, c+i):
            next_grid[r][c+i] = 0 
    
    for i in range(num):
        if is_valid(r, c-i):
            next_grid[r][c-i] = 0

    # 떨굼  
    for i in range(n):
        for j in range(n-1, -1, -1):
            if next_grid[j][i] != 0:
                for k in range(n-1, j, -1):
                    if next_grid[k][i] == 0:
                        next_grid[k][i] = next_grid[j][i]
                        next_grid[j][i] = 0
                        break

def count_sang():
    cnted = set()

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for i in range(n):
        for j in range(n):
            for k in range(4):
                if is_valid(i + dr[k], j + dc[k]):
                    if next_grid[i][j] != 0 and next_grid[i][j] == next_grid[i + dr[k]][j + dc[k]]:
                        cnted.add((i, j, i + dr[k], j + dc[k]))

    return len(cnted)

ans = 0
for i in range(n):
    for j in range(n):
        pang(i, j)

        tmp = count_sang()
        ans = max(ans, tmp)

print(ans // 2)