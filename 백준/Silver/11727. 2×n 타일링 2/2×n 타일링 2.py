import sys

# 2xn 의 크기의 직사각형을 채우는 방법의 수를 10007로 나눈 나머지


n = int(sys.stdin.readline())

# 1x2, 2x1, 2x2로 채우는 경우 3가지


# n=0 -> 1
# n=1 , 넓이 2x1  ->1
# n=2 , 2x2 -> 1x2 2개 ,2x1 2개, 2x2 => 3개
# n=3 , 넓이 2x3 -> 2x1 3개, 2x2 한개 + 1x2한개or 2x1 한개 =>5개

if n == 1 or n==0:
    print(1)
    exit()

dp = [0] * (n + 1)
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])
