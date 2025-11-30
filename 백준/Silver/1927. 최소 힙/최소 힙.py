import sys
import heapq
N = int (sys.stdin.readline())

# 자연수 x를 넣는다
# 가장 작은 값 출력하고 , 그 값을 배열에서 제거한다
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다


# 입력
# 연산의 개수 N
# x 가 자연수 : 배열에 x 값 추가
# x가  0 : 가장 작은 값 출력 후 , 그 값을 배열에서 제거
# x는 2^31보다 작은 자연수 또는 0이고, 음의 정수는 x

# 출력 
# 입력에서 0 이 주어진 횟수만큼 답을 출력한다, 만약 비어있는 경우 가장 작은 값을 출력하라고 한 경우 0

heap = []

op = []

for _ in range (N) :
    operation = int(sys.stdin.readline())
    op.append(operation)

for o in op :

    if o == 0 : # 가장작은 값 출력후, 배열에서 제거
        if len (heap) ==0 :
            print (0)
        else :
            print(heapq.heappop(heap))
    
    else :
        heapq.heappush(heap,o)
    

