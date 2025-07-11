# import sys

# N,M = map(int, sys.stdin.readline().split())

# nums = list( map(int, sys.stdin.readline().split()))

# answer =[]

# for _ in range(3) :
#     sum =0
#     start,end = map(int, sys.stdin.readline().split())

#     if start == end :
#         sum = nums[start-1]
        
#     else:
#         for i in range(start-1,end):
#             sum += nums[i]
    
#     answer.append(sum)

# for a in answer:
#     print(a)


import sys

N,M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N+1)
for i in range(1,N+1) :
    prefix_sum[i] = prefix_sum[i-1] +nums[i-1]


for _ in range(M) :
    i,j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j]-prefix_sum[i-1])

    