import sys
from collections import deque

row,col = map(int,sys.stdin.readline().split())


maps = [[] for _ in range(row)]

for i in range(row):
    lines = map(str,sys.stdin.readline().split())
    maps[i] +=lines

visited= [[False]* (col) for _ in range(row)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]
picture=0
def bfs(start):

    que = deque([start])
    visited[start[0]][start[1]]= True
    
    picture =1
    
    while que :
        cur_y,cur_x = que.popleft()

        for i in range(4):
            move_y,move_x= cur_y+dy[i],cur_x+dx[i]

            if 0<=move_y<row and 0<=move_x<col:
                if maps[move_y][move_x]=='1' and not visited[move_y][move_x]:
                    picture+=1
                    visited[move_y][move_x]=True
                    que.append((move_y,move_x))

      

    return picture

all_result =[]
for i in range(row):
    for j in range(col):
        if not visited[i][j] and maps[i][j]=='1':
            result = bfs((i,j))
            all_result.append(result)

print(len(all_result))
print(max(all_result) if len(all_result)>0 else 0)

