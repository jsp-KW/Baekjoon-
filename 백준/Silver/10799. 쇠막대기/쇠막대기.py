import sys

# 여러개의 쇠막대기를 레이저로 절단하려고 한다
# 효율적인 작업을 위해, 쇠막대기를 아래에서 위로 겹쳐 놓고
# 레이저 () , 쇠막대기 왼쪽 끝 ( , 오른쪽 끝 )

s = sys.stdin.readline().rstrip()

cnt = 0

stack = []

for i in range(0,len(s)):
    if s[i] == '(' :
        stack.append(s[i])
    else :
        stack.pop()
        if s[i-1] == ')' :
            cnt+=1
        else :
            cnt +=len(stack)
        

print(cnt)