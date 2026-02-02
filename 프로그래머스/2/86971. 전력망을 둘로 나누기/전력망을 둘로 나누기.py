from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for node1,node2 in wires:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    
    def bfs(start, restrict):
        visited=[False]*(n+1)
        visited[start]= True
        q= deque([start])
        
        while q:
            cur_node= q.popleft()
            for nxt in graph[cur_node]:
                if cur_node == restrict[0] and nxt== restrict[1]:
                    continue
                if not visited[nxt]:
                    visited[nxt]= True
                    q.append(nxt)
                    
        return sum(visited)
    
    ans= float('inf')
    for w in wires:
        ignore1,ignore2= w
        
        return_val = bfs(ignore1,(ignore1,ignore2))
        ans= min(ans,abs(return_val- (n-return_val) ))
        
        
    return ans