from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    
#     graph = [[] *(n+1) for _ in range (n+1)]
 

#     # graph 양방향 만들기 
#     for road in roads :
#         start, end = road[0], road[1]
#         graph[start].append (end)
#         graph[end].append (start)
    
#     # bfs로직 -> python에서는 자동으로 None 타입을 반환함
#     def bfs (start) :
#         distance = [-1] *(n+1)
#         distance[start] = 0
        
#         q= deque ([start])
        
#         while q :
#             cur = q.popleft ()
            
#             for nxt in graph[cur] :
#                 if distance[nxt] ==-1 :
#                     distance[nxt] = distance[cur] +1
#                     q.append(nxt)
#         return distance
#   # destination -> source 한번만 bfs조지면 됨

#     res = bfs (destination)
    
#     for start_node in sources:
#         answer.append(res[start_node])
    
    
    
    
    
    
    
    
    
    
    graph = [[] for _ in range (n+1)]
    
    for r in roads :
        start = r[0]
        end = r[1]
        
        graph[start].append(end)
        graph[end].append(start)
        
    distance = [-1]*(n+1)
    
    def bfs(start): 
        distance[start] = 0
        q= deque([start])
        while q :
            cur_node = q.popleft()
            for nxt_node in graph[cur_node] :
                if distance[nxt_node] == -1 :
                    distance[nxt_node] = distance[cur_node] +1
                    q.append(nxt_node)
        return 
    
    bfs(destination)
    
    for target_source in sources :
        answer.append (distance[target_source]) 
            
             
    return answer