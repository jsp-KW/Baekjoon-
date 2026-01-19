import sys

N = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))

max_val = max(nums)
for i in range (len(nums)) :
    nums[i] = (nums[i]/max_val) *(100)

print(sum(nums)/len(nums))