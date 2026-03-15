import sys

N = int(sys.stdin.readline())

matrix_sizes =[]
# DP[i][j]  i 번 행렬부터 j번 행렬까지 곱할때 필요한 최소 연산의 수
# i~j 에서 k번째 나눈다면, i~k , k+1~j
# dp[i][k] + dp[k+1][j] + matrix[i][0]xmatrix[k][1]x matrix[j][1]
# 왼쪽행렬 연산 + 오른쪽 행렬 연산 + 최종 왼+오 합치고 연산

for _ in range (N):
    row,col = map(int,sys.stdin.readline().split())
    matrix_sizes.append((row,col))


dp= [[0]*(N) for _ in range (N)]


INF= float('inf')
# (AB)CD #괄호 가능구간 0,1,2 / 0이면 끝점 1, 1이면 2, 2면 3-> N-length+1
for length  in range (2,N+1) : #행렬 길이()길이
    for i in range (N-length+1) :#0,1,2 
        j = i+length -1
        dp[i][j] = INF

        for k in range (i,j) : #왼쪽 부분의 끝 : (i~k) x (k+1 ~j)
            cost = (dp[i][k] + dp[k+1][j] + matrix_sizes[i][0]* matrix_sizes[k+1][0]* matrix_sizes[j][1])
            dp[i][j] = min(dp[i][j], cost)


print(dp[0][N-1])

