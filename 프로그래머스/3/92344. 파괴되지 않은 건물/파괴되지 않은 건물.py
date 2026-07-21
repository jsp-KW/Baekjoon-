def solution(board, skill):
    answer = 0
    
    # 시작점에 +5 종료점 다음점에 -를 해주면, 누적합 계산이 가능함
    
    # type ==1 공격 : 내구도 낮춤
    # type == 2 회복 : 내구도 높임
    
    # type, r1,c1,r2,c2, degree
    
    # board[start] += degree
    # board[end+1] += -degree
    
    
    # r1,c1  +degree
    # r1 c2  -degree
    # r2 c1 -degree
    # r2 c2 +degree
    
    # type ==1 인 경우 반대로
    
    row = len(board)
    col = len(board[0]) 
    
    temp = [[0] *(col+1) for _ in range(row +1) ]
  
    
    for s in skill :
        r1,c1,r2,c2, degree = s[1],s[2],s[3],s[4],s[5]
        if s[0] == 1 : #공격
            temp[r1][c1] -= degree 
            temp[r1][c2+1] += degree
            temp[r2+1][c1] += degree
            temp[r2+1][c2+1] -= degree 
            
        else : #회복
            temp[r1][c1] += degree
            temp[r1][c2+1] -= degree
            temp[r2+1][c1] -= degree
            temp[r2+1][c2+1] +=degree
    
    
    for i in range (row +1) :
        for j in range (1,col+1) :
            temp[i][j] += temp[i][j-1]
            
    for j in range (col+1) :
        for i in range (1, row+1) :
            temp[i][j] += temp[i-1][j] 
            
    
    
    for i in range (0, row) :
        for j in range(0, col) :
            if board[i][j] + temp[i][j] >=1 :
                answer+=1
            
        
    return answer