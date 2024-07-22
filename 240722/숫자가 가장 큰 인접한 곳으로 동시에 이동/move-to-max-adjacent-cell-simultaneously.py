n, m, t = map(int, input().split())

grid = [
    [0 for _ in range(n+1)]
]

for _ in range(n):
    grid.append([0] + list(map(int, input().split())))

count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):
    r, c = map(int, input().split())
    count[r][c] += 1 

next_count = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1]

def in_range(r, c):
    return 1 <= r <= n and 1 <= c <= n 


for _ in range(t):
    for r in range(n+1):
        for c in range(n+1):
            if count[r][c] != 0:
                cur_val = grid[r][c]
                for i in range(4):
                    if in_range(r + dx[i], c + dy[i]) and grid[r + dx[i]][c + dy[i]] > cur_val:
                        nr = r + dx[i]
                        nc = c + dx[i]
        
                next_count[nr][nc] += 1
                
    for i in range(n+1):
        for j in range(n+1):
            if next_count[i][j] >= 2:
                next_count[i][j] = 0
    
    for i in range(n+1):
        for j in range(n+1):
            count[i][j] = next_count[i][j]
            next_count[i][j] = 0

ans = 0
for i in range(n+1):
    for j in range(n+1):
        ans += count[i][j]

print(ans)