import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 다익스트라 -> 특정 정점에서 특정 정점까지 도착
# 모든 컴퓨터를 연결하는 최소비용 -> 전체를 하나로 연결 : mst
edges = []
for _ in range (M) :
    a,b,c = map(int,sys.stdin.readline().split())
    edges.append((c,a,b))


edges.sort()

parent = [i for i in range (1+N)]

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union (a,b):
    rootA= find(a)
    rootB = find(b)
    #a -> b- >c : find(a) == find(c) 라, a->c인 간선 추가 못함.
    # mst n-1개 간선만 사용

    if rootA == rootB :# 사이클 판단 로직 분기문
        return False
    
    if rootA < rootB :
        parent[rootB]= rootA
    else:
        parent[rootA] = rootB
    return True
answer =0
cnt = 0

for cost, a, b in edges :
    if union(a,b) :
        answer+=cost
        cnt +=1
        if cnt == N -1 :
            break

    
print(answer)