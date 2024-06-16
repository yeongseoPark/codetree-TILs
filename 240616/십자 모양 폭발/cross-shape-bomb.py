def is_valid(r,c):
    return 0 <= r < n and 0 <= c < n

def bomb(r, c):
    length = grid[r][c]

    grid[r][c] = 0
    for i in range(length):
        if is_valid(r+i, c):
            grid[r+i][c] = 0
        if is_valid(r-i, c):
            grid[r-i][c] = 0
        if is_valid(r, c+i):
            grid[r][c+i] = 0 
        if is_valid(r, c-i):
            grid[r][c-i] = 0

def pull():
    for col in range(n):
        temp = [0 for _ in range(n)]
        temp_idx = 0
    
        for i in range(n-1, -1, -1):
            if grid[i][col] != 0:
                temp[temp_idx] = grid[i][col]
                temp_idx += 1
        
        for i in range(n-1, -1, -1):
            grid[i][col] = temp[n-i-1]

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

row, col = map(int, input().split())

bomb(row-1,col-1)
pull() 

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()