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

  
    
    graph = [[] *(N+1) for _ in range (N+1)]
    answer =0
    # k시간 이하로 배달 
    
    #1번마을에서
    
    for r in road :
        start = r[0]
        end = r[1]
        cost = r[2]
        
        graph[start].append((cost, end))
        graph[end].append((cost, start))
        
    
    INF = float('inf')
    distance = [INF]*(N+1)
   
    def dijkstra(start) :

        q=[(0,start)]
        distance[start] = 0
        
        
        while q  :
            cur_cost, cur_node = heapq.heappop(q)
            
            if distance[cur_node] < cur_cost :
                continue
            
            for nxt_cost, nxt_node in graph[cur_node] :
                total_cost = distance[cur_node] +nxt_cost 
                if total_cost < distance[nxt_node] :
                    distance[nxt_node] = total_cost
                    heapq.heappush(q,(total_cost, nxt_node))
    
    dijkstra(1)
    
    for i in range (1, N+1) :
        if distance[i] <= K :
            answer+=1
        
    
    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    