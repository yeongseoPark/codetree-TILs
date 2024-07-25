k, n = map(int, input().split())

answer = []

def print_ans():
    for i in answer:
        print(i, end = " ")
    print()

def choose(cur_num):
    if cur_num == n:
        print_ans()
        return
    
    for i in range(1, k+1):
        answer.append(i)
        choose(cur_num + 1)
        answer.pop()

choose(0)