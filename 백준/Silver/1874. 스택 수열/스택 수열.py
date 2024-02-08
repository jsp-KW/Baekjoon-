import sys

def make_seq (stack):
    temp = []
    result = []

    cur =  1

    for num in stack :
        
        while cur <= num:
            temp.append(cur)
            result.append('+')
            cur = cur +1


        if temp[-1] == num:
            temp.pop()
            result.append('-')
        
        else:
            print("NO")
            return

    for i in result:
        print(i)



n = int(sys.stdin.readline().rstrip())

stack = []

for i in range (n):
    num = int(sys.stdin.readline().rstrip())
    stack.append(num)

make_seq (stack)
