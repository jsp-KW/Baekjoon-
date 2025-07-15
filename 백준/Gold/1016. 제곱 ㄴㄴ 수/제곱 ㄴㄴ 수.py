
import sys
import math
n, m = map(int, sys.stdin.readline().split())
length =m-n +1

arr = [True] * length

for i in range(2, int(math.isqrt(m)) +1) :

    square = i *i
    start = ((n+square -1)// square) * square
    
    for j in range(start, m+1, square) :
        arr[j-n] = False


print (sum(arr))
    
