import sys

n,m = map(int,sys.stdin.readline().split())

parent = [i for i in range (n+1)]

answers= []


def find(parent, x) :


    #x의 부모의 값을 할아버지 값으로 대체해서 올라간다
    while parent[x] != x :
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x



def union (parent, A,B) :
    rootA = find(parent,A)
    rootB = find(parent,B)

    if rootA < rootB :
        parent[rootB] = rootA
    elif rootA == rootB :
        return False
    
    else :
        parent[rootA] = rootB

    return True


for _ in range (m) :
    op,a,b = map(int,sys.stdin.readline().split())
    if op == 0 :
        union (parent, a,b) 
    elif op ==1 :
        if find(parent,a) == find (parent,b) :
            answers.append("YES")
        else:
            answers.append("NO")

    
for ans in answers :
    print(ans)



