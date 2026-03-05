import sys
from collections import deque
# 1~N
# N개의 풍선 원형
# i-1 / i / i+1
#  1번 풍선 왼쪽 N


# 1번을 터뜨린다. -> 풍선 안의 종이를 꺼내, 종이에 써진 값만큼 이동하여 풍선을 터뜨린다
# 양수일때는 오른쪽으로, 음수일때는 왼쪽으로 이동

N = int(sys.stdin.readline())
destroy_order = 1 

destroyed = [-1] *(N)
balloons =  list(map(int,sys.stdin.readline().split()))
info = [(idx,balloon) for idx, balloon in enumerate(balloons)]

cur = 0
q = deque(info)
answers = []
while q :
    cur_idx, cur_step = q.popleft()
    answers.append(cur_idx+1)
    destroy_order +=1
    # rotate (음수) : 왼쪽으로 밀기 / rotate(양수) : 오른쪽으로 밀기
    if cur_step > 0 :
        q.rotate (-(cur_step-1)) # 왼쪽으로 이동(양수면)
    elif cur_step < 0 :
        q.rotate (-cur_step) # 오른쪽 끝에서 0번으로(음수 스텝이면, 보정해서)
    
print(*answers)
