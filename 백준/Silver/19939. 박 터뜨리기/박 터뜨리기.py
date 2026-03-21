import sys

N,K = map(int,sys.stdin.readline().split())

# n개의 공 k개 바구니
# 5 개공 3개의 바구니/ 3개 바구니 각각 다르게 할 수 없어서 -1
# 최대 개수 최소개수의 차이를 줄인다,=

#7개 공, 3개 바구니 -> 1 2 4
var = 1
sangsu = sum([i for i in range (1,K+1)])
temp = N-sangsu
if N < sangsu:
    print(-1)
else :
    if temp% K == 0 :
        print(K-1)
    else:
        print(K)
