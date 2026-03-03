import sys
sys.setrecursionlimit(10**5)

# DFS, 

N,M, R = map(int,sys.stdin.readline().split())

graph = [[]for _ in range (N+1)]
for _ in range (M) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for row in graph:
    row.sort()

visited= [-1]*(N+1)

depth = 0
def dfs (start, depth) :
    visited[start] = depth
    for nxt in graph[start] :
        if visited[nxt] == -1 :
            dfs(nxt, depth +1)

dfs(R, depth )
for i in range (1, len(visited)) :
    print(visited[i])