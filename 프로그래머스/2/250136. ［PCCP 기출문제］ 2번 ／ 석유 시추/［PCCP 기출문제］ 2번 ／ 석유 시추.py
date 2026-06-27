from collections import deque
def solution(land):
    answer = 0
    

    dic = dict()
    
    
    
    row = len(land)
    col = len(land[0])
    
    visited = [[-1]*(col) for _ in range (row)]

        
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    land_num =1
    def bfs (start, land_num) :
        cnt =1
        y,x = start
        visited[y][x] = land_num
        q = deque([start])
        
        while q :
            cur_y, cur_x = q.popleft()
            for i in range (4) :
                my,mx = cur_y + dy[i], cur_x +dx[i]
                if 0<= my <row and 0<= mx <col :
                    if visited[my][mx] == -1 and land[my][mx] == 1 :
                        visited[my][mx] = land_num
                        q.append((my, mx))
                        cnt+=1
                        
        return (land_num, cnt)
    
    
    for i in range (row) :
        for j in range (col) :
            if land[i][j] == 1 and visited[i][j] == -1:
                get_num, get_cnt = bfs((i,j), land_num)
                dic[get_num] = get_cnt
                land_num +=1
    
    

    answer = -1 
    
    for i in range (col) :
        res_set = set()
        for r in range (row) :
            if visited[r][i] != -1 :
                res_set.add (visited[r][i])
        
        total_oil = 0
        for num in res_set :
            total_oil += dic[num]
            
        answer = max(answer, total_oil)
    
        
    
    return answer