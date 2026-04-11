import sys

N = int(sys.stdin.readline())

# 최대 값, 최소값을 출력

nums = list(map(int,sys.stdin.readline().split()))
operations = list(map(int,sys.stdin.readline().split())) # +-x%
min_val = float('inf')
max_val = -float('inf')
def dfs (idx, current) :
    global min_val, max_val
    if idx == N :
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return 
    
    if operations[0] > 0 :
        operations[0] -=1
        dfs (idx+1, current + nums[idx])
        operations[0] +=1


    if operations[1] > 0 :
        operations[1] -=1
        dfs(idx+1, current-nums[idx])
        operations[1] +=1

    if operations[2] > 0 :
        operations[2] -=1
        dfs(idx+1, current*nums[idx])
        operations[2] +=1
    

    if operations [3] > 0 :
        operations[3] -=1
        if current  < 0 :
            dfs(idx+1, -(-current // nums[idx])) # 파이썬 음수면 내림이라, -3//2 = -1이아닌 -2라
        else:
            dfs(idx+1, current // nums[idx])
        operations[3] +=1

    
dfs (1,nums[0])

print(max_val)
print(min_val)



    
