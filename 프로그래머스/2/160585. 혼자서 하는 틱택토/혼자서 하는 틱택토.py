def solution(board):
    answer = -1
    
    # 규칙을 지켜서 나올 수 있는 결과면 1 / 아니라면 0
    
    # 선공 후공 번갈아서
    
    # 선공이 먼저
    
    #'O'
    
    # 후공이 먼저
    # 'X'
    
    
    o_cordinates = []
    x_cordinates = []
    row = len(board)
    col = len(board[0])
    
    for i in range (0,row):
        for j in range(0,col) :
            if board[i][j] =='O':
                o_cordinates.append((i,j))
            if board[i][j] =='X' :
                x_cordinates.append((i,j))
                
    o_count = len(o_cordinates)
    x_count = len(x_cordinates)
    
    # 선공이 O
    
    # oxo
    # o
    if x_count > o_count :
        return 0
    
    if o_count > x_count +1 :
        return 0
    
    def check_win(coord) :
        
        coordinates = set(coord)
        for i in range (3) :
            if (i,0) in coordinates and (i,1) in coordinates and (i,2) in coordinates :
                return True
            
        
        for j in range (3) :
            if (0,j) in coordinates and (1,j) in coordinates and (2,j) in coordinates :
                return True
            
        
        if (0,0) in coordinates and (1,1) in coordinates and  (2,2) in coordinates :
            return True
        
        if (0,2) in coordinates and (1,1) in coordinates and (2,0) in coordinates :
            return True
    
        return False

    o_win = check_win(o_cordinates)
    x_win = check_win(x_cordinates)
    
    if o_win and x_win :
        return 0
    if not o_win and not x_win :
        return 1
    

    if o_win and not x_win :
        if o_count == x_count +1 :
            return 1
        else:
            return 0
        
    if x_win and not o_win:
        if o_count == x_count:
            return 1
        else:
            return 0
            


    
    return answer