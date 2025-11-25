import sys
from collections import deque
# 양 #, . 풀
# 서로다른 # 두개이상 붙어있으면 한무리의 양
# 몇개의 양무리가 있엇는지


T = int (sys.stdin.readline())

dy = [1,-1,0,0]
dx = [0,0,-1,1]
result = []

def bfs(node) :
    y,x = node
    visited[y][x] = True
    q = deque([node])

    while q :
        cur_y, cur_x = q.popleft()

        for i in range (4) :
            move_y, move_x = cur_y+ dy[i] , cur_x + dx[i]

            if 0<=move_y<H and 0<=move_x <W :
                if grid[move_y][move_x] == '#' and not visited[move_y][move_x] :
                    visited[move_y][move_x] = True
                    q.append((move_y,move_x))

        

for _ in range (T) :
  
    answer =0
    H,W = map(int, sys.stdin.readline().split())
    grid = []

    for i in range (H) :
        grid.append(list(map(str, sys.stdin.readline().rstrip())))
       

    visited = [[False]*(W) for _ in range (H)]
    
    for i in range (H) :
        for j in range (W) :
            if grid[i][j] == '#' and not visited[i][j]  :
                answer +=1
                bfs((i,j))

    result.append(answer)

for r in result :
    print (r)