import sys

N = int(sys.stdin.readline())

board = [[] for _ in range (N)]

# 사탕의 색이 다른 인접한 두 칸을 고른다, 그다음사탕을 서로 교환
# 모두 같은 색으로 이루어져 있는 가장 긴 연속된 행, 또는 열을 통해 사탕을 모두 먹는다
# 사탕이 있을때, 먹을 수 있는 사탕의 최대 개수를 구하자

# 빨간색 :C 파란색: P, 초록색: Z , 노란색 : Y

for i in range (N) :
    temp= list (sys.stdin.readline().rstrip())
    board[i].extend(temp)


def check_candy () :
    best = 1
    count_candy = 0
    for i in range (N) :
        prev =  board[i][0]
        count_candy =1 
        for j in range (1,N) :
            if board[i][j]  == prev :
                count_candy +=1
            else :
                prev = board[i][j]
                count_candy =1 
            
            best =max(best, count_candy)

    for i in range (N) :
            prev = board[0][i] 
            count_candy =1
            for j in range (1,N) :
                if board[j][i] == prev :
                    count_candy +=1
                else :
                    prev = board[j][i]
                    count_candy = 1
                
                best = max (best, count_candy)
    return best
            
            
            

max_cnt = 0
for i in range (N):
    for j in range (N) :

        if 0<=j <N-1  :
            temp = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = temp
            res = check_candy()
            max_cnt = max(max_cnt, res)
            if board[i][j] != board[i][j+1] :
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
        if 0<= i <N-1 :
            temp = board[i][j]
            board[i][j] = board[i+1][j]
            board[i+1][j] = temp
            res = check_candy()
            max_cnt = max(max_cnt, res)
            if board[i][j] != board[i+1][j] :
                board[i][j] , board[i+1][j] = board[i+1][j], board[i][j]

            
print(max_cnt)


