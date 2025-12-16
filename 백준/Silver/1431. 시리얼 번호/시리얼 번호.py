import sys


n = int(sys.stdin.readline())

temp = []

for _ in range (n) :
    s = sys.stdin.readline().rstrip()
    length = len (s)
    temp.append((s,length))


temp.sort(key= lambda x : (x[1],
 (sum(list(int(num) for num in x[0] if num.isdigit()))),
   x[0]))


for ans in temp :
    print (ans[0])