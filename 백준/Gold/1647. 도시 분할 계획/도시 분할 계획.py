import sys

# n개의 집과 m 개의 길로 이루어져 있다.# 유지비가 있대,
# 마을의 이장은 두 개의 분리된 마을로 분할
# 마을에는 집이 하나 있어야하고, 분리된 마을 안에 있는 임의의 두집 사이에는 경로 존재
# 분리된 마을안에서도 임의의 두 집 사이의 경로가 항상 존재하게 하면서 길을 더 없앨 수 잇다
#  유지비의 합을 최소로 하고싶다


N, M = map(int,sys.stdin.readline().split())

edges = []

for _ in range (M) :
    country1, country2 , cost =map(int,sys.stdin.readline().split())
    edges.append ((cost,country1, country2))

edges.sort()

# 서로 연결된 집 사이, 또 길을 넣는 것은 낭비
# 가장 싼 길을 꺼내서, 두집이 같은 마을인지 확인, -> 이미 같은 마을이라면, 무시
# 서로 다른 마을 이라면, 길을 합친다

#  가중치 없는 최단 거리 -> BFS
#  가중치 있는 최단거리 다익스트라
#  모든 노드를 잇는 최소 총합 비용 , 공사비 아끼자.
parent = [ i for i in range (N+1)]


def find (parent,x) :
    if parent[x] != x :
        parent[x] = find(parent,parent[x])
    return parent[x]

def union (parent, a,b) :
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA < rootB :
        parent[rootB] = rootA  # 번호가 작으니,큰놈의 부모가 작은놈
    else:
        parent[rootA] = rootB

answer = 0
last_edge_cost = 0 # 가장 비싼 길 저장
for edge in edges :
    c ,target_a, target_b = edge 
    if find(parent,target_a) == find(parent,target_b) :
        continue
    union(parent, target_a, target_b)
    answer+=c
    last_edge_cost = c





print(answer-last_edge_cost)

    