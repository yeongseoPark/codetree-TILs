n, m , t = map(int, input().split())

a = [[0] * (n+1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

next_count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def get_max_neighbor_pos(curr_x, curr_y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    max_num, max_pos = 0, (0, 0)

    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy

        if in_range(next_x, next_y) and a[next_x][next_y] > max_num:
            max_num = a[next_x][next_y]
            max_pos = (next_x, next_y)
    
    return max_pos

def move(x ,y):
    next_x, next_y = get_max_neighbor_pos(x, y)
    next_count[next_x][next_y] += 1

def move_all():
    for i in range(1, n+1):
        for j in range(1, n+1):
            next_count[i][j] = 0 

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if count[i][j] == 1:
                move(i, j) 
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count[i][j] = next_count[i][j]

def remove_duplicate_marbles():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if count[i][j] >= 2:
                count[i][j] = 0

for _ in range(m):
    x, y = map(int, input().split())
    count[x][y] = 1

for _ in range(t):
    move_all()

    remove_duplicate_marbles() 

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ans += count[i][j]

print(ans)