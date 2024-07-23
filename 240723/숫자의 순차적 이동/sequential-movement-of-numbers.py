n , m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dic = {} # 숫자 : 위치
for i in range(n):
    for j in range(n):
        dic[grid[i][j]] = (i, j) 

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def find_biggest(num, r, c):
    biggest_r = r
    biggest_c = c
    biggest_num = 0

    for i in range(c-1, c+2):
        if in_range(r-1, i):
            if grid[r-1][i] > biggest_num:
                biggest_num = grid[r-1][i]
                biggest_r = r-1
                biggest_c = i
    
    for i in range(c-1, c+2):
        if in_range(r+1, i):
            if grid[r+1][i] > biggest_num:
                        biggest_num = grid[r+1][i]
                        biggest_r = r+1
                        biggest_c = i

    if in_range(r, c-1):
        if grid[r][c-1] > biggest_num:
            biggest_num = grid[r][c-1]
            biggest_r = r
            biggest_c = c-1

    if in_range(r, c+1):
        if grid[r][c+1] > biggest_num:
            biggest_num = grid[r][c+1]
            biggest_r = r
            biggest_c = c+1
    
    return (biggest_r, biggest_c)

for _ in range(m):
    for num in range(1, n*n + 1):
        r = dic[num][0]
        c = dic[num][1]
        nr, nc = find_biggest(num, r, c)
        tmp = grid[r][c]
        grid[r][c] = grid[nr][nc]
        grid[nr][nc] = tmp

        for i in range(n):
            for j in range(n):
                dic[grid[i][j]] = (i, j) 

for i in range(n):
    for j in range(n):
        print(grid[i][j], end= " ") 
    print()