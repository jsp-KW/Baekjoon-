import math

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

ans = -1

for r in range(N):
    for c in range(M):
        for dr in range(-N, N):
            for dc in range(-M, M):
                if dr == 0 and dc == 0:
                    continue 

                str_num = ""
                nr, nc = r, c
                while 0 <= nr < N and 0 <= nc < M:
                    str_num += grid[nr][nc]
                    num = int(str_num)
                    
                   
                    if math.isqrt(num)**2 == num:
                        ans = max(ans, num)
                    
                    nr += dr
                    nc += dc

print(ans)
