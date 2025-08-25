# import sys

# M = int(sys.stdin.readline().strip())

# s = set()

# out = bytearray() 
# result = []
# for _ in range (M) :
#     op = sys.stdin.readline().rstrip("\n")
#     if op.startswith('check') :
#         target = int( op.split()[1])
#         if target in s :
#             result.append(1)
#         else :result.append(0)

#     elif op.startswith('add') :
#         target = int( op.split()[1])

#         if target in s : continue
#         else : s.add(target)

#     elif op.startswith('remove') :
#         target = int( op.split()[1])
#         if target not in s : continue
#         else : s.remove(target)
    
#     elif op.startswith('toggle'):
#         target = int( op.split()[1])
#         if target not in s : s.add(target)
#         else: s.remove(target)

    
#     elif op.startswith('empty'):
#         s= set()
    
#     elif op.startswith('all') :
#         s = set(range (1,21))
        

# for r in result :
#     print (r)

# import sys
# input = sys.stdin.readline

# M = int(input().strip())
# s = set()
# out = bytearray()  # 출력 버퍼

# for _ in range(M):
#     op = input().strip()

#     if op == 'empty':
#         s.clear()

#     elif op == 'all':
#         s = set(range(1, 21))

#     else:
#         cmd, xs = op.split()
#         x = int(xs)

#         if cmd == 'check':
#             out += b'1\n' if x in s else b'0\n'
#         elif cmd == 'add':
#             s.add(x)
#         elif cmd == 'remove':
#             s.discard(x)     
#         elif cmd == 'toggle':
#             if x in s:
#                 s.remove(x)
#             else:
#                 s.add(x)

# #
# sys.stdout.buffer.write(out)
import sys
from array import array
input = sys.stdin.readline

res = array('B') 

M = int(input())
S = 0  # 비트마스크 (1~20 → 비트 0~19)

for _ in range(M):
    line = input().strip()
    if line == 'all':
        S = (1 << 20) - 1 #0 20개에서 -1 하면, 1이 19개 
    elif line == 'empty':
        S = 0
    else:
        cmd, xs = line.split()
        x = int(xs) - 1 # 0~19 까지라, 정수변환후 -1
        m = 1 << x # 왼쪽으로 x칸 shift, x번째 비트만 1인 마스크 생성
        if cmd == 'add':
            S |= m
        elif cmd == 'remove':
            S &= ~m # not 후 and  함면 해당 비트만 꺼짐 
        elif cmd == 'check':
            res.append(1 if (S & m) else 0)# and로만 그 자리 탐색, 꺼진지 켜진지 확인가능
        elif cmd == 'toggle': # 다르면 1, 같으면 0인 xor,  즉 없으면 추가 있으면 제거(비트0으로)
            S ^= m
write = sys.stdout.write
for b in res :
    write('1\n' if b else '0\n')