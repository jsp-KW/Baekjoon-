
import sys
import heapq

T = int (sys.stdin.readline())

for _ in range (T) :
    operation_cnt = int (sys.stdin.readline())
    min_q = []
    max_q = []
    isLive = [False] *(operation_cnt)

    def clean_max() :
        while max_q and not isLive[max_q[0][1]]:#(-value,i) 에서 [i]
            heapq.heappop(max_q)# 힙에서 제거

    def clean_min() :
        while min_q and not isLive[min_q[0][1]]:# (value, i) [i]
            heapq.heappop(min_q)
    
    for i in range (operation_cnt) :
        temp = sys.stdin.readline().split()
        operation = temp[0]
        value = int(temp[1])
        if operation == 'I' :
            heapq.heappush(min_q,(value,i))
            heapq.heappush(max_q, (-value,i))
            isLive[i] = True
        else :
            if value == 1 :
                clean_max()
                if max_q :
                    isLive[heapq.heappop(max_q)[1]] =False#이제 진짜 없애는거

            else :
                clean_min ()
                if min_q :
                    isLive[heapq.heappop(min_q)[1]] = False # 
    clean_max()
    clean_min()


    if not min_q and not max_q :
        print("EMPTY")
    else :
        print(-max_q[0][0], min_q[0][0])