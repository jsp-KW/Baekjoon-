import sys
from itertools import combinations


N,M,K = map(int,sys.stdin.readline().split())

# 1부터 N까지의 수
# 서로다른 M개의 수를 골라서, 적어도 K개의 수가 같으면 당첨
# 당첨될 확률은?

numbers= []

for i in range (1,N+1) :
    numbers.append(i)

my_choice = set(range(1,M+1))

total = 0
cnt = 0
for comb in combinations(numbers,M):
    total +=1

    if len(set(comb)& my_choice) >=K :
        cnt+=1

print(cnt/total) 

