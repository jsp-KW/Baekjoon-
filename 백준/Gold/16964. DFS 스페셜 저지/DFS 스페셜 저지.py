import sys
N = int(sys.stdin.readline())

graph = [[] for _ in range (N+1)]

for _ in range (N-1) :
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


visit_order = list(map(int,sys.stdin.readline().split()))

order_standard = [0] *(N+1)
for idx, value in enumerate(visit_order) :
    order_standard[value] = idx
 


for i in range (1,N+1 ):
    graph[i].sort(key = lambda x : order_standard[x])


# dfs (1) 부터 호출
visited =  [False]*( N+1 )

number = 0

if visit_order[0] != 1 :
    print(0)
    sys.exit()

stack  = [1]
res = []

while stack :
    v= stack.pop()
    if visited[v] :
        continue

    visited[v] = True
    res.append(v)

    for nxt in reversed(graph[v]):
        if not visited[nxt] :
            stack.append(nxt)
    



print (1 if res == visit_order else 0 )