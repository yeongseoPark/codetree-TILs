n,t = map(int, input().split())

left = list(map(int, input().split()))
right = list(map(int, input().split()))
bottom = list(map(int, input().split()))


for _ in range(t):
    bottom_left = bottom[n-1]
    left_top    = left[n-1]
    right_bottom = right[n-1]
    
    for i in range(n-1, 0, -1):
        left[i] = left[i-1]

    for i in range(n-1, 0, -1):
        right[i] = right[i-1]
    
    for i in range(n-1, 0, -1):
        bottom[i] = bottom[i-1]
    
    left[0] = bottom_left
    right[0] = left_top
    bottom[0] = right_bottom

for i in left:
    print(i, end = " ")

print()

for i in right:
    print(i, end = " ")

print()

for i in bottom:
    print(i, end = " ")