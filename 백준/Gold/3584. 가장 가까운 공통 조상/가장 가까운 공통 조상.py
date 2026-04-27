import sys

T = int(sys.stdin.readline())

answers= []

for _ in range (T):
    N = int(sys.stdin.readline())


    parent=  [0]*(N+1)
    for _ in range (N-1) :
        node1, node2 = map(int,sys.stdin.readline().split()) # node1이 node2 의 부모라는 뜻
        parent[node2] = node1

    target1, target2 = map(int,sys.stdin.readline().split())
    
    candidates = set()
    cur = target1
    while cur!= 0 :
        candidates.add(cur)
        cur = parent[cur]

    cur = target2 

    while True :
        if cur in candidates :
            answers.append(cur)
            break
        
        cur = parent[cur]
    
for ans in answers :
    print(ans)