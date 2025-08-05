import sys
import math

X,Y,D,T = map(int, sys.stdin.readline().split())

# 걷기 : 1초에 1만큼
# 점프 : T초에 D만큼(일직선만 가능)
# X,Y -> 0,0 으로 가는데까지 걸리는 시간의 최솟값, 두가지 방법을 적절히 조합해서


home_distance = math.sqrt(X**2 + Y**2)

if home_distance >= D :
    case1 = home_distance # 그냥 걷기
    case2 = (home_distance//D) *T + (home_distance- (home_distance//D)*D) #점프최대한 하고 + 남은거리 걷기
    case3 =((home_distance//D)+1)*T

    min_result = min (case1,case2,case3)
    min_result=round(min_result,9)
    print (min_result)

# 점프를 이용한 경우
# 걷기만 하는경우, 점프를 1번 + 걷기, 점프를 2번
else : #집까지의 거리가 충분히 점프거리보다 작은 경우
    case1 = home_distance # 걷기로만 가기
    case2 = T + (D-home_distance) #점프 한번 해서 초과하고 뒤로 걸어오기
    case3 = 2*T
    
    min_result = min(case1,case2,case3)
    min_result= round(min_result,9)
    print(min_result)
