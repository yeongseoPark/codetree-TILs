n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def is_happy_sequence(sub_list):
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, n):
        if sub_list[i-1] == sub_list[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        max_ccnt = max(max_ccnt, consecutive_count)
    
    return max_ccnt >= m

for i in range(n):
    sub_list = matrix[i]

    if is_happy_sequence(sub_list):
        ans += 1


for i in range(n):
    sub_list = []
    for j in range(n):
        sub_list.append(matrix[j][i])

    if is_happy_sequence(sub_list):
        ans += 1


print(ans)