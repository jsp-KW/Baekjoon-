import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
x =int(sys.stdin.readline())
nums.sort()

result = set()

left = 0
right = N-1 

while left < right :

    if nums[left] + nums[right] == x :
        result.add((nums[left], nums[right]))
        left =left +1
    
    elif nums[left] + nums[right] > x :
        right = right -1 
    
    else :
        left = left + 1



print(len(result))
