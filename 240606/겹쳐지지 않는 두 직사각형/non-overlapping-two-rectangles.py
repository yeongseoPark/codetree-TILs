n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def not_duplicated(i, r, j, c, row_start, row_end, col_start, col_end):
    if (i > row_end or i + r < row_start) or (j > col_end or j + c < col_start):
        return True
    return False

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
            for r in range(n):
                for c in range(m):
                    if in_range(i + r, j + c) and not_duplicated(i, r, j, c, row_start, row_end, col_start, col_end):
                        mine = get_sum(i, i + r, j, j + c)
                        tmp = max(tmp, mine) 
    return tmp

ans = float('-inf')
for i in range(n):
    for j in range(m):
        for r in range(n):
            for c in range(m):
                if in_range(i + r, j + c):
                    mine = get_sum(i, i + r, j, j + c)
                    another = second_rec(i, i + r, j, j + c)
                    if another != float('-inf'):
                        ans = max(ans, mine + another)

print(ans)