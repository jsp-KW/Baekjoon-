import sys

# 준규가 사는 나라에서는 수 3개를 이용해서 연도를 나타낸다,
# 각각의 수는 지구, 태양, 그리고 달을 나타낸다

# 지구를 나타내는 수를 E, 태양 S, 달 M
# 1년은 준규가 살고있는 나라에서 1 1 1 로 나타낼 수 있음
# 1년이 지날 때 마다, 세수는 1 씩 증가,
# 15년은 15 15 15, 1년 지나면 1 16 16 이 된다 E 가 1<=E<=15 라서

year = 1

E,S,M = map(int,sys.stdin.readline().split())

while True :
    if (year-E)%15 == 0 and (year-S) %28 == 0 and (year-M)%19 == 0 :
        print(year)
        break
    year +=1

