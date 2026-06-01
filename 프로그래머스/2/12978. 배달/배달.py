import heapq 

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range (N+1) ]
    for r in road :
        a= r[0]
        b= r[1]
        cost = r[2]
        graph[a].append((cost, b))
        graph[b].append((cost,a))
    
    INF = float('inf')

    def dijkstra(start,end) :
        q = [(0,start)]
            
        distance = [INF] *(N+1) 
    
        
        distance[start] = 0
        
        while q  :
            cur_cost, cur_node = heapq.heappop(q) 
            
            if cur_cost > distance[cur_node] :
                continue 
                
            if cur_node == end :
                return distance[end]
            
            for nxt_cost, nxt_node in graph[cur_node] :
                total_cost = nxt_cost + distance[cur_node]
                if total_cost < distance[nxt_node] :
                    distance [nxt_node] = total_cost 
                    heapq.heappush (q,(total_cost, nxt_node))
    
    for i in range (1, N+1) :
        result = dijkstra(1,i)
        if result <= K :
            answer +=1

        
    return answer