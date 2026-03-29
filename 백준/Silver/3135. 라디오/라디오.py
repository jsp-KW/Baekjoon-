import sys
from collections import deque

A,B = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())

jumps = []
for _ in range (n) :
    temp = int(sys.stdin.readline())
    jumps.append(temp)


jumps.sort(reverse=True)

rest = abs(B-A)

if rest ==0 :
    print(0)
    sys.exit()


distance = [-1]*(1000)

q= deque([A])
distance[A] = 0

while q :
    cur = q.popleft()

    if cur == B :
        break

    for basic_move in [-1,1] :
        basic=  cur +basic_move 
        if 0<= basic <1000 :
            if distance[basic] == -1 :
                distance[basic]= distance[cur] +1 
                q.append(basic)

    for nxt in jumps :
    
        if 0<= nxt < 1000 :
            if distance[nxt] == -1 :
                distance[nxt] =1 
                q.append(nxt)
            

print (distance[B])
