import sys
from collections import deque
# sys.setrecursionlimit(10**6) 
# N = int(sys.stdin.readline())
# #root 가 1


# connections = [[] for _ in range(N+1)]
# visited =[False]* (N+1)
# for _ in range (N-1) :
#     A,B = map(int,sys.stdin.readline().split())
#     connections[A].append(B)
#     connections[B].append(A)


# parents = [0] *(N+1)
# #print(connections)
# def dfs (start) :
    
#     visited[start] = True
    
#     for node in connections[start]:
#         if visited[node] != True :
#             parents[node] = start
#             dfs(node) 
#     return visited


# dfs (1)

# for i in range (2,N+1) :
#     print(parents[i])

input = sys.stdin.readline
N = int(input())
g = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

parent = [0]*(N+1)
visited = [False] *(N+1)

def bfs (start) :
    visited[start] = True
    q = deque()
    q.append(start)
    while q :
        cur = q.popleft()
        for node in g[cur]:
            if visited[node] != True :
                visited[node] = True
                parent[node] = cur
                q.append(node)

bfs(1)

for i in range(2,N+1) :
    print(parent[i])
                
