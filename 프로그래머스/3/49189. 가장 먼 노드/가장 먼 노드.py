from collections import deque

def solution(n, edge):
    answers = []
    graph = [[] for _ in range (n+1)]
    visited = [-1]*(n+1)
    # n개의 노드가 있는 그래프
    # 1~ n 까지의 번호
    #  1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하자,
    #  가장 멀리떨어진 노드란, 최단경로로 이동했을 때, 간선의 개수가 가장 많은 노드
    
    for e in edge :
        n1,n2 = e
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    def bfs (start,target)  :
        visited [start] = 0
        q = deque ([start])
        
        while q :
            cur = q.popleft()
            for nxt in graph[cur] :
                
                if visited[nxt] == -1  and nxt != target :
                    visited[nxt] = visited[cur] +1
                    q.append(nxt)
        
    bfs (1,n+1)
        
    max_val = max(visited)
    print (visited)
    cnt = 0 
    for ans in visited :
        if max_val == ans :
            cnt +=1
    return cnt