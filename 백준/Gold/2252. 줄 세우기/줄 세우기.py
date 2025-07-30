import sys
from collections import deque

# 데크를 이용한 위상정렬

# queue 가 아닌 deque인 이유
# queue.Queue() -> thread safe 하도록 설계되었지만, 내부적으로 lock이 걸려 멀티 스레딩 환경에서는 안전하지만 느림
# get(), put()을 사용할 때 내부 락을 걸고 푸는 비용이 들기 때문에 단일 스레드 알고리즘에서 오히려 비효율적.
# 단일 스레드에서 빠르게 돌려야 할 경우 deque 가 성능이 좋고 간결함.
# list는 pop시 O(N) -> 적합 X
# deque -> append, popleft 모두 O(1)


###
# 1. 모든 학생의 진입 차수 게산
# 2. 진입차수 0인 학생의 번호 deque에 넣기
# 3. 큐가 비워질때까지
#   3-1. result 리스트에 큐에서 하나 popleft후 추가
#   3-2. popleft 된 학생의 다음 순서 학생이 존재하는 경우 다음 학생들의 진입차수 -1
#   3-3. 진입차수 0이 된 학생 다시 deque 추가
# ###

N,M = map(int, sys.stdin.readline().split())

students_graph = [[] for _ in range (N+1)] 
# 학생 1번이 2,3번 보다 앞서있는 경우
# students_graph[1] = [2,3] 으로 표현하기 위한 이중리스트 기반 인접 리스트 표현 방식

in_degree = [0] * (N+1) #

for _ in range (M) : # M번 반복
    A,B = map (int, sys.stdin.readline().split())
    students_graph[A].append(B) 
    in_degree[B] +=1 # A->B
   
dq = deque()

for i in range (1,N+1) : #학생은 N번까지 있으므로
    if in_degree[i] == 0: # 차수가 0인 경우 큐에 삽입
        dq.append(i)


result = []

while dq:#큐에 원소가 존재하는 경우 루프문 돌기
    cur = dq.popleft() #큐에서 꺼내오고
    result.append(cur) # 결과에 저장

    for next in students_graph[cur] : #cur 번째 학생의 다음 학생이 next
        in_degree[next] -=1 # next 학생의 차수 -1
        if in_degree[next] ==0 : # 만약 next 학생의 차수가 0이라면
            dq.append(next) # 큐에 next 학생 넣기


print (' '.join(map(str,result)))