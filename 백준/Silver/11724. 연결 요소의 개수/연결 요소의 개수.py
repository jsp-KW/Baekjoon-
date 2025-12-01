import sys


N,M = map(int,sys.stdin.readline().split())
# 방향이 없는 그래프
# 연결 요소 개수를 구하라


# 정점의 개수 N, 간선의 개수 M
# 간선의 양 끝점 u,v 

graph = [[] for _ in range (N+1)]
for _ in range (M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] *(N+1)

def dfs (start) :
    visited [start] = True 
    
    for next in graph[start] :
        if not visited[next] :
            dfs(next)

count = 0

for i in range (1,N+1) :
    if not visited [i] :
        dfs(i)
        count +=1

print (count)

