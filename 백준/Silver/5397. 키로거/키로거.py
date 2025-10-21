import sys

T = int(sys.stdin.readline())

for _ in range(T):
    left_stack = []
    right_stack = []

    for ch in sys.stdin.readline().rstrip():
        if ch == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif ch == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif ch == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(ch)
    

    print(''.join(left_stack + list(reversed(right_stack))))
