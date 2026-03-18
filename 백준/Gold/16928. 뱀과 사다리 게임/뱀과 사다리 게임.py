import sys
from collections import deque

#1~6
#10x10
#100칸
#1~100까지 수가 적혀있음
#i번 칸 플레이어/ 4가 나오면, i+4칸 100번칸 넘는경우 이동 x
#사다리라면, 사다리를 타고 위로 올라감, 뱀이 있으면, 뱀을 따라서 내려감
# 사다리를 이용해, 이동한 칸의 번호는 원래있던 번호보다 크고, 뱀 이용칸은 원래 칸번호보다 작아진다.
# 1번-> 100칸 도착하는것이 목표


board = [i for i in range (1,101)]

N, M = map(int,sys.stdin.readline().split())

for _ in range(N) :
    x,y = map(int,sys.stdin.readline().split())
    board[x-1] = y


for _ in range (M) :
    u,v = map(int,sys.stdin.readline().split())
    board[u-1] = v


# 1번 시작 : 100번칸 도착을 위해 주사위를 최소 몇 번 굴려야 하는가?

distance = [-1]*(101)

def bfs (start):
    distance[start] = 0
    q = deque ([start])
    while q :
        cur = q.popleft()
        for i in range (1,7):
            nxt= cur +i
            if nxt >100 :
                continue 
            real_nxt = board[nxt-1]
            if 0<real_nxt and real_nxt <=100 :
                if distance[real_nxt] == -1 :
                    distance[real_nxt] = distance[cur] +1
                    q.append(real_nxt)


bfs(1)

print(distance[100])

