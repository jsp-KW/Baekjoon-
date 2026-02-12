# 1~100000000000 산성 -1~ -100000000000 알칼리
# 0 에 가장 가까운 용액을 만들려고한다
# 같은 종류의 두 용액도 가능.
# 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾아보자
import sys

n = int (sys.stdin.readline())
acid = list(map(int,sys.stdin.readline().split()))

if acid[0] >0 and acid[n-1] >0 :
    print (acid[0], acid[1])
    sys.exit()
elif acid[0] <0 and acid[n-1] <0 :
    print(acid[n-2], acid[n-1])
    sys.exit() 

left = 0
right = n-1 

target_diff = float('inf')
combs = []
answer = (acid[left], acid[right])
while left < right :
    current_sum = acid[left] +acid[right]

    if abs (current_sum) < target_diff :
        target_diff = abs (current_sum)
        answer = (acid[left], acid[right])
    
    if current_sum < 0 : # 합이 0보다 작으면, left 증가
        left +=1 
    elif current_sum >0 : # 크면 right 증가
        right -=1
    else :
        break

print (answer[0], answer[1])