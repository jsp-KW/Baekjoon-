import sys
from collections import deque



# n 개의 트럭이 건너가려한다
# 다리 길이 : w 
# 각 트럭들은 하나의 단위시간에 하나의 단위길이 만큼만 이동할 수 있다
# 최대 하중 L


n,w,L = map(int,sys.stdin.readline().split())
trucks = deque(map(int,sys.stdin.readline().split()))

time = 0

bridge = deque([0]*(w))
q = deque(trucks)
cur_bridge_weight = 0

while trucks or cur_bridge_weight > 0 :

    out_truck = bridge.popleft()
    cur_bridge_weight -= out_truck

    if trucks and cur_bridge_weight + trucks[0] <= L :
        truck= trucks.popleft()
        cur_bridge_weight+= truck
        bridge.append(truck)

    else: 
        bridge.append(0)

    time +=1 

print(time)
