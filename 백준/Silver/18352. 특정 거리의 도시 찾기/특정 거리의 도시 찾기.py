import sys
from collections import deque

# 1-> N ,  M개의 단방향 도로 존재 , 도로 거리 1
# x->x 로 가는 최단 거리는 0, n=4 , k=2, x=1


N, M, K, X = map(int,sys.stdin.readline().split())

graph = [[] for _ in range (1+N)]

# X 로 부터 출발하여 도달할 수 있는 도시중, 최단 거리가 k인 모든 도시의 번호를
# 하나의 오름차순으로 출력하자

distance = [-1]*(N+1)

for _ in range (M) :
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)



def bfs (start) :
    distance[start] = 0
    q= deque([start])

    while q :
        cur_node = q.popleft()

        for nxt in graph[cur_node] :
            if distance[nxt] == -1 :
                distance[nxt]= distance[cur_node] +1
                q.append(nxt)

bfs (X)

answer = []
for i in  range (1, len(distance)) :
    if distance[i] == K :
        print(i)
        answer.append(i)

if len(answer) == 0 :
    print(-1)


