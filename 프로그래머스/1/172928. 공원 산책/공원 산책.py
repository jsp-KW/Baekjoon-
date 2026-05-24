def solution(park, routes):
    answer = []
    
    length = len(routes) 
    # 길 O , 장애물 X
    
 
    # 시작지점 S
    
    start_y, start_x =0,0
    
    board = []
    
    for p in park :
        temp = []
        for ch in p :
            temp.append(ch)
        board.append(temp)
        
    for i in range (0, len(board)) :
        for j in range (0, len(board[i])):
            if board[i][j] == 'S' :
                start_y, start_x = i,j
                break
                
    # 동 서 남 북
     # 'E' , 'W' ,' S  N
 
    
    row = len(board)
    col = len(board[0])
    cur_y, cur_x = start_y, start_x
    
    for route in routes :
        op = route.split(" ")[0]
        n = int (route.split (" ")[1])
        
        possible = True
        if op == 'E' :
            for check in range (cur_x+1,cur_x +n+1)  : 
                if not (0<= check < col) or board[cur_y][check] == 'X' :
                    possible = False
                    break
            if not possible :
                continue
            else :
                cur_y, cur_x = cur_y, cur_x +n
            
        elif op == 'W' :
            # 0, 1, 2 
            for check in range (cur_x-1,cur_x-n-1,-1) :
                if not (0<= check < col) or board[cur_y][check] == 'X' :
                    possible = False
                    break
                    
            if not possible :
                continue
            else :
                cur_y, cur_x = cur_y, cur_x  -n
                
                    
        elif op =='S':
            
            for check in range (cur_y+1, cur_y+n +1) :
                if not (0<=check < row ) or board[check][cur_x]  == 'X' :
                    possible = False
                    break
            
            if not possible :
                continue
            else :
                cur_y, cur_x = cur_y +n, cur_x
                
        else:
            
            for check in range (cur_y-1, cur_y-n-1, -1):
                if not (0 <= check <row ) or board[check][cur_x]  == 'X':
                    possible = False
                    break
            if not possible :
                continue 
                
            else :
                cur_y, cur_x = cur_y -n, cur_x 

        
    return [cur_y,cur_x]