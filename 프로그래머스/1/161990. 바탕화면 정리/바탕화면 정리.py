def solution(wallpaper):
    answer = []
    # 거리 = 절대값 x차 + 절대값 y차
    
    board =[] 
    
    for arr in wallpaper :
        temp = []
        for a in arr:
            temp.append(a)
            
        board.append(temp)
        
    cordinates = []
    for i in range  (0, len (board)) :
        for j in range (0, len(board[i])) :
            if board[i][j] == '#' :
                cordinates .append ((i,j,i+1,j+1))
    
    start_y, start_x , end_y, end_x = cordinates[0][0],cordinates[0][1],cordinates[0][2],cordinates[0][3]
    for i in range (1, len(cordinates)) :
        start_y = min(start_y, cordinates[i][0])
        start_x = min(start_x, cordinates[i][1])
        end_y = max(end_y, cordinates[i][2])
        end_x = max(end_x, cordinates[i][3])
    
    
    return [start_y, start_x, end_y, end_x]