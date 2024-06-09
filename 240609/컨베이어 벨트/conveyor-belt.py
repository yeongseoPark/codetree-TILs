n, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2)]

for _ in range(t):
    top_right = grid[0][n-1]
    bottom_right = grid[1][n-1]
    for j in range(n-1, 0, -1): # 첫 줄 이동
        grid[0][j] = grid[0][j-1]

    for j in range(n-1, 0, -1): # 두번째 줄 이동
        grid[1][j] = grid[1][j-1]

    grid[0][0] = bottom_right
    grid[1][0] = top_right

for i in range(2):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()