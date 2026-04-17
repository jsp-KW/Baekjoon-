import sys
from collections import deque


n = int(sys.stdin.readline())

tree =  [[] for _ in range (n+1)]

if n == 1 :
    print(0)
    exit()


for _ in range (n-1) :
    u,v, cost = map(int,sys.stdin.readline().split())
    tree[u].append((v,cost))
    tree[v].append((u,cost))


def bfs (start) :
    distance = [-1]*(n+1)

    q = deque([(start,0)])
    distance [start] = 0
    farthest_node = start
    max_distance = 0

    while q :
        cur_node, cur_cost = q.popleft()

        for nxt_node, nxt_cost in tree[cur_node] :
            if distance[nxt_node] == -1 :
                distance[nxt_node] = nxt_cost + distance[cur_node]
                q.append((nxt_node, distance[nxt_node]))
                if distance[nxt_node] > max_distance :
                    max_distance = distance[nxt_node]
                    farthest_node = nxt_node
    return farthest_node, max_distance


node_A,_ = bfs(1)

_, result_distance = bfs(node_A)


print(result_distance)