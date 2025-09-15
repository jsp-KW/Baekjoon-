import sys


# 커서 
# 문자열 길이 L, 커서 위치 가능 -> L+1

#출력 : 모든 명령어를 수행하고 편집기에 입력되어있는 문자열 반환


# count =  int(sys.stdin.readline())
# cursor = len(sentence) 

# operations = []
# for _ in range (count) :
#     op = sys.stdin.readline().rstrip("\n")
#     operations.append(op)

# for operation in operations:
    
#     if len(operation) == 1: #L,D,B -> 커서를 왼쪽, 오른쪽, 왼쪽에 있는 문자를 삭제
#         if operation == "L":
#             if cursor == 0:
#                 continue
#             else :
#                 cursor = cursor -1
        
#         elif operation == "D":
#             if cursor == len(sentence) :
#                 continue
#             else:
#                 cursor = cursor +1

                
        
#         else :
#             if cursor > 0 :
#                 sentence = sentence[:cursor-1] +sentence[cursor :]
#                 cursor = cursor-1

#     else : # P $ -> $ 라는 문자를 커서 왼쪽에 추가하기
#         add_ch = operation.split()[1]
#         sentence = sentence[:cursor] + add_ch + sentence[cursor:]
#         cursor = cursor +1
       
# print(sentence)

cursor_left =list( sys.stdin.readline().rstrip("\n"))
cursor_right = []
count = int(sys.stdin.readline())

for _ in range (count) :
    op = sys.stdin.readline().split()

    if op[0] == "L" :
        if cursor_left:
            cursor_right.append(cursor_left.pop())
    elif op[0] == "D" :
        if cursor_right :
            cursor_left.append(cursor_right.pop())
    
    elif op[0] == "B" :
        if cursor_left:
            cursor_left.pop()

    else :
        cursor_left.append(op[1])

print("".join(cursor_left +cursor_right[::-1]))
