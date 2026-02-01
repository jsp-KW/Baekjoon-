import sys

N,M = map(int,sys.stdin.readline().split())

board = []
for _ in range (N) :
    temp= list (map(str, sys.stdin.readline().rstrip()))
    board.append (temp) 

final =""
Hammings = 0
for j in range (0,M) :

   
    counts = {'A':0 , "G" : 0 , "C" :0 , "T": 0}
    for i in range (0, N) :
        counts[board[i][j]] +=1 

    max_val = -1
    selected = ''
    
    for ch in ['A','C','G','T'] :
        if counts[ch] > max_val :
            max_val = counts[ch] 
            selected = ch
    
    final +=selected
    Hammings += (N- counts[selected])

print (final)
print (Hammings)
    