import sys
from itertools import combinations

result = []
while True :

    inputs = sys.stdin.readline().split()
    if inputs[0] == '0' :
        break

    else: 
        K = int(inputs[0])
        S = inputs[1::]
        S_int = []
        for n in S :
            int_val = int(n)
            S_int.append(int_val)


        for comb in combinations(S_int,6) :
            result.append(sorted(list(comb)))

        result.append("\n")


for res in result :
    if res == "\n" :
        print()
    else: print (* res)
