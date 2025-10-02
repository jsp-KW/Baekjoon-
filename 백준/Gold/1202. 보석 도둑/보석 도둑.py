import sys
import heapq


# 보석 N개
# 각 보석마다 무개 Mi, 가격 Vi
# 가방을 K개 가지고 있고, 각 가방마다 최대 무게 Ci
# 가방에는 최대 한개의 보석만 넣을수 있음

# 생각 흐름 -> 가치순으로 정렬하면, 어차피 무게제한을 못 채우는 경우 못 챙김 ㅠㅠ
# 그러면? 무게순으로 일단 정렬하고, 가방제한 무게도 정렬하자
# 이 다음 부터 막힘..
# 어떻게 구성해야할까? -> 우선순위 큐
N, K = map(int ,sys.stdin.readline().split()) # 보석 개수, 가방 개수

v_list = [] 
for i in range (N) :
    M,V = map(int ,sys.stdin.readline().split()) # (무게,가격)
    v_list.append((M,V))

bag_weight_li = []

for i in range (K) :
    C = int(sys.stdin.readline().rstrip()) # 가방에 담을 수 있는 최대 무게
    bag_weight_li.append(C)

v_list.sort(key = lambda x:(x[0])) # 무게 기준 정렬
bag_weight_li.sort() # 가방 무게제한 정렬

pq = []
answer= 0
idx = 0 
#무게 제한을 만족하면서 가치가 비싼 보석들을 넣는데, 파이썬은 최소힙이 기본이라
#넣을땐-로 최소로 만들고, 뺄때 그 값에 - 를 곱한다.
for b in bag_weight_li : # 가방하나
    while idx < N and v_list[idx][0] <= b :
        heapq.heappush(pq, -v_list[idx][1])
        idx+=1


    if pq :
        answer += -heapq.heappop(pq)

print (answer)

