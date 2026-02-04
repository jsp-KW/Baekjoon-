import sys


#x-0.5 --- 위치 --- x+0.5

N, L = map(int,sys.stdin.readline().split())

locations = list(map(int,sys.stdin.readline().split()))

locations.sort()

first = locations[0]
last = locations[N-1]


cnt = 0
limit =0

for loc in locations :
    if loc > limit :
        cnt +=1

        limit = (loc-0.5) + L

print(cnt)