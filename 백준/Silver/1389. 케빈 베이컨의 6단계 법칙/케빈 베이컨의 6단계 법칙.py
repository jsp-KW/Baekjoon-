import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())

# 1->3 1->4 2->3 ,3->4 , 4->5


friends = [ []for _ in range (N+1)]

for _ in range (M) :
    p1,p2 = map(int,sys.stdin.readline().split())
    friends[p1].append(p2)
    friends[p2].append(p1)



def bfs (start_person) :
    dist = [-1]*(N+1)
    dist[start_person] = 0

    q = deque ([start_person]) 
    while q :
        cur = q.popleft()
        
        for nxt in friends[cur] :
            if dist[nxt] == -1  :
                dist[nxt] = dist[cur] +1
                q.append(nxt)
    
    return sum(dist)+1


answer = []
for i in range (1,N+1) : # 1번부터 N번까지
   
    result = bfs (i)
    answer.append((i,result))

answer.sort(key = lambda x : (x[1]))
print(answer[0][0])