n , m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def in_dia(i, j, x, y, k):
    if abs(i-x) + abs(j - y) <= k:
        return True

for k in range(n+1): # 가능한 k의 범위는 n을 넘어가지 않음
    cost = k * k + (k+1) * (k+1)

    for i in range(n):
        for j in range(n):
            # 모든 점에 대해 완전 탐색
            cnt = 0
            revenue = 0
            # 마름모 안에 들 수 있는 후보군들 중, 실제 마름모 안에 들고 채굴이 가능한 경우
            for y in range(i - k, i + k + 1):
                for x in range(j - k, j + k + 1):
                    if 0 <= x < n and 0 <= y < n and in_dia(i, j, x, y, k):
                        if matrix[x][y] == 1:
                            cnt += 1
                            revenue += m
        
            if revenue - cost >= 0:
                ans = max(ans, cnt) 

print(ans)