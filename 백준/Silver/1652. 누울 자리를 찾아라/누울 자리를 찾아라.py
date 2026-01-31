import sys
N = int(sys.stdin.readline())

board = [[]for _ in range (N)]

for i in range (N) :
    temp = list(map(str, sys.stdin.readline().rstrip()))
    board[i].extend (temp)

row_cnt = 0

for i in range (N) :
    cnt = 0
    for j in range (N) :
        if board [i][j] == '.' :
            cnt +=1
        else :
            if cnt >=2 :
                row_cnt +=1
            cnt = 0
    
    if cnt >=2 :
        row_cnt +=1

            

col_cnt =0

for i in range (N) :
    cnt = 0

    
    for j in range (N) :
        if board[j][i] == '.' :
            cnt+=1
        else :
            if cnt >=2 :
                col_cnt +=1
            cnt = 0
    
    if cnt >=2 :
        col_cnt+=1
        

print (row_cnt, col_cnt)
