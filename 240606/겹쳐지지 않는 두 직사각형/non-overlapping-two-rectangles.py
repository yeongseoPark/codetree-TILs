n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

max_row = n
max_col = m

def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def not_duplicated(i, r, j, c, row_start, row_end, col_start, col_end):
    if row_start <= i <= row_end or row_start <= i + r <= row_end or col_start <= j <= col_end or col_start <= j + c <= col_end:
        return False
    
    return True

def get_sum(row_start, row_end, col_start, col_end):
    tmp = 0
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            tmp += grid[i][j]
    
    return tmp

def second_rec(row_start, row_end, col_start, col_end):
    tmp = float('-inf')
    for i in range(n):
        for j in range(m):
            for r in range(max_row):
                for c in range(max_col):
                    if in_range(i + r, j + c) and not_duplicated(i, r, j, c, row_start, row_end, col_start, col_end):
                        row_range = (i, i+r)
                        col_range = (j, j+c) 

                        mine    = get_sum(row_range[0], row_range[1], col_range[0], col_range[1])

                        tmp = max(tmp, mine) 
    
    return 0 if tmp == float('-inf') else tmp

ans = float('-inf')
for i in range(n):
    for j in range(m):
        for r in range(max_row):
            for c in range(max_col):
                if in_range(i + r, j + c):
                    row_range = (i, i+r)
                    col_range = (j, j+c) 

                    mine    = get_sum(row_range[0], row_range[1], col_range[0], col_range[1])
                    another = second_rec(row_range[0], row_range[1], col_range[0], col_range[1])

                    ans = max(ans, mine + another) 

print(ans)