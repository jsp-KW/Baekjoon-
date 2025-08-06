# import sys
# from queue import PriorityQueue

# N = int(sys.stdin.readline())
# h = PriorityQueue()

# problems = []
# for _ in range(N) :
#     deadline,cup_noodle_cnt = map (int, sys.stdin.readline().split())
#     problems.append((deadline, cup_noodle_cnt))


# problems.sort()

# solve_cnt = 0
# # print ("problems", problems)
# for deadline, cup_noodle  in problems :
#     h.put(cup_noodle)

#     if h.qsize() >deadline :
#         a =h.get()
#         # print ("제거된 컵라면 수" , a)


# result = 0

# while True :
#     if h.qsize() ==0 :
#         break
#     result += h.get()
# print (result)


import sys
import heapq

N= int(sys.stdin.readline())

problems = []

pq = []
for _ in range (N) :
    deadline, cup_noodle_cnt = map (int,sys.stdin.readline().split())
    problems.append((deadline, cup_noodle_cnt))

problems.sort(key= lambda x :x[0])

for deadline, noodle_cnt in problems :
    heapq.heappush(pq,noodle_cnt)

    if len(pq) > deadline :
        heapq.heappop(pq)


print(sum(pq))