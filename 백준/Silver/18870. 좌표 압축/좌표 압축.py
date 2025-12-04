import sys
from collections import defaultdict

n = int (sys.stdin.readline())

numbers = list(map(int,sys.stdin.readline().split()))
#[2,4,-10,4,-9]

distinct_numbers = sorted(list(set(numbers)))
# [-10,-9,2,4]

d = defaultdict()

for index, value in enumerate(distinct_numbers) :
    d [value] = index


print(" ".join(str(d[num]) for num in numbers))
