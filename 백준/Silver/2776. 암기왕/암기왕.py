import sys

T = int(sys.stdin.readline().rstrip("\n"))

for _ in range(T):
        

    n= int(sys.stdin.readline().rstrip("\n"))

    memo1 = set(map(int,sys.stdin.readline().split()))

    m = int(sys.stdin.readline().rstrip("\n"))


    check = list(map(int,sys.stdin.readline().split()))

    for t in check:
        if t in memo1:
            print("1")
        else:
            print("0")