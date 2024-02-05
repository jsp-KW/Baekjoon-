
# import sys
# # 정수 0 인 경우 -> 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거함
# # 정수가 0 이 아닌 경우 -> 배열에 정수를 추가하는 연산

# x = int(sys.stdin.readline()) # 정수 x 입력

# arr = []
# for i in range  (x) :
#     temp = int(sys.stdin.readline())

#     if temp != 0 : # 0 이 아니라면 배열에 추가
#         arr.append (temp)
#     else: # 0이라면 배열에서 절댓값이 가장 작은 값을 출력, 후 배열에서 제거
#         if not arr : # 리스트가 비어있는 경우 
#             print (0)
#         else : #리스트에서 절댓값이 가장 작은 친구를 출력
#             min_val = min(arr, key=lambda x: (abs(x), x))  # 절대값이 가장 작은 값 찾기
#             arr.remove(min_val) # 람다함수를 이용하여, 튜플을 통해 절대값, 원본 값 ( 첫번째 원소로 정렬 후, 절대값이 같은 경우 두번째 요소로 정렬함.)
#             print(min_val)


#우선순위 큐를 활용한 ..

import sys
import heapq

x = int (sys.stdin.readline())

abs_heap = []
for i in range (x) :
    n= int (sys.stdin.readline())
    if n != 0:
        heapq.heappush(abs_heap,(abs(n), n))
    else:
        if not abs_heap: 
            print (0)
        else:
            print (heapq.heappop(abs_heap)[1])

