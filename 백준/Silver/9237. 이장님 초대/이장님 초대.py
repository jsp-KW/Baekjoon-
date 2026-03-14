import sys

n= int(sys.stdin.readline())
# 나무하나 심는데, 1일걸림
#

day = 1

grow_time = list(map(int,sys.stdin.readline().split()))

grow_time.sort(reverse=True)

result = []
for time in grow_time :
    result.append(time+day)
    day+=1


print(max(result)+1)