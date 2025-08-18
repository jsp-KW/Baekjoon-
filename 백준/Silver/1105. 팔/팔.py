import sys

# L,R = map(int, sys.stdin.readline().split())

# eight_cnt = 0
# min_eight_cnt = float('inf')
# for num in range (L,R+1) :
    
#     str_num = str(num)
#     for ch in str_num:
#         if ch == '8' :
#             eight_cnt +=1

#     if min_eight_cnt > eight_cnt : 
#         min_eight_cnt = eight_cnt

#     eight_cnt = 0

# print(min_eight_cnt)

L,R = sys.stdin.readline().split()

if len(L) != len(R) :
    print(0)
else :
    answer = 0
   
    for i in range(0, len(L)):
        if L[i] != R[i] :
            break
        if L[i] == '8' and L[i] ==R[i] :
            answer +=1

    print (answer)