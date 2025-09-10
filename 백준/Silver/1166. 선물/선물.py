import sys

N,L,W,H = map(int,sys.stdin.readline().split())


lower, higher = 0.0, max(L,W,H)

for _ in range (100) :
    mid = (lower+higher)/2 

    if int(L//mid) * int(W//mid) * int(H // mid) >= N :
        lower = mid
    else:
        higher = mid

    
print(float(lower))