import sys

N,S = map(int, sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

min_length = float('inf')

start = 0
end = 0

current_sum = 0

while True :
    if current_sum >=S :
        min_length = min(min_length, end-start)
        current_sum -= nums[start]
        start +=1
    elif end == N :
        break
    else:
        current_sum += nums[end]
        end +=1


print(min_length if min_length != float('inf') else 0)
