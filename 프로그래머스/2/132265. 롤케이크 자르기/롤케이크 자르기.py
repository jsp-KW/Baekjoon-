from collections import Counter
def solution(topping):
    answer = 0
    # 토핑 가짓수가 동일하게 올라간다면 공평하게 나뉘어진거로 생각한다
    # 잘라서, set 으로 만들고 교집합을 제외한 나머지 토핑 종류의 개수가 같으면 공평한것
    
    left = set()
    right = Counter (topping)
    
    for t in topping :
        left.add (t)
        right[t] = right [t] -1 
        
        if right[t] == 0 :
            del right[t]
        
        if len(left) == len(right) :
            answer +=1 
            
    return answer