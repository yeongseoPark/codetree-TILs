from itertools import combinations
def check(big_row, small_row, big_col, small_col, matrix):
    for i in range(small_row, big_row + 1):
        for j in range(small_col, big_col + 1):
            if int(matrix[i][j]) < 0:
                return False
    return True

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(input().split()))

ans = 0

row_comb = list(combinations([i for i in range(n)], 2))
col_comb = list(combinations([i for i in range(m)], 2))

for i in row_comb:
    big_row   = max(i)
    small_row = min(i)
    row_len   = big_row - small_row + 1
    for j in col_comb:
        big_col   = max(j)
        small_col = min(j)
        col_len = big_col - small_col + 1

        if check(big_row, small_row, big_col, small_col, matrix):
            ans = max(ans, row_len * col_len)

print(ans if ans > 0 else -1)