import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range (N+1)]
visited = [False]*(N+1)

for _ in range (N-1) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visit_order = list(map(int,sys.stdin.readline().split()))
rank = [0]*(N+1)

for i in range (N) :
    rank[visit_order[i]] = i


for row in graph :
    row.sort(key=lambda x:(rank[x]))

def bfs (start) :
    visited[start] = True
    q= deque([start])
    test_path = []
    
    while q :
        cur = q.popleft()
        test_path.append(cur)
        for nxt in graph[cur] :
            if not visited[nxt] :
                visited[nxt] = True
                q.append(nxt)

    if test_path == visit_order :
        print(1)
    else: print(0)
bfs(1)
