import sys
from collections import deque
N,K = map(int,sys.stdin.readline().split())

numbers = list(map(int,sys.stdin.readline().split()))


# 뒤집는거 ,k 개 자체를
# 시작 인덱스 ~ 끝인덱스+1 [:끝인덱스+1]
#bfs

# 뒤집는 함수
def reverse(arr, start_idx, k) :
    new_arr = arr[:]

    new_arr[start_idx: start_idx+k] = new_arr[start_idx: start_idx+k][::-1]
    return new_arr

# bfs ()
# 오름차순으로 정렬


# can_make_asc = 0

# 오름차순인지 check
# def check_asc(arr) :
#     back_val =  arr[0]
#     for i in range (1, len(arr)) :
#         if back_val >= arr[i] :
#             return False
#         else :
#             back_val = arr[i]

#     return True


def bfs(input_arr,K):
    N = len(input_arr)
    target = tuple(sorted(input_arr))
    start = tuple(input_arr)
    visited ={start}

    
    que = deque([(start,0)])

    
    while que :
        cur,depth = que.popleft()

        if cur == target:
            return depth
        
        for i in range(N-K+1) :
            nxt= reverse(list(cur),i,K)
            nxt = tuple(nxt)

            if nxt not in visited:
                visited.add(nxt)
                que.append((nxt, depth+1))

    return -1

result = bfs(numbers,K)

print(result)
             
