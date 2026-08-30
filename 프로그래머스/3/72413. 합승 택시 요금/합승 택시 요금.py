import heapq
def solution(n, s, a, b, fares):
    
    # 무지가 택시요금을 얼마나 아낄 수 있는지 계산해보고 어피치에게 합승을 제안
    # s번지점에서 출발, A의 도착 지점 a, B의 도착지점 b  지점 사이의 예상 택시요금을 나타내는 fares
    
    answer = float ('inf')
    # S -> K -> A,B
    
    graph = [[] for _ in range (n+1)]
    
    INF = float('inf')


    for t in fares :
        start  = t[0]
        end = t[1]
        cost = t[2]
        
        graph[start].append((cost, end))
        graph[end].append((cost,start))
        
    def dijkstra(start) :
            
        distance = [INF] *(n+1)
    
        q = []
        distance[start] = 0
        heapq.heappush (q, (0, start))
        
        while q: 
            cur_cost , cur_node = heapq.heappop(q)
            
            if cur_cost > distance[cur_node] :
                continue
            
            for nxt_cost, nxt_node in graph[cur_node] :
                total_cost = nxt_cost +  cur_cost 
                if total_cost < distance[nxt_node] :
                    distance[nxt_node] = total_cost
                    heapq.heappush (q, (total_cost, nxt_node))
        return distance
    
    # s에서 출발한 다익스트라 -> k까지? -> k에서 a, b 비용 
    # s
    
    distance_s = dijkstra(s)
    distance_a = dijkstra(a)
    distance_b = dijkstra(b)
    
    # s에서 시작하는 최단거리
    # a에서 시작하는 최단 거리
    # b에서 시작하는 최단 거리
    
    
    for k in range (1, n+1) :
        answer = min (answer, distance_s[k] + distance_a[k] +  distance_b[k])
       
        
        

    return answer