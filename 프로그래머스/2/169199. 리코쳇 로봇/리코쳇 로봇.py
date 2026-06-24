from collections import deque

def solution(board):
    answer = 0
    
    row = len(board)
    col = len(board[0])
    
    maps = []
    
    for r in board:
        maps.append(r)
    
    visited= [[-1]*(col) for _ in range (row)]
    
    dy = [-1,1,0,0]
    dx=  [0,0,-1,1]
    
    def bfs (start) :
        y,x = start
        q = deque ([start])
        visited[y][x] =0
        while q :
            cur_y, cur_x = q.popleft()
            
            if maps[cur_y][cur_x] == 'G' :
                return visited[cur_y][cur_x]
            
            for i in range (4) :
                stop_y, stop_x = cur_y, cur_x # stop 멈추는 지점
                
                # next는 다음에 방문할 지점 계산
                # 방문할 지점이 장애물 or  범위 밖
                # break
                # 방문 못하므로 탈출하고, 이전 지점 stop 에서 visited 값 계산
                while True : 
                    next_y = stop_y +dy[i]
                    next_x = stop_x +dx[i]
                    
                    if 0>next_y or next_y >=row  or next_x <0 or next_x >=col :
                        break
                        
                    if maps[next_y][next_x] == 'D' :
                        break
                        
                    stop_y = next_y
                    stop_x = next_x
                
                if visited[stop_y][stop_x] == -1 :
                    visited[stop_y][stop_x] = visited[cur_y][cur_x] +1 # 미끄러지는건 계산 안하므로, 처음 꺼낸 좌표값에서 +1
                    q.append ((stop_y, stop_x))

    # 시작지점 
    for i in range (0, row) :
        for j in range (0,col):
            if visited[i][j] ==-1 and maps[i][j] == 'R':
                answer = bfs((i,j))
    
    if not answer :
        return -1
    else :
        return answer
  