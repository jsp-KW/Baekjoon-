import sys
from collections import deque


# 공기 청정기, 칸 x인 경우 확산 x, 미세먼지는 인접한 네 방향으로확산
# 동시에 일어난다 확산은, n,  n/5 이고, r,c 에 남는건 r,c - (확산된 방향개수 x r,c/5)



# 공기청정기
# 위쪽 반시계, 아래쪽 : 시계
# 바람의 방향대로 한칸씩 이동한다


R,C, T = map(int,sys.stdin.readline().split())
board= [[] for _ in range (R)]

for i in range (R) :
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)


# 공기청정기 ==-1 

cleans = []
dusts = []
for i in range (R) :
    for j in range (C) :
        if board[i][j] == -1 :
            cleans.append((i,j))
        elif board[i][j] != 0 and board[i][j] !=-1:
            dusts.append((i,j))


def find_dusts () :
    result = []
    for i in range (R) :
        for j in range (C) :
            if board[i][j] > 0 :
                result.append((i,j))
    return result


            
# 꼭짓점 , Y,X 좌표 기준 -> 0,0 / 0,C-1/ R-1,0 / R-1,C-1 이면 두 좌표 밖에 없음  

def spread() :
    temp =[[0]*(C) for _ in range (R)] #쓰기 전용

    for y, x in cleans :
        temp[y][x] = -1 
    
    for cur_y, cur_x in dusts :
        if board[cur_y][cur_x] <=0  :
            continue

        spread_mount = board[cur_y][cur_x] //5

        dy =[-1,1,0,0]
        dx =[0,0,-1,1]
        cnt = 0
        for i in range (4) :
           
            my,mx = dy[i] +cur_y, dx[i] + cur_x 
            if 0<= my < R and 0<= mx < C and board[my][mx] !=-1  :
                temp[my][mx]  += spread_mount 
                cnt+=1
        
        temp[cur_y][cur_x] += board[cur_y][cur_x] - (cnt*spread_mount) # += 다른곳에서도 먼지가 확산 가능해서
    return temp





# 공기청정기 위쪽 아래쪽
# 여기 방향 너무 헷갈린다.
def cleaning () :
    upper = cleans[0][0] # y좌표
    lower = cleans[1][0] # y-1좌표
    
 

       #아래쪽으로 반시계
    for i in range (upper-1,0, -1) :
        board[i][0] = board[i-1][0]
    
    #왼쪽
    for i in range (0, C-1) :
        board[0][i] = board[0][i+1]

      #위로
    for i in range (0,upper) :
        board[i][C-1] = board[i+1][C-1]

    #으른쪽으로 밀기
    for i in range (C-1,1,-1) :
        board[upper][i] = board[upper][i-1]
    board[upper][1] = 0 #청정기 때문에

   




       # 위쪽
    for i in range  (lower+1, R-1) :
        board[i][0] = board[i+1][0] 

       # 왼쪽
    for i in range (0, C-1) :
        board[R-1][i] = board[R-1][i+1]

        
    #아래쪽
    for i in range (R-1,lower,-1) :
        board[i][C-1] = board[i-1][C-1]
   
    #오른쪽
    for i in range (C-1, 1,-1) :
        board[lower][i] = board[lower][i-1]
    board[lower][1] = 0




 
    #청정기 표시 확실히 복구
    board[upper][0] = -1 
    board[lower][0] =-1


for _ in range (T) :
    dusts= find_dusts()
    board = spread()
    cleaning()


ans= 0
for i in range (R) :
    for j in range (C) :
        if board[i][j] ==-1 :
            continue
        else :
            ans += board[i][j]

print(ans)
        