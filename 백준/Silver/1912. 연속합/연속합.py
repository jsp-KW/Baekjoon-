import sys

n= int(sys.stdin.readline())

# n개의 정수로 이루어진 임의의 수열
# 연속된 수 선택 구할수있는 합중 가장 큰 합의 수를 구하자,
# 수는 한개이상 선택

# 정렬 x
temp = list(map(int,sys.stdin.readline().split()))

dp=[0]*(n)
dp[0]=temp[0]


# dp i 번째 까지의 합 이렇게 구해야하나?
# start ~end 가 i가 end 면, start 를 0부터 i-1까지 후보가있는데 어떻게 해야하지?

for i in range (1, n):
    dp[i] = max (dp[i-1] + temp[i], temp[i]) #


print(max(dp))

