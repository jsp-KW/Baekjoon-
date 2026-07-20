def solution(n):
    answer = 0
    
    board = [-1]*(n) # board[row] 해당 행에 놓은 퀸의 열
    
    def dfs (row) :
        nonlocal answer
        
        if row == n :
            answer+=1
            return
        
        for col in range (n) :
            
            possible = True
            
            for prev_queen in range (row) :
                prev_row = prev_queen
                prev_col = board[prev_queen]
                
                if prev_col == col :
                    possible =False
                    break
                
                if prev_row == row :
                    possible = False
                    break
                    
                if abs(prev_row - row) == abs(prev_col -col) :
                    possible = False
                    break
                    
            if possible :
                board[row] = col
                dfs (row+1) 
                board[row] = -1

    dfs(0)

    
    # 퀸은 가로 세로, 대각선 으로 이동이 가능하다
    
    # 같은 행이면 x
    #같은 열이면 x
    #행 차이 == 열 차이 같으면 x
    
    return answer