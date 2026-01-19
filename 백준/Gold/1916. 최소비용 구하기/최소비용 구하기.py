import sys
import heapq
N = int(sys.stdin.readline())

# N 개의 도시 -> M개의 버스
# A->B 최소화
# 최소비용

M = int (sys.stdin.readline())

bus_info = [[] for _ in range (N+1) ]
for _ in range (M) :
    arrive_city_num , start_city_num, cost = map(int,sys.stdin.readline().split())
    #도착 도시, 출발도시 , 비용
    bus_info[arrive_city_num].append((start_city_num,cost))


target_start, target_arrive = map(int,sys.stdin.readline().split())

# 다익스트라

INF = float('inf')

distance = [INF] *(N+1)
distance[target_start] = 0

pq = [(0,target_start)]

while pq :
    cur_cost, cur_city = heapq.heappop(pq) 

    if cur_cost > distance[cur_city] : # 현재 도시의 비용보다 크면, continue
        continue

    if cur_city == target_arrive : #같으면 종료
        break

    for next_city, edge_cost  in bus_info[cur_city] :
        next_cost = cur_cost + edge_cost 
        if next_cost  < distance[next_city] :
            distance [next_city] = next_cost
            heapq.heappush(pq, (next_cost,next_city))

print(distance[target_arrive])