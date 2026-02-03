import sys

num = int (sys.stdin.readline())

isOk = False 

if '0' not in str(num) :
    print(-1)
    sys.exit()

sum_all = 0
num_to_str = list (str(num))


for ch in num_to_str: 
    sum_all +=  int(ch)


if sum_all %3 != 0 :
    print( -1)
    sys.exit()

num_to_str.sort (reverse=True)


print(''.join(num_to_str))    