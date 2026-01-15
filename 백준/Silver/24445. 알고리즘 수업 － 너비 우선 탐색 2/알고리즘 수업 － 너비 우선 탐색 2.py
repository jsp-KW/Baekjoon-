import sys
from collections import deque
# 1~ N, 간선 가중치 1
# 내림차순으로 방문!


N, M,R = map(int, sys.stdin.readline().split())

graph = [[]for _ in range (N+1)]

for _ in range (M) : 
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
   
for i in range (N+1) :
    graph[i].sort(reverse=True)

visited = [0]*(N+1)
cnt = 0

def bfs (start) :
    global cnt 
    cnt +=1
    q = deque ([start])
    visited[start] = cnt
    while q :
        cur_node = q.popleft()
        for nxt in graph[cur_node] :
            if  visited[nxt] == 0 : 
                cnt +=1
                visited[nxt] = cnt
                q.append(nxt)

bfs (R)

for i in  range (0,len(visited)) :
    if i ==0 :
        continue
    print (visited[i])
    