import sys
from collections import defaultdict
N,K = map(int,sys.stdin.readline().split())

# 부분합

arr = list(map(int, sys.stdin.readline().split()))

sum = 0
answer = 0

# 구간합 
sum_arr = [0]*(N+1)

for i in range (1,N+1) :
    sum_arr[i] = sum_arr[i-1] + arr[i-1]
    

cnt = defaultdict(int)

for s in sum_arr :
    
    temp = s-K
    answer += cnt[temp]
    cnt[s] +=1 
    

print (answer)

