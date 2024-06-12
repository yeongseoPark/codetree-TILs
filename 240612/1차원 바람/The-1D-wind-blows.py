SHIFT_RIGHT = 0
SHIFT_LEFT = 1

n, m, q = tuple(map(int, input().split()))
a = [
    [0 for _ in range(m + 1)] for _ in range(n + 1)
]

def shift(row, curr_dir):
    if curr_dir == SHIFT_RIGHT:
        a[row].insert(1, a[row].pop())
    else:
        a[row].insert(m, a[row].pop(1))

def has_same_number(row1, row2):
    return any([
        a[row1][col] == a[row2][col]
        for col in range(1, m + 1)
    ])


def flip(curr_dir):
    return SHIFT_RIGHT if curr_dir == SHIFT_LEFT else SHIFT_LEFT


def simulate(start_row, start_dir):
    shift(start_row, start_dir)
    
    start_dir = flip(start_dir)
    
    curr_dir = start_dir
    for row in range(start_row, 1, -1):
        if has_same_number(row, row - 1):
            shift(row - 1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break
    
    curr_dir = start_dir
    for row in range(start_row, n):
        if has_same_number(row, row + 1):
            shift(row + 1, curr_dir)
            curr_dir = flip(curr_dir)
        else:
            break

for row in range(1, n + 1):
    given_nums = list(map(int, input().split()))
    for col, num in enumerate(given_nums, start = 1):
        a[row][col] = num

for _ in range(q):
    r, d = tuple(input().split())
    r = int(r)
    
    simulate(r, SHIFT_RIGHT if d == 'L' else SHIFT_LEFT)

for row in range(1, n + 1):
    for col in range(1, m + 1):
        print(a[row][col], end = " ")
    print()