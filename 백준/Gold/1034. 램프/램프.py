import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

li = []
for _ in range(N):
    row = sys.stdin.readline().strip()
    li.append(row)


try:
    K = int(sys.stdin.readline().strip())
except:
    K = 0

pattern_count = defaultdict(int)
for row in li:
    pattern_count[row] += 1


max_on = 0
for pattern, count in pattern_count.items():
    zero_cnt = pattern.count('0')
    if zero_cnt <= K and (K - zero_cnt) % 2 == 0:
        max_on = max(max_on, count)

print(max_on)
