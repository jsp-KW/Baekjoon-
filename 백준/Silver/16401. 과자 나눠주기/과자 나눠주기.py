import sys

M, N = map(int,sys.stdin.readline().split())

snacks = list(map(int,sys.stdin.readline().split()))

# 조카 수 M / 과자 개수 N 개
# 조카 1명에게 줄 수 있는 막대과자의 최대길이를 구하라
# 최대 길이 x라면, 
left = 1
right= max(snacks)

answer = 0
while left <= right :
    mid = (left + right) //2

    cnt = 0

    for snack in snacks :
        cnt += (snack // mid)

    
    if cnt >= M :
        answer = mid
        left = mid +1 
    else :
        right = mid -1

print (answer)
        
