reverse = 0
straight = 1

n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def rotate(x, y, k, l, direction):
    if direction == reverse:
        dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
        move_nums = [k, l, k, l]

    else:
        dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
        move_nums = [l, k, l, k]

    # 1 복사
    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]
    
    # 2 회전
    for dx, dy, move_num in zip(move_nums):
        for _ in range(move_num):
            nx, ny = x + dx, y + dy
            temp[nx][ny] = grid[x][y]
            x, y = nx, ny
    
    # 다시 복사
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

row, col, m1, m2, m3, m4, direction = map(int, input().split())

rotate(row-1, col-1, m1, m2, direction)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()