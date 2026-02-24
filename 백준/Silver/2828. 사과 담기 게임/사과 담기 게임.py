import sys

# 스크린은 N칸 나누어져있고, M 칸을 차지하는 바구니가 있다

# N
# M    M<N

# 5칸  - - - - -
# 1칸 -

N, M = map(int,sys.stdin.readline().split())# 1칸부터
J = int(sys.stdin.readline())


left = 1
right = M

answer= 0

apples = []
for _ in range (J) :
    apple_loc= int(sys.stdin.readline())
    if apple_loc < left :
        answer+= abs(apple_loc-left)
        left= apple_loc
        right = left+M -1
    elif apple_loc >right :
        answer+= apple_loc- right
        right = apple_loc
        left = right - M +1
    else :
        continue

print(answer)
