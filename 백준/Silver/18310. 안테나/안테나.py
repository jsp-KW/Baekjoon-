import sys

# 모든 집까지의거리의 총 합이 최소가되도록 설치
# 집에 있는곳에만 설치 가능

N = int(sys.stdin.readline())
home_loc = list(map(int,sys.stdin.readline().split()))
home_loc.sort()


# min~max 까지 있고, 그중 하나 설치

# 1 5 7 9 , 7이라면,  6, 2 ,0 2 10 임로, 작은값
# 중앙값이 가장 최소일듯한데,,

if N %2 == 0 :
    median = home_loc[(N-1) //2]
else:
    median = home_loc [N//2]

print(median)