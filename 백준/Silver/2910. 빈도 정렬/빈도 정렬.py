import sys

from collections import Counter
from collections import defaultdict
X,Y = map(int, sys.stdin.readline().split())

numbers =  list(map(int, sys.stdin.readline().split()))

dictionary=  defaultdict(int)
dictionary.keys()
for n in numbers:
    dictionary[n] +=1

result = []
order_idx = 0
for k,v in dictionary.items() :
    result.append((k,v,order_idx))
    order_idx+=1


result.sort(key =lambda x: (-x[1],x[2]))

finall_result = []
for k,v,idx in result :
    
    for i in range (v) :
        finall_result.append(k)

print (*finall_result)
    
