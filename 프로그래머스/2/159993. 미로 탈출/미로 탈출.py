from collections import deque

def solution(maps):
    answer = 0
    
    row = len(maps)
    col = len(maps[0])
    
    graph = []
    
    for m in maps :
        temp = []
        for i in range (0, len(m)) :
            temp.append(m[i])
        graph.append(temp)
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    def bfs (start, target) :
        
        distance = [[-1] *(col) for _ in range(row)]
        y,x = start 
        distance[y][x] = 0
        q = deque([start])
        while q :
            cur_y, cur_x = q.popleft()
            
            if cur_y == target[0] and cur_x == target[1] :
                return distance[cur_y][cur_x]
            
            for i in range(4) :
                my, mx = cur_y + dy[i] , cur_x +dx[i]
                
                if 0<= my< row and 0<= mx <col :
                    if distance[my][mx] ==-1 and graph[my][mx] != 'X' :
                        distance[my][mx] = distance[cur_y][cur_x] +1
                        q.append((my,mx))
        return -1
    
    
    start_y, start_x = 0,0
    lever_y, lever_x = 0,0
    end_y, end_x =0,0
    for i in range (row) :
        for j in range (col) :
            if maps[i][j] =='S' :
                start_y, start_x = i,j
                
            if maps[i][j] == 'L' :
                lever_y, lever_x = i, j
            
            if maps[i][j] == 'E' :
                end_y, end_x = i, j
                
            
                
    bfs_res = bfs((start_y, start_x), (lever_y, lever_x))
    
    if bfs_res == -1 :
        return -1
    else :
        
        bfs_res2 = bfs((lever_y, lever_x), (end_y, end_x))
        
        if bfs_res2 == -1 :
            return -1
        else :
            return bfs_res + bfs_res2
    
    return answer
 

 