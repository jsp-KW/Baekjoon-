import sys
from collections import deque

N,M,R = map(int,sys.stdin.readline().split())

graph = [[] for _ in range (N+1)]

for _ in range (M) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for row in graph:
    row.sort()

visited = [-1]*(N+1)

depth = 0

def bfs (start) :
    visited[start] = 0
    
    q = deque([start])

    while q  :
        cur = q.popleft()
        
        for nxt in graph[cur] :
            if visited[nxt] == -1 :
                visited[nxt] = visited[cur] +1 
                q.append(nxt)


bfs (R)

for i in range (1,N+1) :
    print(visited[i])

    