import sys

N = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))

def can_see(i, j):
    a, b = i, j
    if a > b:
        a, b = b, a  

    for k in range(a + 1, b):
        left = h[k] * (b - a)
        right = h[a] * (b - a) + (h[b] - h[a]) * (k - a)
        if left >= right:  
            return False
    return True

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        if can_see(i, j):
            cnt += 1
    ans = max(ans, cnt)

print(ans)
