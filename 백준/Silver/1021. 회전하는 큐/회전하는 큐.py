import sys
from collections import deque

# 첫번째 원소를 뽑아낸다
# 왼쪽으로 한칸 이동 -> 첫번째가 맨 뒤로가고, 두번째가 첫번째로 이동
# 오른쪽으로 한칸 이동 -> 마지막이 처음으로 됨.

N,M = map (int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))

dq = deque()
answer = 0
for i in range(1,N+1) :
    dq.append(i)

for t in target :

    idx = dq.index(t)
    left_cnt = idx
    right_cnt = len(dq) - idx

    if left_cnt <= right_cnt :
        dq.rotate(-left_cnt)
        answer += left_cnt
    else:
        dq.rotate(right_cnt)
        answer+= right_cnt


    dq.popleft()

print (answer)
        

