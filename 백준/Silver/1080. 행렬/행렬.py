import sys

N,M = map(int,sys.stdin.readline().split())

def flip (A,x,y) :
    for i in range (3):
        for j in range(3):
            if A[x+i][y+j] ==1 :
                A[x+i][y+j] =0
            else :
                A[x+i][y+j]=1


A = []
for _ in range (N) :
    lines =list(map(int, sys.stdin.readline().strip()))
    A.append(lines)

B =[]
for _ in range (N) :
    lines =list(map(int, sys.stdin.readline().strip()))
    B.append(lines)

count = 0

for i in range (N-2) :
    for j in range (M-2) :
        if A[i][j] != B[i][j] :
            flip(A,i,j)
            count +=1 

if A == B :
    print(count)

else :
    print(-1)



