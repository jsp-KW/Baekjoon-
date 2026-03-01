import sys
from collections import deque

N= int(sys.stdin.readline())
# 쓰여있는 수의 배수만큼 떨어져있는곳으로 갈 수 있다
# a->b , a에서 최소 몇번 점프해서 b번째가지 갈 수 있는지

bridge = list(map(int,sys.stdin.readline().split()))
start, end = map(int,sys.stdin.readline().split())
start = start -1
end = end -1

distance = [-1]*(N)

# 시작 a
# 칸 숫자 k = bridge[a]
# 갈수있는 위치, a+- k, a+- 2k, a+- 3k 범위 안에서
# 목표간 인덱스 - 현재칸 인덱스  = k의 배수

q = deque([start])
distance[start] = 0

while q :
    cur = q.popleft()
    if cur == end :
        break
    
    for i in range (cur,-1, -bridge[cur]) : # left,
        if distance[i] == -1 :
            distance[i] = distance[cur]+1
            q.append(i)
       
    for i in range (cur, N, bridge[cur]) :
        if distance[i] == -1 :
            distance[i] = distance[cur] +1
            q.append(i)
print(distance[end])

