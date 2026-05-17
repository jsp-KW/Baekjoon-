from collections import deque

def solution(maps):
    answer = 0
    # 벽 못감, 통로 ㅇ
    # 통로중 미로 빠져가는 문 -> 레버
    #한칸 이동 1초 최대한 빠르게
    
    graph = []
  
    row = len(maps)
    col = len(maps[0])


    for m in maps :
        temp =[]
        for i in range (0, col) :
            temp.append(m[i])
        graph.append(temp)
        
    dy =[-1,1,0,0]
    dx =[0,0,-1,1]

    def bfs (start, target) :
        distance = [[-1]*(col) for _ in range (row)]
        y,x = start
        distance[y][x] = 0
        q = deque([start])
        
        while q :
            cur_y, cur_x = q.popleft()
            
            if graph[cur_y][cur_x] == target :
                return distance[cur_y][cur_x]
            for i in range (4) :
                move_y,move_x = cur_y+dy[i], cur_x +dx[i]
                if 0<= move_y<row and 0<= move_x <col :
                    if distance[move_y][move_x] == -1 and graph[move_y][move_x]!='X' :
                        distance[move_y][move_x] =distance[cur_y][cur_x] +1
                        q.append((move_y,move_x))
        return -1
        
        
    
    start_y,start_x = 0,0 
    lever_y, lever_x = 0,0
    for i in range (row) :
        for j in range (col) :
            if graph[i][j] =='S':
                start_y, start_x =i,j
            if graph[i][j] =='L' :
                lever_y,lever_x = i,j

                
    res =bfs ((start_y, start_x), 'L')
    if res == -1 :
        return -1
    
    else :
        res2 = bfs((lever_y, lever_x), 'E')
        if res2 != -1 : 
            return res +res2
        else :
            return -1

 