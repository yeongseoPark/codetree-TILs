from collections import deque
from copy import deepcopy

a = input().rstrip()
val = 1000

def encode(deq_a):
    seq = 1
    prev = deq_a[0]
    ans = ""
    for i in range(1, len(deq_a)):
        if deq_a[i] == prev:
            seq += 1
        else:
            ans += prev + str(seq)
            prev = deq_a[i]
            seq = 1
    ans += prev + str(seq)
    
    return ans

for shift in range(len(a)):
    deq_a = deque(list(a))
    for _ in range(shift):
        tmp = deq_a.pop()
        deq_a.appendleft(tmp)
    cur = encode(deq_a)
    val = min(val, len(cur))

print(val)