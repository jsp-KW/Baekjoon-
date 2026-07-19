import heapq 

def solution(N, road, K):
#     answer = 0
#     graph = [[] for _ in range (N+1) ]
#     for r in road :
#         a= r[0]
#         b= r[1]
#         cost = r[2]
#         graph[a].append((cost, b))
#         graph[b].append((cost,a))
    
#     INF = float('inf')
#     distance = [INF] *(N+1) 
        
#     def dijkstra(start) :
#         q = [(0,start)]
   
#         distance[start] = 0
        
#         while q  :
#             cur_cost, cur_node = heapq.heappop(q) 
            
#             if cur_cost > distance[cur_node] :
#                 continue 
            
#             for nxt_cost, nxt_node in graph[cur_node] :
#                 total_cost = nxt_cost + cur_cost
#                 if total_cost < distance[nxt_node] :
#                     distance [nxt_node] = total_cost 
#                     heapq.heappush (q,(total_cost, nxt_node))
    
        
#     dijkstra(1)
#     for i in range (1, N+1) :
#         if distance[i] <= K :
#             answer +=1

    answer =0
    graph = [[] for _ in range (N+1)]
    
    for r in road :
        a = r[0]
        b= r[1]
        cost = r[2]
        graph[a].append((cost, b))
        graph[b].append((cost,a))
    
    INF = float('inf')
    distance = [INF] * (N+1)
    distance[1] = 0
    
    pq = [(0,1)]
    
    while pq :
        
        cur_cost, cur_node= heapq.heappop(pq)
        if (distance[cur_node] < cur_cost) :
            continue
            
        distance[cur_node] = cur_cost
        
        for nxt_cost, nxt_node in graph[cur_node]:
            total_cost = cur_cost + nxt_cost
            if distance[nxt_node] > total_cost :
                distance[nxt_node] = total_cost
                heapq.heappush(pq, (total_cost, nxt_node))
    
    
    for num in distance :
        if num <= K :
            answer+=1
    return answer