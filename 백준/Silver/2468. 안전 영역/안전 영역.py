import sys
from collections import deque

N = int(sys.stdin.readline())


origin_map = []
visited= [[False] *(N) for _ in range (N)]

dx = [0,0,-1,1]
dy= [-1,1,0,0]

answers = []


def bfs (start, threshold) :

    y,x = start
    visited [y][x] = True
    q = deque([start])

    while q :
        cur_y, cur_x = q.popleft()
        for i in range (4) :
            move_y, move_x = cur_y+dy[i] , cur_x +dx[i]

            if 0<= move_y <N  and 0 <= move_x <N :
                if not visited[move_y][move_x]  and origin_map[move_y][move_x] > threshold :
                    visited[move_y][move_x] = True
                    q.append((move_y, move_x))
    return True
 
for i in range (N) :
    origin_map.append(list(map(int,sys.stdin.readline().split())))



max_height = max (map(max, origin_map))
for case in range (0,max_height+1):
    visited= [[False] *(N) for _ in range (N)]
    safe_ground = 0
    for i in range (N) :
        for j in range (N) :
            if not visited[i][j]  and origin_map[i][j] > case :
                if (bfs((i,j), case)) : safe_ground +=1
               

    answers.append(safe_ground)

print (max(answers))

