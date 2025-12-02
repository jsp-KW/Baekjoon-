import sys
import heapq

# 최대힙
# 파이썬은 기본적으로 최소힙
# 최대힙을 만드려면, 삽입시 -를 달고, 뺄때 - 제거한 걸로


# 배열에 자연수 x를 넣는다
# 가장 큰 값을 출력하고 그 값을 배열에서 제거한다

N = int(sys.stdin.readline())

heap = []

for _ in range (N) :
    x = int (sys.stdin.readline())

    if x ==0 :
        if len (heap) == 0 :
            print (0)
        else: # 가장 큰 값 출력
      
            max_val= heapq.heappop(heap)
            print (abs(max_val))

    else : #힙에 추가
        heapq.heappush(heap,-x)
        
         
            
    