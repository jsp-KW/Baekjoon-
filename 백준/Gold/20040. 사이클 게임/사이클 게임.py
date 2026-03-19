import sys

# 0~n-1 까지 고유한 번호 부여, n개
#
n, m= map(int,sys.stdin.readline().split())
cnt = 0
edges = []
for _ in range (m) :
    p1,p2 = map(int,sys.stdin.readline().split())
    edges.append((p1,p2))

parent = [i for i in range (0,n)]

def find (x) :
    if x!= parent[x] :
        parent[x] = find(parent[x])
    return parent[x]

def union (A,B) :
    rootA = find(A)
    rootB = find(B)

    if rootA == rootB :
        return False

    else :
        if rootA < rootB :
            parent[rootB] = rootA 
        else :
            parent[rootA] = rootB
    return True

is_cycle = False
for u,v in edges :
    if not union(u,v) :
        is_cycle = True
        print(cnt+1)
        sys.exit(0)
    else:
        cnt +=1

if not is_cycle :
    print(0)
