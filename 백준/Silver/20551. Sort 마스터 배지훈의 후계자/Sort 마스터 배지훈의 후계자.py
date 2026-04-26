import sys
import heapq
N, M = map(int,sys.stdin.readline().split())
nums = []
for _ in range (N) :
    num = int(sys.stdin.readline())
    nums.append(num)

nums.sort()

def lower_bound (arr, target) :
    left = 0
    right = len(arr)-1
    answer = -1 

    while left <=right :
        mid = (left+ right) //2

        if arr[mid] == target : # 더 값이 있을 수 있으니, 정답 저장후, mid 값을 -1 한걸 오른쪽을 왼쪽으로 당긴다
            answer = mid
            right = mid -1
        elif arr[mid] > target :
            right = mid-1

        else :
            left= mid +1


    return answer

answers = []
for _ in range (M):
    check = int(sys.stdin.readline())
    idx = lower_bound(nums, check)
    answers.append(idx)
        

for ans in answers :
    print(ans)