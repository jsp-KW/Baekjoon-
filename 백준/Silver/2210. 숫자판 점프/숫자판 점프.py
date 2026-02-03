import sys

# 5x5 크기 숫자판이 있음
# 인접해있는 네 방향 다섯번 이동
# 칸에 적힌 숫자 차례로 붙이면 6자리 수 나옴
# 이동할때는 한번 거쳤던 칸을 다시 거쳐도 되고, 0으로 시작하는 수도 만들 수 있다


board = [[] for _  in range (5)] 

for i in  range (5) :
    temp = list (map(int,sys.stdin.readline().split()))
    board[i].extend (temp)

move = [(-1,0),(1,0),(0,-1),(0,1)]

res = set ()

def dfs (start, string,step) :

    cur_y, cur_x = start 
    get_str = str(board[cur_y][cur_x])
    string+= get_str
    if step ==5: 
        res.add(string)
        return
    
    for m in move :
        dy,dx = m
        move_y,move_x = cur_y+ dy, cur_x+dx
        if 0<=move_y <5 and 0<=move_x <5 :
            dfs ((move_y,move_x), string , step +1)

for i in range (5) :
    for j in range (5) :
        dfs ((i,j), "",0)
       
print (len(res))