from collections import deque
def solution(game_board, table):
    answer = 0
    game_row = len(game_board)
    game_col = len(game_board[0])
    visited_board =[[False]*(game_col) for _ in range (game_row)]
    visited_table = [[False]*(game_col) for _ in range (game_row)]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    blanks = []
    get_shape = []
    
             
    def bfs_board (start) :
        board_cordinates = []
        y,x = start
        visited_board [y][x] = True
        board_cordinates.append((y,x))
        q= deque([start])

        while q :
            cur_y,cur_x = q.popleft()
            for i in range (4) :
                my,mx = cur_y +dy[i], cur_x +dx[i]
                if 0<= my < game_row and 0<= mx < game_col :
                    if game_board[my][mx] == 0 and not visited_board[my][mx]:
                        visited_board[my][mx] = True
                        board_cordinates.append((my,mx))
                        q.append((my,mx))
        return board_cordinates

    def bfs_table (start) :
        y,x = start
        visited_table [y][x] = True
        table_cordinates = []
        table_cordinates.append((y,x))

        q= deque([start])

        while q :
            cur_y,cur_x = q.popleft()
            for i in range (4) :
                my,mx = cur_y +dy[i], cur_x +dx[i]
                if 0<= my < game_row and 0<= mx < game_col :
                    if table[my][mx] == 1 and not visited_table[my][mx]:
                        visited_table[my][mx] = True
                        table_cordinates.append((my,mx))
                        q.append((my,mx))
        return table_cordinates

    for i in range (0, game_row) :
        for j in range (0, game_col) :
            if game_board[i][j] ==0 and not visited_board[i][j] :
                    blanks.append(bfs_board((i,j)))
                    
    for i in range (0, game_row) :
        for j in range (0, game_col) :
            if table[i][j] ==1 and not visited_table[i][j]:
                get_shape.append(bfs_table((i,j)))
    # blanks => 보드판에 남은 공간 좌표들
    # get_shape => table에서 쓸수 있는 도형 좌표들
    
    # normalize 좌표 정규화
    
    def normalize (target) :
        min_y ,min_x = float('inf'),float('inf')
        
        for y,x in  target :
            if y < min_y :
                min_y = y
            if x< min_x :
                min_x = x
                
        normalize_res= []
        for y,x in target :
            normalize_res.append((y-min_y, x-min_x))
        normalize_res.sort()
        
        return tuple(normalize_res)
    
    blanks_norm = [normalize(block) for block in blanks]
    shapes_norm = [normalize(s) for s in get_shape]
    
    def rotate (shape) :
        rotated = [(x,-y) for y,x in shape] # 회전시, y,x -> x,-y ->-y,-x -> -x,y
        return normalize(rotated)
    
    used_shapes = [False]*len(shapes_norm)
    for target_blank in blanks_norm :
        found = False
        
        for i, shape in enumerate(shapes_norm) :
            if used_shapes[i] :
                continue
            
            rotated_shape = shape
            
            for _ in range (4) :
                if target_blank == rotated_shape :
                    answer+= len(target_blank)
                    found = True
                    used_shapes[i] = True
                    break
                rotated_shape = rotate(rotated_shape)
            if found : break
           
                
    
        
    return answer