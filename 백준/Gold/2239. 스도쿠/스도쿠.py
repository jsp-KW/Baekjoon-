import sys


board = [[] for _ in range (9)]

for i in range (9) :
    temp = list(map(int,sys.stdin.readline().rstrip()))
    board[i].extend(temp)

zeros = []
numbers = [i for i in range (1,10)]

for i in range(9) :
    for j in range (9) :
        if board[i][j] == 0  :
            zeros.append((i,j))

#  3x3 사이즈에서 0의 개수가 몇개인지 구하고, 그게 x라면

def check_zero_cnt (r,c,num) :

    for i in range (9) :
        if board[r][i] ==num or board[i][c] == num :
            return False
        
    start_r, start_c = (r//3)*3 , (c//3)*3 
    for i in range (3) :
        for j in range (3) :
            if board[start_r +i][start_c + j] == num :
                return False 
            
    return True 


def backTracking(depth) : 
    if depth == len(zeros) :
        for row in board :
            print("".join(map(str, row)))
        sys.exit(0)

    r,c = zeros[depth]
    
    for try_num in numbers :
        if check_zero_cnt(r,c, try_num) :
            board[r][c] = try_num
            backTracking(depth+1)
            board[r][c] = 0


backTracking(0)