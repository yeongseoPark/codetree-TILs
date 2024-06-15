n = int(input())

grid = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

# m1, m2, m3, m4 방향
right_up   = (-1, 1)
left_up    = (-1, -1)
left_down  = (1, -1)
right_down = (1, 1)

def rotate(row, col, m1, m2, m3, m4, direction):
    # 각 꼭짓점
    bottom_row, bottom_col = row, col
    right_row, right_col   = row + (m1-1) * right_up[0], col + (m1-1) * right_up[1]
    top_row, top_col       = right_row + (m2-1) * left_up[0], right_col + (m2-1) * left_up[1]
    left_row, left_col     = top_row + (m3-1) * left_down[0], top_col + (m3-1) * left_down[1]

    if direction: # 시계 방향 회전
        temp = grid[bottom_row][bottom_col]

        for i in range(m1-1):
            grid[bottom_row + (i * right_up[0])][bottom_col + (i * right_up[1])] = grid[bottom_row + ((i+1) * right_up[0])][bottom_col + ((i+1) * right_up[1])] 

        for i in range(m2-1):
            grid[right_row + (i * left_up[0])][right_col + (i * left_up[1])] = grid[right_row + ((i+1) * left_up[0])][right_col + ((i+1) * left_up[1])]

        for i in range(m3-1):
            grid[top_row + (i * left_down[0])][top_col + (i * left_down[1])] = grid[top_row + ((i+1) * left_down[0])][top_col + ((i+1) * left_down[1])]

        for i in range(m4-1):
            grid[left_row + (i * right_down[0])][left_col + (i * right_down[1])] = grid[left_row + ((i+1) * right_down[0])][left_col + ((i+1) * right_down[1])]
        
        grid[left_row + ((m4-1) * right_down[0])][left_col + ((m4-1) * right_down[1])] = temp

    else: # 반시계 방향 회전
        temp = grid[bottom_row][bottom_col]

        for i in range(m4-1):
            grid[bottom_row + (i * right_down[0])][bottom_col + (i * right_down[1])] = grid[bottom_row + ((i+1) * right_down[0])][bottom_col + ((i+1) * right_down[1])]

        for i in range(m3-1):
            grid[left_row + (i * left_down[0])][left_col + (i * left_down[1])] = grid[left_row + ((i+1) * left_down[0])][left_col + ((i+1) * left_down[1])]
        
        for i in range(m2-1):
            grid[top_row + (i * left_up[0])][top_col + (i * left_up[1])] = grid[top_row + ((i+1) * left_up[0])][top_col + ((i+1) * left_up[1])] 
        
        for i in range(m1-1):
            grid[right_row + (i * right_up[0])][right_col + (i * right_up[1])] = grid[right_row + ((i+1) * right_up[0])][right_col + ((i+1) * right_up[1])]

        grid[right_row + ((m1-1) * right_up[0])][right_col + ((m1-1) * right_up[1])] = temp

for row in range(1, n+1):
    cur_list = list(map(int, input().split()))
    for col, num in enumerate(cur_list, start=1):
        grid[row][col] = num

row, col, m1, m2, m3, m4, direction = map(int, input().split())

rotate(row, col, m1, m2, m3, m4, direction)

for i in range(1, n+1):
    for j in range(1, n+1):
        print(grid[i][j], end=" ")
    print()