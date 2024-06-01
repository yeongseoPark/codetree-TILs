n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        if i + m > n or j + m > n:
            continue 
        
        cur_val = matrix[i][j]
        vertical_happy = True
        horizontal_happy= True
        
        for k in range(m):
            if matrix[i][j+k] != cur_val:
                horizontal_happy = False 
                break
        
        for k in range(m):
            if matrix[i+k][j] != cur_val:
                vertical_happy = False
                break 
        
        if vertical_happy:
            ans += 1
        if horizontal_happy:
            ans += 1

print(ans)