import sys
from itertools import combinations

nums = [0,1,2,3,4,5,6,7,8,9]
answers= []

want_to_know = int(sys.stdin.readline())

for i in range (1,11) :
    for combs in combinations(nums, i) :
        num = int(''.join(map(str,sorted(combs, reverse=True))))
        answers.append(num)

answers.sort()

if want_to_know <= len (answers) :

    print (answers[want_to_know-1])
else :
    print (-1)
