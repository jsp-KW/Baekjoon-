import sys

N,M = map(int, sys.stdin.readline().split())

strings = set()

for _ in range (N) :
    temp = sys.stdin.readline().rstrip()
    strings.add(temp)

cnt = 0

for _ in range (M) :
    target = sys.stdin.readline().rstrip()
    if target in strings :
        cnt +=1 


print(cnt)


