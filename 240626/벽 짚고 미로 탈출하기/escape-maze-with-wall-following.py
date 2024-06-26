n = int(input())

r, c = map(int, input().split())

r -= 1
c -= 1

grid = [
    [i for i in list(input())]
    for _ in range(n)
]

# 우 상 좌 하
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

time = 0

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def movable(r, c):
    return grid[r][c] == "."

def check_right(direction_i, r, c):
    if direction_i == 0:
        if not is_valid(r+1, c):
            return "end"
        return "yes" if grid[r+1][c] == "#" else "no"

    elif direction_i == 1:
        if not is_valid(r, c+1):
            return "end"
        return "yes" if grid[r][c+1] == "#" else "no"

    elif direction_i == 2:
        if not is_valid(r-1, c):
            return "end"
        return "yes" if grid[r-1][c] == "#" else "no"

    elif direction_i == 3:
        if not is_valid(r, c-1):
            return "end"
        return "yes" if grid[r][c-1] == "#" else "no"

while True:
    cannot_move = True
    finished = False

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if not is_valid(nr,nc): # 밖으로 나간경우 끝냄
            finished = True
            cannot_move = False
            break

        if movable(nr, nc): # 움직일 수 있으면 움직이고
            # r = nr
            # c = nc
            cannot_move = False 

            res = check_right(i, nr, nc) # 벽짚고 이동 가능?

            if res == "yes":
                r = nr
                c = nc + 1
                break
            elif res == "no":
                if not is_valid(nr - 1, nc + 1):
                    finished = True
                    break
                r = nr - 1
                c = nc + 1
                break
            elif res == "end":
                finished = True
                break

    time += 1

    if finished or cannot_move:
        break

if cannot_move:
    print(-1)
else:
    print(time)