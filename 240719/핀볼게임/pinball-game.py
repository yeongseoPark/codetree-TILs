# 1 /
# 2 \

n = int(input())
graph = [ 
    list(map(int, input().split()))
    for _ in range(n)
]

dr = [0, 1, 0, -1] # 동 남 서 북 
dc = [1, 0, -1, 0] 

dirs = {
    0: [(i, 0) for i in range(n)],   # 동
    1: [(0, j) for j in range(n)],   # 남 
    2: [(i, n-1) for i in range(n)], # 서
    3: [(n-1, j) for j in range(n)]  # 북
    }

def cursor(nk, k): # 값, 방향
    if nk == 1: # /
        if k == 0:
            k = 3
        elif k == 1:
            k = 2      
        elif k == 2:
            k = 1
        elif k == 3:
            k = 0
    elif nk == 2: # \
        if k == 0:
            k = 1
        elif k == 1:
            k = 0
        elif k == 2:
            k = 3
        elif k == 3:
            k = 2

    return k

def move(r, c, k): # K는 현재 방향 
    cnt = 1 
    nk = graph[r][c]
    k = cursor(nk, k)
    r, c = r + dr[k] , c + dc[k]
    while 0 <= r < n and 0 <= c < n:
        cnt += 1
        nk = graph[r][c]
        k = cursor(nk, k)
        r += dr[k] 
        c += dc[k]
    
    return cnt + 1 

ans = 0 
for k , v in dirs.items():
    for r, c in v:
        ans = max(ans, move(r, c, k))

print(ans)