import sys

N,M = map(int,sys.stdin.readline().split())

parent =  [i for i in range(N+1)]

def find(x) :
    # if parent[x] != x: # 위에 연결된 부모 노드가 존재하면
    #     parent[x] =  find(parent[x]) # 6 4 3 2 면 바로 2로 압축시키는 
    # return parent[x]
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a,b):
    get_a = find(a)
    get_b = find(b)

    if get_a < get_b :
        parent[get_b] = get_a
    else :
        parent[get_a] = get_b



for _ in range(M):
    operation, a,b =  map(int, sys.stdin.readline().split())

    if operation ==0 :
        union(a,b)
    else :
        print("YES" if find(a) == find(b) else "NO")