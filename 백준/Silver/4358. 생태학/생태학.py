import sys
from collections import defaultdict

# 나무의 분포도 측정 , 전체 몇 % 차지하는지 구하자

trees = sys.stdin.read().splitlines()

dic =defaultdict(int)

all_cnt  =0
for t in trees :
    dic[t] +=1 
    all_cnt +=1

#     print (f"{key} {value:.4f}" )

answers = []
for key,value in dic.items() :
    value = (value/all_cnt)* 100
    answers.append((key,value))


answers.sort (key = lambda x : (x[0]))

for ans in answers :
    print(ans[0], f"{ans[1]:.4f}")
