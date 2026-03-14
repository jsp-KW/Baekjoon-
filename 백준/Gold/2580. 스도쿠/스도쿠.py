import sys

board = [[]for _ in range (9)]

for i in range (9) :
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)

fill_targets= []

for i in range (9) :
    for j in range (9) :
        if board[i][j] == 0 :
            fill_targets.append((i,j))


def get_final_candidates (y,x) :
    end_y, end_x =0,0

    if 0<= y<3 :
        if 0<=x<3 :
            end_y =3
            end_x = 3
            
            
        elif 3<=x<6 :
            end_y =3
            end_x = 6
        
        else:
            end_y = 3
            end_x = 9

    
    elif 3<=y<6 :
        if 0<=x<3 :
            end_y = 6
            end_x = 3

            
        elif 3<=x<6 :
            
            end_y = 6
            end_x = 6
        
        else:
            
            end_y = 6
            end_x = 9

    else :
        if 0<=x<3 :
            end_y = 9
            end_x = 3
            
        elif 3<=x<6 :
            end_y = 9
            end_x = 6
        
        else:
            end_y = 9
            end_x = 9

    num_used = [False] *(10)
    # 3x3 사이즈에서 안쓴 숫자 체크 -> num_used로 기록
    for i in range (end_y-3,end_y) :
        for j in range (end_x-3,end_x) :
            if board[i][j] ==0 :
                continue
            num_used[board[i][j]] = True

    candidates = [] 
    for i in range (1, len(num_used)) :
        if not num_used[i] :
            candidates.append(i)

    for cand in candidates :
        # 가로 세로 조건 만족하는 후보들 찾기
        row_used = [False]*(10)
        col_used= [False]*(10)

        for i in range(0,9):
            if board[y][i] != 0 :
                row_used[board[y][i]] =True # y,x 에서 가로부터 탐색
            if board[i][x] != 0 :
                col_used[board[i][x]]= True
        
        final_cand = []
        for i in range (1,10) :# 세개의 조건을 만족하는 후보만 뽑아내서 return
          if not row_used[i] and not col_used[i] and not num_used[i] :
              final_cand.append(i)
    return final_cand


def solve(depth) :
    if depth == len (fill_targets) :
        for row in board:
            print(*row)
        exit(0)

    cur_y, cur_x= fill_targets[depth]

    candidates = get_final_candidates(cur_y,cur_x)# 후보들을 가지고 왔고,

    for cand in candidates:
        board[cur_y][cur_x] = cand 
        solve(depth +1) 
        board[cur_y][cur_x] =0 # 백트래킹


    
 # row 012 col 012,345,678
# row 345 col 012 , 345, 678
# row 678 col 012, 345,678

solve (0)