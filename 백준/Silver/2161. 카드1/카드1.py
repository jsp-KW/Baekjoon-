import sys
from collections import deque
# N장의 카드
#

N = int(sys.stdin.readline())

cards = [i for i in range (1,N+1)]

removed = []

q = deque(cards)

last = 0
while True :
    # 앞에서 제거하고,
    # 바로 뒤로 넣는다
    if len(removed) == N-1 :
        last = q[0]
        break

    removed.append (q.popleft())
    q.append(q.popleft())

print(*removed, last)