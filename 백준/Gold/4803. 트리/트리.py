import sys
sys.setrecursionlimit(2000)

def find(parent, x) :

    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]
    

def union (a,b,parent,is_cycle) :
    rootA = find(parent, a)
    rootB = find(parent, b)

    # cycle check 

    if rootA == rootB :
        is_cycle[rootA] = True
        return
    
    if is_cycle[rootA] or is_cycle[rootB] :
        is_cycle[rootA] = True
        is_cycle[rootB] = True
        
    if rootA < rootB :
        parent[rootB] = rootA
    else :
        parent[rootA]= rootB 

case =1
while True:
    
    n,m = map(int,sys.stdin.readline().split())
    if n ==0 and m == 0  : break
    parent = [i for i in range (n+1)]
    is_cycle = [False]*(n+1)

    graph = [[] for _ in range (1+n)]
    for _ in range (m) :
        u,v = map(int,sys.stdin.readline().split())
        union(u,v,parent,is_cycle)

    cnt = 0

    for i in range (1,n+1) :
        if parent[i] == i and not is_cycle[i] :
            cnt +=1

    if cnt ==0 :
        print(f"Case {case}: No trees.")
    elif cnt >1 :
        print(f"Case {case}: A forest of {cnt} trees.")
    elif cnt == 1:
        print(f"Case {case}: There is one tree.")
    
    case +=1
    


