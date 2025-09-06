import sys

L = int(sys.stdin.readline())

set_nums = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())

# n을 포함하는 좋은 구간의 개수
# 좋은구간 -> S가 주어졌을때 A<B를 만족하고, A <=x <= B 를 만족하는 모든 정수 x가 집합 s에 속하지 않을때

if n in set_nums :
    print (0)
else :
    left = 0
    right = 0
    diff = 0
    diffs = []
    set_nums.sort()
    for num in set_nums :
        diff = n - num 
        diffs.append(diff)

    left = -1
    for i, d in enumerate(diffs) :
        if d > 0 :
            left = i
        else :
            break
    right = left+1
    

    left_value = set_nums[left] if left !=-1 else 0
    right_val = set_nums[right] if right !=-1 else 1001

    print ((n-left_value) * (right_val-n) -1)
 


