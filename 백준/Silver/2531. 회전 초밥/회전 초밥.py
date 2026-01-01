import sys

N , d, k , c = map (int,sys.stdin.readline().split())
#접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수 , 쿠폰 번호
arr = []
for _ in range (N) :
    num = int(sys.stdin.readline())
    arr.append(num)


arr2 =  arr + arr[0:k-1]

susi_count = [0] *(d+1)
distinct = 0

# 첫번째 윈도우에서, 범위가 k 인거 까지 초밥종류 + 갯수 카운트
# 윈도우 설정
for i in range(k):
    if susi_count[arr2[i]] == 0 :
        susi_count[arr2[i]] +=1
        distinct = distinct+1
    else: 
        susi_count [arr2[i]] +=1
    
best_case = distinct + (1 if susi_count[c] ==  0 else 0)

# 0 ~ N-1 까지만 볼건데,
# N-1 에서는 K-1 개만 더 보면됨

# 오른쪽 범위, K-1 ~ N-1 + K-1 

left = 0
right = k 

# 한칸식 옆으로, 왼쪽은 빠지고, 오른쪽은 증가하므로
for _  in range (1,N) :
    x = arr2[left]
    susi_count [x] -=1 

    if susi_count [x] == 0 :
        distinct -=1
    left +=1 

    y = arr2[right] 
    if susi_count[y] == 0:
        distinct +=1 
    susi_count[y] +=1
    right +=1

    score = distinct + (1 if susi_count[c] ==0  else 0)

    best_case = max(best_case, score)

print(best_case)





