n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr = [0] + arr
first  = tuple(map(int, input().split()))
second = tuple(map(int, input().split()))

def reduce(start, end):
    temp = []

    for i in range(1, len(arr)):
        if i < start or i > end:
            temp.append(arr[i])
    
    return [0] + temp

arr = reduce(first[0], first[1])
arr = reduce(second[0], second[1])


print(len(arr) -1)
for i in range(1, len(arr)):
    print(arr[i])