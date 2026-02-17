import sys
import heapq
# 가중치 존재
# 최단 경로

V,E = map(int,sys.stdin.readline().split())
start_node = int(sys.stdin.readline())

graph = [[] for _ in range (V+1)]

for _ in range (E) :
    u,v,cost  = map(int,sys.stdin.readline().split())
    graph[u].append ((cost,v))


# 일단최단경로
# start_node 를 기준으로 방문해서, 최소 경로의 경로값을 출력하자
# 시작점은 0으로 출력하고, 경로 존재 x 경우 INF를 출력하자


INF = float('inf')
distance = [INF] *(V+1)

def dijkstra (start) :
    q = []
    heapq.heappush(q, (0,start))
    distance [start] = 0

    while q :

        cur_cost ,now = heapq.heappop(q)

        if distance[now]  < cur_cost :
            continue

        for nxt_cost,nxt_node  in graph[now] :
            cost = nxt_cost + cur_cost
            
            if cost  < distance[nxt_node]:
                distance[nxt_node] = cost
                heapq.heappush (q, (cost,nxt_node))


dijkstra(start_node)

for i in range (1,V+1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])