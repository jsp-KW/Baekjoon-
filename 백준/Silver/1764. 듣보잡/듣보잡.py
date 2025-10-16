import sys


N,M = map(int, sys.stdin.readline().split())

듣도 = set()
보도 = set()

for _ in range (N) :
    temp = sys.stdin.readline().rstrip()
    듣도.add(temp)

for _ in range (M):
    temp = sys.stdin.readline().rstrip()
    보도.add(temp)

print (len(듣도&보도))
result = list(듣도&보도)

for r in sorted(result) :
    print (r)


