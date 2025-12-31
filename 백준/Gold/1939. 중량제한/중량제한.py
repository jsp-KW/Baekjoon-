import sys
from collections import deque

N, M  = map(int,sys.stdin.readline().split())

#한번의 이동으로 옮길 수 있는 물품들의 중량의 최대값
# N 개의 섬,
# A <-> B 번 중량제한이 C인 다리가 존재한다

bridges = [[] for _ in range (N+1)]


max_weight = 0


for _ in range (M) :
    A,B,C = map(int,sys.stdin.readline().split())
    bridges[A].append ((B,C))
    bridges[B].append ((A,C))
    
    if C> max_weight :
        max_weight  = C


start, end = map (int,sys.stdin.readline().split())

def bfs (weight):
    visited =[False]*(N+1)

    q = deque([start])
    visited[start] = True

    while q :
        cur  = q.popleft()

        if cur == end :
            return True
        
        for next, cur_weight in bridges [cur] :
            if not visited[next] and cur_weight >= weight :
                visited[next]= True
                q.append(next)

    return False


low, high = 1, max_weight

while low <= high :
    mid = (low + high) //2 

    if bfs(mid) :
        answer = mid
        low = mid+1 
    else :
        high = mid -1


print (answer)
    

 

