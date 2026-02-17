import sys
N, M = map(int,sys.stdin.readline().split())

board = [[] for _ in range (N)]

for i in range (N) :
    temp = list(map(int,sys.stdin.readline().split()))
    board[i].extend(temp)


# ---- -> 대칭 의미x, 회전시 2개
# 네모 -> 회전 의미x, 대칭 의미 x-> 1개
# ㅗ 모양 -> 4개 회전만

# ----

cordinates = [

[(0,0),(0,1),(0,2),(0,3)],
[(0,0),(1,0),(2,0),(3,0)],

# ㅁ
[(0,0),(0,1),(1,0),(1,1)],

# ㄴ
[(0,0),(0,1),(0,2),(1,2)],

[(0,0),(0,1),(0,2),(1,0)],

[(0,0),(1,0),(1,1),(1,2)],

[(0,1),(1,1),(2,1),(2,0)],



[(0,0),(1,0),(2,0),(0,1)],

[(0,0),(0,1),(1,1),(2,1)] ,

[(1,0),(1,1),(1,2),(0,2)],

[(0,0),(1,0),(2,0),(2,1)],
# ㄴ
#  |

[(0,0),(0,1),(1,1),(1,2)],
[(0,1),(1,1),(1,0),(2,0)],
[(1,0),(1,1),(0,1),(0,2)],
[(0,0),(1,0),(1,1),(2,1)],

# ㅗ
[(1,0),(1,1),(0,1),(2,1)],
[(0,0),(1,0),(1,1),(2,0)],
[(0,0),(0,1),(1,1),(0,2)],
[(0,1),(1,1),(1,0),(1,2)]
]

ans = 0
for r in range (N):
    for c in range (M) :
            
            for shape in cordinates :
                cur_sum = 0
                possible = True 
                for dx, dy in shape :
                    nx,ny = c+dx, r+dy 
                    if  0<= nx < M and 0 <= ny <N :
                        cur_sum += board[ny][nx]
                    else :
                         possible = False
                         break
                if possible :
                     ans = max(ans, cur_sum)

print(ans)