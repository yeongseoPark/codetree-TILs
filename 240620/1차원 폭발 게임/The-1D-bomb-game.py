n, m = map(int, input().split())

numbers = [int(input()) for _ in range(n)]

def get_end_idx_of_explosion(curr_idx, curr_num):
    for end_idx in range(len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers) - 1

while True:
    did_explode = False
    curr_idx = 0 

    while curr_idx < len(numbers):
        end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        if end_idx - curr_idx + 1 >= m:
            del numbers[curr_idx:end_idx+1] # 리스트에서 삭제
            did_explode = True
        else:
            curr_idx = end_idx + 1
        
    if not did_explode:
        break


print(len(numbers))
for number in numbers:
    print(number)