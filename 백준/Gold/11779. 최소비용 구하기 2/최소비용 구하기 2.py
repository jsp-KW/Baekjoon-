import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph =[[] for _ in range (n+1)]

for _ in range (m) :
    start,end,cost =  map(int,sys.stdin.readline().split())
    graph[start].append((cost,end))

start_city, end_city = map(int,sys.stdin.readline().split())

path = {start_city,}
INF=  float('inf')

# 최소 비용과 경로를 출력하자.
parent = [0]*(n+1)
def dijkstra(start) :
    q = ([(0,start)])
    distance = [INF]*(n+1)
    distance[start] = 0

    while q :
        cur_cost, cur_city = heapq.heappop(q)

        if cur_cost > distance [cur_city] :
            continue
        
        if cur_city == end_city :
            print(distance[cur_city])
            break

        distance[cur_city] = cur_cost 

        for nxt_cost, nxt_city in graph[cur_city] :
            total_cost = nxt_cost + distance[cur_city]
            if total_cost  < distance[nxt_city]:
                distance[nxt_city] = total_cost
                heapq.heappush(q,(total_cost,nxt_city))
                parent[nxt_city] = cur_city


dijkstra(start_city)
path = []
cur = end_city
while cur !=0:
    path.append(cur)
    cur = parent[cur]

path.reverse()
print(len(path))
print(*path)