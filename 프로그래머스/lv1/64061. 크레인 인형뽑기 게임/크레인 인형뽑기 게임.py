from collections import deque

def solution(board, moves):
    answer =0
    dq = deque()
    for i in moves:
        for j in range(0,len(board)) :
                if  board[j][i-1] !=0:
                    doll = board[j][i-1]
                    board[j][i-1] =0
                    if len(dq) >0 and dq[-1] == doll:
                            dq.pop()
                            answer+=2
                            
                    else:
                        dq.append(doll)
                    break
                            
        
    return answer

