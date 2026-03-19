import sys

#절사 평균 : 가장 작은값들과 큰 값들을 제외하고 평균을 내는 것을 말한다
# 30% 경우, 15%씩 제외하고 평균을 계산한다.
#25-> 3.75 -> 반올림 4명씩 제외
# 평균도 정수로 반올림 -> 16.7경우->17

n = int(sys.stdin.readline())
scores= []
for _ in range (n) :
    score=  int(sys.stdin.readline())
    scores.append(score)

scores.sort()

def make_round (num) :
    if num - int(num) >= 0.5 :
        return int(num) +1
    else :
        return int(num)
    
remove_per =make_round( n * 0.15)

if n -(2*remove_per) == 0 :
    print(0)
    sys.exit()


if remove_per == 0 :
    print (make_round(sum(scores) / n))
    sys.exit()

avg=sum(scores[remove_per : -remove_per]) / (n-(2*remove_per))

print(make_round(avg))