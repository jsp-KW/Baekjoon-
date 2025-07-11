import sys

def hanoi (n, start, end) :
    if n == 1:
        print (start, end)
        return
    
    other = 6 -start-end # 기둥 1,2,3 =6 - 시작기등 - 목적기둥 ==> 보조기둥
    hanoi (n-1, start, other)
    print(start,end)
    hanoi (n-1,other, end)

n = int(sys.stdin.readline())
print(2**n - 1)
hanoi(n, 1, 3)