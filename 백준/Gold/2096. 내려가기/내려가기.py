import sys

N = int(sys.stdin.readline())
arr = []
for i in range (N) :
    a,b,c = map(int,sys.stdin.readline().split())

    if i == 0 :
        dp= [a,b,c] 
        dp2= [a,b,c]
    else :
        prev_max1,prev_max2, prev_max3 = dp
        prev_min1, prev_min2, prev_min3 = dp2


        dp[0] = max(prev_max1,prev_max2) +a
        dp[1] = max(prev_max1,prev_max2,prev_max3) +b
        dp[2] = max(prev_max2,prev_max3) +c

        dp2[0] = min(prev_min1,prev_min2) +a
        dp2[1] = min(prev_min1,prev_min2, prev_min3) +b
        dp2[2] = min(prev_min2, prev_min3) +c


print(max(dp),min(dp2))