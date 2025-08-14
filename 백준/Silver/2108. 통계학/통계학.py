import sys
from collections import defaultdict

N = int(sys.stdin.readline())

산술평균 = 0

numbers = []
for _ in range (N) :
    n = int(sys.stdin.readline())
    numbers.append(n)


산술평균 = round(sum(numbers) / len(numbers))
print(산술평균)
numbers = sorted(numbers)

find_median = len(sorted(numbers)) //2
print( numbers[find_median])

check_many = defaultdict(int)

for temp in numbers :
    check_many[temp] +=1


max_val = max(check_many.values())

res = []
for k,v in check_many.items() :
    if v ==max_val :
        res.append(k)

if len(res)  >= 2:
    최빈값 = res[1]
else :
    최빈값 = res[0]
    

print (최빈값)

범위 = max(numbers) - min(numbers)

print(범위)