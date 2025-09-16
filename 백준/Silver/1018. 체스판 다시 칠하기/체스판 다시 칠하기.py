import sys


# M x N 
N, M = map(int, sys.stdin.readline().split())

maps = [[]*(M) for _ in range (N)]
for i in range (N) :
    lines = sys.stdin.readline().rstrip("\n")
    maps[i] += lines


answer =float('inf')

for i in range (N-7) :
    for j in range (M-7) :

        repaint_w = 0
        repaint_b = 0

        for row in range (i,i+8) :
            for col in range (j, j+8) :
                expected_w = 'W' if (row+col)%2 == 0 else 'B'
                expected_b = 'B' if (row+col)%2 ==0 else 'W'


                if maps[row][col] != expected_w :
                    repaint_w +=1
                if maps[row][col] != expected_b :
                    repaint_b +=1
        answer = min(answer,repaint_b, repaint_w)


print (answer)


