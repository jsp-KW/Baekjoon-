import sys
import math
from itertools import combinations

T= int(sys.stdin.readline())

for _ in range (T) :
    cordinates_cnt = int(sys.stdin.readline())
    cordinates = set()
    for _ in range (cordinates_cnt) :
        x,y = map(int, sys.stdin.readline().split())
        cordinates.add((x,y))

    cordinates= list(cordinates)
    min_value = float('inf')

    for combination in combinations(cordinates, len(cordinates)//2) :
        x1,y1 =0,0
        x2,y2 =0,0

        comb_set = set(combination)

        for x,y in cordinates :
            if (x,y)  in comb_set :
                x1+= x
                y1 +=y

            else:
                x2 +=x
                y2 +=y
            

        dx = x1-x2
        dy = y1-y2

        length = math.sqrt(dx*dx + dy*dy)
        min_value = min (min_value, length)
    
    print(min_value)