import sys
from itertools import combinations

N = int(sys.stdin.readline())
decreasing_nums = []

nums = [i for i in range (10)]

for length in range(1,11) :
    for combination in combinations (nums, length) :
        
        number = int (''.join(map(str, sorted(combination, reverse=True))))
        decreasing_nums.append(number)


decreasing_nums.sort()

if N < len(decreasing_nums) :
    print(decreasing_nums[N])
    
else :
    print(-1)
    
    