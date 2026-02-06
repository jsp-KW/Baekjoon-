import sys

N = int(sys.stdin.readline())

# N 개의 로프, w인 물체를 들어올릴때 k 개 사용하면, w/k 만큼 중량이 걸림
# 물체의 최대 중량을 구해내자

ropes = []
for _ in range (N) :
    r = int(sys.stdin.readline())
    ropes.append(r)

ropes.sort(reverse=True)

ans = 0

for i in range (N) :
    
    cur = ropes[i]*(i+1)

    if cur > ans :
        ans = cur

print(ans)

