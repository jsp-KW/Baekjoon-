import sys


N,M = map(int, sys.stdin.readline().split())

m = []
for _ in range (N) :
    temp = list(map(int,sys.stdin.readline().rstrip()))
    m.append(temp)


result = 1
search_range = min(N, M)
for i in range (N) :

    for j in range (M) :

        start = m[i][j]
       
        for k in range (1,search_range) :
            if i+k <N and j+k <M :
                if start == m[i][j+k] and start == m[i+k][j] and start == m[i+k][j+k] :
                    result = max(result, (k+1)**2)

print (result)