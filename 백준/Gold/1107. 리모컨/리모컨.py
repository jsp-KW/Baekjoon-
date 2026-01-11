import sys

# 0~9 , + - , +: 채널 +1 , -: 채널 -1
# 채널 0에서 - 누른경우 채널 변화 x, 채널은 무한대만큼있음. 상한 500000
# 채널 N으로 이동하기 위해, 버튼을 "최소 몇번 눌러야하는지?"
# 현재 채널 100번
# 버튼 일부숫자 고장남
N = int (sys.stdin.readline())
broken_cnt = int(sys.stdin.readline())
if broken_cnt > 0  :
    broken_btn = list(map(int,sys.stdin.readline().split()))
else :
    broken_btn =  []



answer = abs(N-100) # 시작 채널이 100이므로, 상한 설정

#왼쪽 0 , 채널 오른쪽 무한대,
# 1 2 3 4 5 9 
# 5455 번 , ++  -> 6번

def can_possible (x) :

    if x == 0 :
        if  0 in broken_btn :
            return False 
        return True
    
    while x> 0 :
        temp  = x % 10
        if temp in broken_btn :
            return False
        x = x // 10
    return True


for x in range (0,1000001) :
    if can_possible(x) :
        press_cnt = len(str(x))
        plus_or_minus_cnt = abs(N-x)
        answer = min (answer , press_cnt +plus_or_minus_cnt)
        
print (answer)