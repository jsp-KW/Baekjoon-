import sys
from collections import deque

row,col,garbage_cnt= map(int,sys.stdin.readline().split())

maps= [[0]*(col) for _ in range(row)] #왼쪽상단이 0,0, col개 열을 가진 배열을 row개 선언한 이중리스트

for _ in range(garbage_cnt):
    r,c= map(int,sys.stdin.readline().split())
    maps[r-1][c-1] = '#' #쓰레기 위치 저장

visited =[[False]*(col) for _ in range(row)] #방문처리할 리스트도 map과 같은 크기로

move_x =[0,0,-1,1] #상하좌우 이동시 변경되는 x좌표
move_y =[1,-1,0,0] #상하좌우 이동시 변경되는 y좌표



def bfs(start) :
    big_size= 0

    y= start[0]
    x= start[1]

    visited[y][x]=True   #인자로 들어온좌표 i,j= start[0],start[1]인데, 여기서 i가 행이고 y좌표,
    que = deque() #queue선언
    que.append((y,x))# queue에 삽입
    garbages = 1# 해당좌표도 쓰레기 개수 1개로 초기화, bfs호출시 쓰레기 존재하는 위치에서만 호출할것이므로
    while que :
    
        cur= que.popleft() # 큐에서 꺼내오고,
    
        for i in range (4) : #현재 좌표에서 상하좌우 방향으로 쓰레기가 인접했다면
            dy,dx = cur[0]+move_y[i], cur[1]+move_x[i]
            if 0<=dx<col  and 0<=dy<row :
                if visited[dy][dx] != True and maps[dy][dx] =='#':
                    garbages +=1 #쓰레기 크기 증가
                    visited[dy][dx]= True # 그 방향은 쓰레기 합쳤으니 방문처리
                    que.append((dy,dx)) # 큐에 좌표 다시삽입
                    
                    
        big_size= max(big_size,garbages) # 상하좌우를 다 살피고 난 후, 최종적인 쓰레기 크기 비교후 return
        
    return big_size
return_bfs = 0 
for i in range(0,row):
    for j in range(0,col):
        if visited[i][j] !=True and maps[i][j] =='#' : # 쓰레기 있는곳만 방문해서 처리하기
           
            return_bfs = max(return_bfs,bfs((i,j))) # 해당좌표에서 나온 최대 크기 vs 이전의 쓰레기 크기 중 최대값 return


print(return_bfs) #최종적으로 답은 최대 크기