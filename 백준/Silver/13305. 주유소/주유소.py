import sys

#N 개의 도시가 있다
#리터당 가격
#도로 길이
#1km 마다 1리터 사용
#첫 출발시 기름이 없어서 넣고 출발해야함
# 최소의 비용을 구하자
#

N = int(sys.stdin.readline())
road_lengths = list(map(int,sys.stdin.readline().split()))
oil_prices = list(map(int,sys.stdin.readline().split()))

#처음 : 일단 2번째로 가기 위한 만큼만 주유하기
#이후부터 : 이전보다 더 싼거면, 주유하기
#그니까 주유했다고 가정하고 계산하면 됨
min_oil = oil_prices[0]
cost = min_oil * road_lengths[0] 
for i in range (1,N-1):
    if min_oil > oil_prices[i]:
        min_oil = oil_prices[i]
    
    cost += min_oil *road_lengths[i]

print(cost)
    