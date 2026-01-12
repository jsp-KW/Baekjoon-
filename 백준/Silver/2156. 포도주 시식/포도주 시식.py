import sys


n = int (sys.stdin.readline())

drinks =[0]
for _ in range (n) :
    temp = int(sys.stdin.readline())
    drinks.append(temp)


# successive_cnt 
dp = [0]*(n+1)

if n>= 1 :
    dp[1] = drinks[1]
if n>= 2 :
    dp[2] = drinks[1] +drinks[2]


for i in range (3, n+1) :
    dp[i] = max (
        dp[i-1],
        dp[i-2]+drinks[i],
        dp[i-3] +drinks[i-1] + drinks[i]

    )

print (dp[n])