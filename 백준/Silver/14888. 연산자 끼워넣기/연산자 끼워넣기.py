import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split(' ')))
opt_count = list(map(int, sys.stdin.readline().split(' ')))
opt_li = ['+','-','*','/']
min_ans = float('inf')
max_ans = float('-inf')

def dfs (idx, result ):
    global min_ans, max_ans

    if idx == n :
        min_ans = min (min_ans, result)
        max_ans = max(max_ans, result)
        return
    

    for i in range(4) :
        if opt_count[i]>0:
            opt_count[i]-=1

            if i==0 :
                dfs(idx+1, result+ num[idx])
            elif i==1 :
                dfs(idx+1,result -num[idx])
            elif i==2:
                dfs(idx+1,result*num[idx])
            elif i ==3:
                if result <0 :
                    dfs(idx+1, -((-result)//num[idx]))
                else :
                    dfs(idx+1, result// num[idx])
            
            opt_count[i] +=1

dfs(1,num[0])


print(max_ans)
print(min_ans)

