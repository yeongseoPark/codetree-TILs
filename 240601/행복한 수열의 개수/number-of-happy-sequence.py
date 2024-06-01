n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    sub_list = matrix[i]

    for idx in range(len(sub_list)):
        if idx + m <= n:
            sub_sub_list = sub_list[idx : idx + m]
            if len(set(sub_sub_list)) == 1:
                ans += 1
                break


for i in range(n):
    sub_list = []
    for j in range(n):
        sub_list.append(matrix[j][i])

    for idx in range(len(sub_list)):
        if idx + m <= n:
            sub_sub_list = sub_list[idx : idx + m]
            if len(set(sub_sub_list)) == 1:
                ans += 1
                break


print(ans)