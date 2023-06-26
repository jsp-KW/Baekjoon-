import sys

n = int(input())

sell={}

for i in range(n):
    s= input()
    if s not in sell:
        sell[s] =1
    else:
        sell[s]+=1

sorted_dict = sorted(sell.items(), key=lambda x: (-x[1], x[0])) #value 값으로 내림차순 후 key값을 기준으로 오름차순
print(sorted_dict[0][0])