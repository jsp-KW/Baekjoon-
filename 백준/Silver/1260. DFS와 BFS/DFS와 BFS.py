from collections import deque 
import sys

n,m,v = map (int, sys.stdin.readline().split())


graph = [[0]* (n+1)  for _ in range (n+1)]
visited = [0] *(n +1)


# 노드 연결하기
for _ in range (m) :
    a,b = map (int, input ().split())
    graph [a][b] = graph [b][a] = 1


#print ("양방향 정점을 이은 그래프 출력", graph)


def dfs (v) :

    visited [v] = 1
    print (v, end =' ')

    for i in range (1, n+1) :
        if (visited[i] ==0  and graph [v][i] ==1) :
            dfs(i)


def bfs (v) :

    q = deque ([v])

    visited[v] = 0

    while q:
        v= q.popleft()
        print (v, end= ' ')

        for i in range (1,n+1):
            if visited[i] ==1  and graph[v][i] ==1 :
                q.append(i)
                visited[i] = 0       

dfs(v)
print()
bfs(v)
