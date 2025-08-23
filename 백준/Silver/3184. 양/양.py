import sys
from collections import deque

# 영역: 한칸 수평 수직만 이동, 울타리를 지나지 않고 다른 칸 이동 가능시, 두칸의 같은 영역안에 있다고 함
# 양> 늑대수 (같은 영역)  이기고, 아니면 늑대가  다먹음
# 아침이 되었을때, 살아남은 양과 늑대의 수를 출력


# . : 빈필드 , # : 울타리 , o: 양, v : 늑대

R,C = map(int,sys.stdin.readline().split())

farm = [[]*(C) for _ in range (R)]

for i in range (0, R) :
    line = sys.stdin.readline().strip()
    farm[i]+=line

# 상하좌우
move_x = [0,0,-1,1]
move_y = [1,-1,0,0]
visited = [[False]*C for _ in range (R)]


def bfs (dy,dx) :
    q = deque([(dy,dx)])
    visited[dy][dx] = True

    sheep = 1 if farm[dy][dx] =='o' else 0
    wolf = 1 if farm[dy][dx] == 'v' else 0
    escapable = (dy == 0 or dy == R-1 or dx == 0 or dx == C-1)
    while q:
        y,x = q.popleft()
        for k in range(4) :
            ny,nx = y +move_y[k] , x +move_x[k]
            if 0<=ny<R  and 0<= nx <C  and not visited[ny][nx] and farm[ny][nx] != '#' :
                visited[ny][nx] = True

                if ny == 0 or ny == R-1 or nx == 0 or nx == C-1:
                    escapable = True
                cell = farm[ny][nx]
                if cell == 'o' : sheep +=1
                elif cell == 'v' : wolf +=1
                q.append((ny,nx))
    if escapable:
        return 0, 0
    
    return (sheep, 0) if sheep > wolf else (0, wolf)
    


total_w, total_s = 0,0
for i in range (0,R) :
    for j in range (0,C) :
        if not visited[i][j]  and farm [i][j] != '#' :
            s,w = bfs(i,j)
            total_s += s
            total_w  +=w

print(total_s,total_w)
