from collections import deque

def solution(n, wires):
    # n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결
    # 2개로 분할, 전선들 중 하나를 끊어서
    # 송전탑의 개수를 최대한 비슷하게 맞추자
    
    # 송전탑의 개수 n, 전선 정보 wires
    
    # 두 전력망이 가지고 있는 송전탑 개수의 차이 절대값을 return 
    
    # 그니까, 끊는다 -> 어느 부분을 끊어야 할까?
    # 끊는다는건 어떻게 해야할까..
    
    
    graph = [[] for _ in range (n+1)] 

    for w in wires :
        v1,v2  = w
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # bfs  할때, 끊는 노드? 를 인자로 넘겨서, 그 노드만 제외하고 갈수있는 노드 수 카운트하고, 끊긴 노드에서 bfs 해서 노드수 둘 차이를 구해야하는건가?
    
    def bfs (start, restrict_node) :
        visited = [False] *(n+1)
        true_cnt = 0
        false_cnt = 0
        visited[start] = True
        q = deque ([start])
        
        while q  :
            cur = q.popleft()
            for nxt in graph[cur] :
                if nxt == restrict_node[1] :
                    continue
                    
                if not visited[nxt] :
                    visited[nxt] = True
                    q.append(nxt)
                    
        for i in range (1,n+1):
            if visited[i] :
                true_cnt+=1

        return abs(true_cnt - (n-true_cnt))
                
                
    min_val = 101
    
    for wire in wires:
     
        ignore1, ignore2 = wire
        min_val = min(min_val,bfs (ignore1,(ignore1,ignore2)))

        
    return min_val