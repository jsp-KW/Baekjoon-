# M 미터가 필요하다
# 절단기에 높이 H를 지정, 높이를 지정하면, 톱날이 땅으로 부터 H미터 위로 올라감
# H 보다 큰 나무-> 잘림, H보다 작은 나무 안 잘림

import sys

N,M = map(int,sys.stdin.readline().split())
# H 를 구해야한다!!

Trees = list(map(int,sys.stdin.readline().split()))
Trees.sort()

left = 0
right = max(Trees)



cut_tree_len =  0
answer = 0

while left <= right :
    mid =(left + right) //2
    H=mid
    cut_tree_len = 0

    for i in range (0,len(Trees)):
        if Trees[i] > H : cut_tree_len += (Trees[i] - H)

   
    if cut_tree_len <M :
        right = mid-1
        
    else :
        answer = mid
        left = mid+1


print (answer)