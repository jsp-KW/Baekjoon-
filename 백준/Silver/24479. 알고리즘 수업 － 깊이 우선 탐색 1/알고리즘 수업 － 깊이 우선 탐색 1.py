import sys
sys.setrecursionlimit(100000)
N,M,R  = map(int, sys.stdin.readline().split())

graph = [[] for _ in range (N+1)]

for _ in range (M) :
    u,v  = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] *(N+1)
for i in range (1,N+1) :
    graph[i].sort()

cnt = 0
def dfs (start):
    global cnt
    cnt+=1
    visited[start] = cnt
    
    for next in graph[start] :
        if visited[next] ==0 :
            dfs(next)


dfs (R)

for i in range (1,len(visited)) :
    print(visited[i])






