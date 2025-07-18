import sys
from itertools import combinations
N,M = map(int, sys.stdin.readline().split())

country =[]

for _ in range(N) :
    rows = list(map(int, sys.stdin.readline().split()))
    country.append(rows)


houses = []
chickens = []

for r in range (N) :
    for c in range(N) :

        if country[r][c] == 1 :
            houses.append((r,c))
        elif country[r][c] ==2 :
            chickens.append((r,c))
        else :
            continue

result = float('inf')
for combination in combinations(chickens, M) :
    total_distance = 0
    for hx, hy in houses :
        min_distance = float('inf')
        for cx, cy in combination :
            distance = abs(hx-cx) + abs(hy-cy)
            min_distance = min(min_distance, distance)
        
        total_distance += min_distance
    result = min(result, total_distance)

print(result)
