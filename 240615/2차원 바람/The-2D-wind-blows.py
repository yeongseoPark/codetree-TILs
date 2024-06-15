n, m, q= map(int, input().split())
grid = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

temp_arr = [
    [0 for _ in range(m+1)]
    for _ in range(n+1)
]

def rotate(start_row, start_col, end_row, end_col):
    temp = grid[start_row][start_col]

    for i in range(start_row, end_row):
        grid[i][start_col] = grid[i+1][start_col]
    
    for i in range(start_col, end_col):
        grid[end_row][i] = grid[end_row][i+1]
    
    for i in range(end_row, start_row, -1):
        grid[i][end_col] = grid[i-1][end_col]
    
    for i in range(end_col, start_col, -1):
        grid[start_row][i] = grid[start_row][i-1]

    grid[start_row][start_col + 1] = temp

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= m

def average(x, y):
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]

    nums = []
    for dx, dy in zip(dxs, dys):
        if in_range(x+ dx, y+dy):
            nums.append(grid[x+dx][y+dy])
    
    return sum(nums) // len(nums) 

def change_number(start_row, start_col, end_row, end_col):
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            temp_arr[row][col] = average(row, col)
    
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            grid[row][col] = temp_arr[row][col]

def simulate(start_row, start_col, end_row, end_col):
    rotate(start_row, start_col, end_row, end_col)

    change_number(start_row, start_col, end_row, end_col)

for row in range(1, n+1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        grid[row][col] = num

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    simulate(r1, c1, r2, c2)

for row in range(1, n+1):
    for col in range(1, m+1):
        print(grid[row][col], end = " ")
    print()