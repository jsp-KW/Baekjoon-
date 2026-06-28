from collections import deque

def solution(n, wires):
    
    graph = [[] for _ in range (n+1)]

    
    
    for w in wires:
        
        start, end = w
        graph[start].append(end)
        graph[end].append(start)
        
    
    def bfs (start, end) :
        visited = [False] *(n+1)
        visited[start] =True
        q = deque([start])
        while q:
            cur = q.popleft()

            for nxt in graph[cur] :
                if( (cur == end and nxt== start) or (cur == start  and nxt == end) ):
                    continue
                if not visited[nxt] :
                    visited[nxt] = True
                    q.append(nxt)
        return sum(visited)
    
    answer=  float('inf')
    for connection in wires :
        start, end = connection
        
        res = bfs (start, end)
        temp = n- res
        answer = min(answer, abs(res-temp))
        
        
    return answer
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     graph = [[] for _ in range(n+1)]
    
#     for node1,node2 in wires:
#         graph[node1].append(node2)
#         graph[node2].append(node1)
    
    
#     def bfs(start, restrict):
#         visited=[False]*(n+1)
#         visited[start]= True
#         q= deque([start])
        
#         while q:
#             cur_node= q.popleft()
#             for nxt in graph[cur_node]:
#                 if cur_node == restrict[0] and nxt== restrict[1]:
#                     continue
#                 if not visited[nxt]:
#                     visited[nxt]= True
#                     q.append(nxt)
                    
#         return sum(visited)
    
#     ans= float('inf')
#     for w in wires:
#         ignore1,ignore2= w
        
#         return_val = bfs(ignore1,(ignore1,ignore2))
#         ans= min(ans,abs(return_val- (n-return_val) ))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 