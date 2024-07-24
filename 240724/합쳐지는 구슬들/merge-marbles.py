n, m, t = map(int, input().split())

# r행 c열 d방향 w무게
# d : U / D / R / L 
marbles = [
    list(input().split())
    for _ in range(m)
]

grid = [
    [[] for _ in range(n)] 
    for _ in range(n)
]

next_grid = [
    [[] for _ in range(n)] 
    for _ in range(n)
]

for i in range(len(marbles)):
    r, c, d, w = marbles[i]
    r = int(r) -1 
    c = int(c) -1
    grid[r][c].append((int(i),d,int(w))) # 번호, 방향, 무게

# U D R L
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

dxdy_map = {
    "U" : 0,
    "D" : 1,
    "R" : 2,
    "L" : 3
}

reverse_map = {
    "U" : "D",
    "D" : "U",
    "L" : "R",
    "R" : "L"
}

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def merge():
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] != []:
                most_num = -1
                most_direction = None
                sum_weight = 0
                for id, d, w in next_grid[i][j]:
                    sum_weight += w
                    if id > most_num:
                        most_num = id
                        most_direction = d
                
                next_grid[i][j] = [(most_num, most_direction, sum_weight)]


def move():
    for r in range(n):
        for c in range(n):
            if grid[r][c] != []:
                i = grid[r][c][0][0]
                d = grid[r][c][0][1]
                w = grid[r][c][0][2]
    
                direction = dxdy_map[d]
                nr = r + dx[direction]
                nc = c + dy[direction]
                if not in_range(nr, nc): # 벽에 부딪히면(나가면) 방향 뒤집고 끝
                    d = reverse_map[d]
                    next_grid[r][c].append((i, d, w)) # 방향만 바꾼채로 넣기
                    continue
                    
                next_grid[nr][nc].append((i, d, w)) 
    


for _ in range(t):
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = []

    move()

    merge()

    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]

cnt = 0 
max_val = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != []:
            cnt += 1
            max_val = max(max_val, grid[i][j][0][2])

print(cnt, max_val)