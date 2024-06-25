n, r, c = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r -= 1
c -= 1

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

movement = []

while True:
    moved = False

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    movement.append(grid[r][c])
    cur_num = grid[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if is_valid(nr, nc):
            if grid[nr][nc] > cur_num:
                max_pos = (nr , nc)
                moved = True

    if not moved:
        break
    
    r = max_pos[0]
    c = max_pos[1]

for i in movement:
    print(i, end = " ")