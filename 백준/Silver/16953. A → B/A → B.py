import sys

A,B = map(int, sys.stdin.readline().split())

# 2를 곱한다
# 1을 수의 가장 오른쪽에 추가


# B 를 일단 2로 나눌수있으면 나누자

# 2로 나눌 수 없는 경우, 1을 제거


op_cnt = 0

while B>A :
   
    if B%2 == 0 :
        B = B//2 
        op_cnt = op_cnt+1

    elif B%10== 1:
        op_cnt = op_cnt+1
        B = B//10
       
    else :
        print(-1)
        exit()

if B == A: print (op_cnt+1)
else: print (-1)