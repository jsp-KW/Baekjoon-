import sys

# N, M 이 주어질때 M인 수열 모두를 구하자
#
N, M = map (int,sys.stdin.readline().split())

nums = [i for i in range (1,N+1)]
# 비내림차순 

nums.sort()
answer= []
def dfs (start, depth) :
    if depth ==M :
        print (*answer)
        return 

    for i in range (start, len(nums)) :
        answer.append (nums[i])
        dfs (i, depth+1)
        answer.pop()


dfs (0,0)