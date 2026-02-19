import sys
import heapq

#N개의 도시가 있다
# M 개의 버스가 있다
# A번째 도시에서 B번째 도시까지 가는데 버스 비용을 최소화
# A번째 도시에서 B번째 도시까지가 가는데 최소비용을 출력하자.

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range (N+1)]

for _ in range (M) :
    start,end,cost = map(int,sys.stdin.readline().split())
    graph[start].append ((cost,end))

start_city, target_city = map(int,sys.stdin.readline().split())


q = [(0,start_city)]

INF = float('inf')

distance = [INF]*(N+1)
distance [start_city] = 0

while q :
    
    cur_cost, cur_node = heapq.heappop(q)

    if distance[cur_node]  < cur_cost :
        continue

    if target_city == cur_node :
        print (distance[cur_node])
        break

    distance[cur_node] = cur_cost

    for nxt_cost, nxt_node in graph[cur_node] :
        temp=cur_cost +nxt_cost
        
        if distance[nxt_node] >  temp :
            distance[nxt_node] = temp
            heapq.heappush(q, (temp,nxt_node))


