import sys

N = int(sys.stdin.readline())

li = []

for i in range (N) :
    temp = list(map(int,sys.stdin.readline().split()))
    li.append(temp)

for i in range (N) :
    for j in range (N) :
        for k in range (N) :

            if li[j][i] and li[i][k] :
                li[j][k] = 1

for row in li :
    print (*row)
