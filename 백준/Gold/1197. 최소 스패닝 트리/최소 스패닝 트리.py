import sys
import heapq 
sys.setrecursionlimit(100000)
# mst

V, E = map(int,sys.stdin.readline().split())
# 가중치의 합이 최소인 트리


edges = []

for _ in range (E) :
    A,B,C = map(int,sys.stdin.readline().split())
    heapq.heappush(edges, (C,A,B))

parents = [i for i in range (V+1)]

def find (parent, x) :
    if parent[x] != x :
        parent[x] = find (parent, parent[x])
    return parent[x]

def union(parent, a, b) :
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB :
        parent[rootB] = rootA
    else :
        parent[rootA]= rootB

count = 0 
#V-1 == count 면 break
sum_val = 0

while edges :

    if count == V-1 :
        break
    
    cost, start, end = heapq.heappop(edges)

    if find(parents,start) != find(parents,end) :
        union(parents,start,end)
        count +=1
        sum_val += cost
   

print(sum_val)