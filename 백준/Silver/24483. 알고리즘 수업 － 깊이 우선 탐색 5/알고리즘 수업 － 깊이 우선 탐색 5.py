import sys
sys.setrecursionlimit(100000)

#R 부터 시작해서, i번째 노드의 깊이를 d라고 하고, R의 깊이는 0이고, 방문 안된 깊이는 -1
# 방문순서는 1, 방문 못하면 0

N,M,R  = map(int,sys.stdin.readline().split())
graph = [[] for _ in range (N+1)]


for _ in range (M) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


for row in graph:
    row.sort()

visited_depth = [-1]*(N+1)
visited_order = [0]*(N+1)

idx = 1

def dfs (start, depth) :
    global idx
    visited_depth[start] = depth
    visited_order[start] = idx
    idx+=1

    for nxt in graph[start] :
        if visited_depth[nxt] == -1 :
            dfs(nxt, depth+1)


dfs(R,0)

sum = 0

for i in range(1, len(visited_order)):
    sum +=  visited_order[i] * visited_depth[i]


print(sum)