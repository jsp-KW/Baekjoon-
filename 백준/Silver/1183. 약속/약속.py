import sys

n = int(sys.stdin.readline())

waits= []
for _ in range (n) :
    appointment, arrivals = map(int,sys.stdin.readline().split())
    result = arrivals-appointment
    waits.append(result)


waits.sort()

lo = waits[(n-1)//2]
hi = waits[n//2]
print(hi - lo + 1)