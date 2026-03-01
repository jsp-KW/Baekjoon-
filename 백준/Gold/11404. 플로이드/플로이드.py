import sys
import heapq

#A->B 로 갈대, 필요한 비용의 최소값

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

citys = [[] for _ in range (n+1)]


for _ in range (m) :
    start, end, cost = map(int,sys.stdin.readline().split())
    citys[start].append((cost, end))

INF = float('inf')

def dijkstra(start) :
    q= [(0,start)]
    distance = [INF]*(n+1)
    distance[start] = 0

    while q  :
        
        cur_cost, cur_node = heapq.heappop(q)

        if distance[cur_node] < cur_cost :
            continue 

        for nxt_cost, nxt_node in citys[cur_node] :
            total_cost = nxt_cost + cur_cost 
            if distance[nxt_node] > total_cost :
                distance[nxt_node]  = distance[cur_node] + nxt_cost
                heapq.heappush(q,(total_cost, nxt_node))
    return distance



# 다익스트라를, 1번노드~ n번까지 호출
# 각 호출당, 시작점부터 다른 노드까지 최소비용이 계산된다
# 그러므로 for문 하나로 가능
for i in range (1,n+1) :
    answers = dijkstra(i)
    inf_processed = []
    for ans in answers :
        if ans == INF :
            inf_processed.append(0)
            continue
        inf_processed.append(ans)
    print(* inf_processed[1:])
        

    
            
            
    