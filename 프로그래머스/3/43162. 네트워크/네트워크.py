from collections import deque
def solution(n, computers):
    # A->B 연결 ->B->C연결 일 경우 A->C도 연결이 가능함
    
    answer =0
    
    visited = [False]*(n+1)
    graph = [[] for _ in range (n+1)]
    
    for i in range (0, len(computers)) :
        start = i+1
        for j in range (0, len(computers[i])) :
            if computers[i][j] == 1 and i!=j:
                graph[i+1].append(j+1)
    
    
    def bfs (start) :
        visited[start] = True
        q = deque([start])
        while q :
            cur = q.popleft ()
            for nxt in graph[cur] :
                if not visited[nxt] :
                    visited[nxt] = True
                    q.append(nxt)
        return True
    
    for i in range (1,n+1) :
        if not visited[i] :
            if bfs(i) :
                answer +=1
    return answer
    
