def solution(arr, k):
    answer = []
    
    # 나온적이 없는 수라면 배열의 맨 뒤에 추가
    # 완성된 배열의 길이가 k 보다 작으면 나머지 값을 -1로 채워서 return
    # set->list  순서 보장 안됨 주의;;;
    
    arr_set = set()
    
    li = []
    
    for num in arr :
        if num not in arr_set :
            arr_set.add(num)
            li.append(num)

    if len(li) > k :
        li = li[:k] 
    
    if len(li) == k :
        return li
    elif len(li) < k :
        cnt = k - len(li)
        for _ in range (cnt) :
            li.append(-1)
        return li
    

