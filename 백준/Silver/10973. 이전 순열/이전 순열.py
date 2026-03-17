import sys

N= int(sys.stdin.readline())
target =list(map(int,sys.stdin.readline().split()))
nums = [i for i in range (1,N+1)]

idx= -1

# 찾으려는 수  < target
# 5 4 3 2 1
# 1 2 3 4 

#4 3 2 1
# idx = 1,
for i in range (len(target)-1,0,-1) :
    if target[i] <target[i-1] :
        idx =i-1
        break

if idx ==-1 :
    print (-1)
else :#idx 랑 바꾸기 위해, target[idx] 값보다 작은 값들 중 가장 큰 값을 찾은 후 , max_min에 저장
    swap_idx= idx +1
    for j in range (idx+1,N) :
        if target[j] < target[idx] :
            if target[j] >= target[swap_idx] :
                swap_idx = j
    

    target[idx], target[swap_idx]  = target[swap_idx], target[idx]
    target[idx+1:] = sorted(target[idx+1:: ], reverse=True)#바로 최소값을 찾아야 하므로, idx+1부터 끝까지는 내림차순 정렬 해줘야함

    print(*target)


    





    
