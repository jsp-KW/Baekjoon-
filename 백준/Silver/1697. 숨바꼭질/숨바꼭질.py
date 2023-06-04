import sys
from collections import deque

a,b = map (int, sys.stdin.readline().split())


map = [0]  * 100001

q= deque()
q.append(a)

while q :

    k = q.popleft()

    if  k ==b :
        print (map [b])
        break


    for i in (k-1,k+1,k*2) :
        if 0<=i <=100000 and map [i] ==0 :
            map [i] = map[k] +1
            q.append(i)
        