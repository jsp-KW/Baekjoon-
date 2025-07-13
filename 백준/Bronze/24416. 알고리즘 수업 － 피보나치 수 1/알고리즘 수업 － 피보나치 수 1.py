import sys

N = int (input())


def fib(n) :
    global cnt1  
 
    if n ==1 or n ==2 :
        cnt1+=1
        return 1
    else :
        return fib(n-1) + fib(n-2)

cnt2 = 0
dp = [0]* (N+1)
dp[0] =1
dp[1] =1

cnt1 = 0
for i in range(2,N+1):
    dp[i] = dp [i-1] + dp[i-2]
    cnt2 +=1

fib(N)
print (cnt1, cnt2-1)