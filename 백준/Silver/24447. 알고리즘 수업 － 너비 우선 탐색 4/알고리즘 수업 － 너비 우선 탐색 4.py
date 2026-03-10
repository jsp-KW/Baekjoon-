import sys
from collections import deque

N,M,R = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(N+1)]


for _ in range(M) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for row in graph:
    row.sort()

visited_order =[-1]*(N+1)
visited_depth = [-1]*(N+1)

idx = 1 
depth =0

# 방문 순서는 꾸준히 증가해야하니까 그냥 global로 관리해서+1
# 깊이는, bfs 는 부모 -> 갈수있는 노드들-> 갈수있는 노드들 사이의 또다른 노드들 : 즉 이전 부모의 깊이+1로 관리
def bfs(start,depth):
    global idx
    visited_depth[start] = depth
    visited_order[start]= idx
    idx+=1
    depth+=1
    q= deque([start])

    while q :
        cur = q.popleft()
        for nxt in graph[cur] :
            if visited_depth[nxt]==-1 :
                visited_depth[nxt]= visited_depth[cur] +1
                visited_order[nxt]= idx
                idx+=1
                q.append(nxt)
                

bfs(R,0)
sum =0

for  i in range(1,len(visited_order)):
    if visited_order[i] == -1 :
        continue
    sum += visited_depth[i]* visited_order[i]


print(sum)