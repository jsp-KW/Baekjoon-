# import sys
# #from itertools import product
# A,B =map(str,sys.stdin.readline().rstrip().split())
# n,m = len(A), len(B)


# # elif len(A) <len(B) :

# #     # A의 앞에 아무거나 추가 가능 0 index에 추가
# #     # A의 뒤에 아무거나 추가 가능 
# #     can_operation = len(B)- len(A)
 
# #     origin_len_a = len(A)
# #     #adaabcc
# #     #aababbc

# #     origin_A = A
# #     result = origin_len_a # 최악의 경우 len A 만큼 다 틀리는 경우
    
# #     how = ["앞", "뒤"]
# #     how_combinations = list(product(how,repeat=can_operation)) # 연산가능한 횟수개 만큼 앞뒤 조합 만들고 리스트로 ("앞","뒤","앞")
    
# #     for h in how_combinations :
# #         collection_A = origin_A #조합마다 매번 A 배열 바뀌니까 원본으로 초기화 해놓고
# #         iter_result =0
# #         #조합을 가지고 문자열 A를 변형
# #         for ch in range(0, len(h)):
# #             if h[ch] =="앞" :
# #                 collection_A= "X"+collection_A
# #             else:
# #                 collection_A = collection_A+"X"
# #         #변형한 문자열 A를 검사
# #         for i in range(0,len(collection_A)):
# #             if collection_A[i]=="X" : # 맞는 판정
# #                 continue
# #             if collection_A[i] !=B[i]: # 다른 판정이므로
# #                 iter_result+=1
# #         result = min(result,iter_result) # iter_result는 앞 또는 뒤 연산으로 변형된 문자열 A가 원래 보다 덜 틀리게 되는 경우

# if n==m:
#     for i in range(0,len(A)) :
#         if A[i] != B[i]:
#             result +=1
#     print(result)


# else:
   
#     result = n    
   
#     for s in range(m - n + 1):
#         mism = 0
#         for i in range(n):
#             if A[i] != B[s + i]:
#                 mism += 1
#                 if mism >=result :
#                     break
#         if mism < result:
#             result = mism

#             if result ==0 :
#                 break
#     print(result)

import sys

A, B = sys.stdin.readline().split()
n, m = len(A), len(B)

if n == m:
    result = sum(1 for i in range(n) if A[i] != B[i])
    print(result)
else:
    result = n  # 최악: 전부 다름
    for s in range(m - n + 1):          # s는 A가 B에 놓일 시작 위치
        mism = 0
        for i in range(n):              # A[i] vs B[s+i] 자리별 비교
            if A[i] != B[s + i]:
                mism += 1
                if mism >= result:      # 가지치기 (옵션)
                    break
        if mism < result:
            result = mism
            if result == 0:             # 더 낮아질 수 없음 (옵션)
                break
    print(result)