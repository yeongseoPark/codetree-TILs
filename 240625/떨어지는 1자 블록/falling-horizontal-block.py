n , m, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

k -= 1

cur_row = 0
while True:
    touched = False
    for col in range(k, k + m):
        if grid[cur_row][col]:
            touched = True 
            break

    if touched:
        break
    
    cur_row += 1

    if cur_row == n:
        break

for col in range(k, k + m):
    grid[cur_row - 1][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    
    print()