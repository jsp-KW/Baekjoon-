import sys
sys.setrecursionlimit(100000)

N,M,R = map(int,sys.stdin.readline().split())

graph = [[] for _ in range (N+1)]

for _ in range (M):
    u,v= map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for row in graph:
    row.sort(reverse=True)

# depth x 방문 순서

# 1->4->3->2
# 1 2 3 4 5 : 1 4 3 2 0
# 방문순서는 1부터, 1번노드 1, 4번 노드 2, 3번 노드 3, 2번 노드 4
# depth 는 0부터
visited_depth = [-1]*(N+1)# 방문 할수있는지 없는지 처리
visited_order = [-1]*(N+1)

idx=1
def dfs(start, depth):
    global idx

    visited_depth[start] = depth
    visited_order[start] = idx
    idx+=1
    
    for nxt in graph[start]:
        if visited_depth[nxt] ==-1: 
            dfs(nxt, depth+1)



dfs (R, 0)

sum = 0
for i in range(1, len(visited_order)):
    if visited_depth[i]==-1 :
        continue
    sum+= visited_depth[i]* visited_order[i]



print(sum)