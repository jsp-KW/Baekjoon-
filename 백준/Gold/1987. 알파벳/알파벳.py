import sys


# 세로 R 칸, 가로 C칸
#  상하좌우 이동가능, 새로 이동한 칸에 적힌 알파벳은 기존의 이동 경로 안의 알파벳과 달라야함.
# 좌측 상단에서 시작하여 말이 최대한 몇 칸을 지날 수 있는지,
# 좌측 상단의 칸도 포함이므로 최소 1

r,c = map(int,sys.stdin.readline().split())

s = set()

board = []

for _ in range (r) :
    board.append(list(map(str, sys.stdin.readline().rstrip())))

start = ((0,0))
dx = [0,0,-1,1]
dy = [1,-1,0,0]



ans = 1
def dfs (y,x,depth) :
    global ans 
    if not (0<=y<r and 0 <= x < c) : return 

    if board[y][x] in s : return

    s.add(board[y][x])

    ans = max(ans, depth)

    for i in range (4) :
        dfs (y+dy[i], x + dx [i] , depth +1)
    
    s.remove(board[y][x])


dfs(0,0,1)
print (ans)