# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def get_score(i, j, k, l):
    score = 0
    dr = [-1, -1, 1, 1]
    dc = [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    for r, c, move_num in zip(dr, dc, move_nums):
        for _ in range(move_num):
            i = i + r
            j = j + c

            if not in_range(i , j):
                return 0

            score += grid[i][j]

    return score

ans = 0

# (i, j)를 시작으로 1, 2, 3, 4 방향
# 순서대로 길이 [k, l, k, l] 만큼 이동하면 그려지는
# 기울어진 직사각형을 잡아보는
# 완전탐색을 진행해봅니다.
for i in range(n):
    for j in range(n):
        for k in range(1, n): # 1, 3 번 움직임 
            for l in range(1, n): # 2, 4 번 움직임
                ans = max(ans, get_score(i, j, k, l))

print(ans)