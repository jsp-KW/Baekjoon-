import sys
from collections import deque


N,M = map(int,sys.stdin.readline().split())

dy = [-1,1,0,0]
dx =[0,0,-1,1]

# 벽 한개까지만 뿌실수있음 ->뿌셔서 이동하는것이 짧아지면 가능

# 1,1 -> N,M
# 0,0 -> N-1,M-1 칸 까지의 최단경로를 구하자
# 최단 거리를 구하면됨
board = [[] for _ in range (N)]
for i in range (N) :
    temp = list(map(int,sys.stdin.readline().rstrip ()))
    board[i].extend(temp)

def bfs (start) :
    
    dist = [[[-1]*(2) for _ in range(M)]for _ in range (N)]
    is_broken = 0
    y,x = start
    dist[y][x][0] = 1
    q = deque ([(y,x,is_broken)])

    while q :
        cur_y,cur_x,is_broken= q.popleft()

        if cur_y== N-1 and cur_x==M-1:
            return dist[N-1][M-1][is_broken]
      
        for i in range (4) :
            my,mx = cur_y +dy[i] , cur_x + dx[i]
            

            if 0<= my<N and 0<= mx <M :
                if board[my][mx] == 1 : # 벽
                    if  is_broken == 0 and dist[my][mx][1] == -1 : # 뿌순적이 없으면
                        dist[my][mx][1] = dist[cur_y][cur_x][0] +1 
                        q.append((my,mx,1))
                    else :
                        continue 

                elif board[my][mx] == 0 : #길
                    if dist[my][mx][is_broken] == -1 :

                        dist[my][mx][is_broken] = dist[cur_y][cur_x][is_broken] +1
                        q.append((my,mx,is_broken)) 

    return -1
result = bfs ((0,0))

print (result )