import sys


N, M = map(int,sys.stdin.readline().split())

# 연속 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하자

nums = list(map(int,sys.stdin.readline().split()))

# 연속 부분구간의 합을 저장할 dp 배열

# i,j  구간이 M 으로 나누어 떨어진다 == j까지의 합 -  0~i-1까지의 합 


count = [0]*(M)

prefix_sum = 0
answer = 0

for i in range (N) :
    prefix_sum+= nums[i]
    r = prefix_sum%M
    if r==0 :
        answer+=1
    
    count[r] +=1

# 나머지가 0인지점 3개 나머지가 1인지점 2개

for cnt in count :
    if cnt >= 2 :
        answer +=  ((cnt)*(cnt -1))//2 

print(answer)