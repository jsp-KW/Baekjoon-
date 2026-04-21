import sys

N,M = map(int,sys.stdin.readline().split())

board =[]

board.append (list(map(int,sys.stdin.readline().split())))
board.append (list(map(int,sys.stdin.readline().split())))

result = sum(board[0][:N]) + sum(board[1][:M])
print(result)