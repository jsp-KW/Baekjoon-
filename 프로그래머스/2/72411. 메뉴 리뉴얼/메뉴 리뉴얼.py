from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    # 최소 2명 이상의 손님으로부터 주문된 단품 메뉴 조합에 대해서만 후보로 포함
    # 각 손님은 2개이상 주문
    
    for c in course :
        candidates = []
        
        for order in orders: 
            order = sorted(order)
            
            for comb in combinations (order, c) :
                candidates.append(''.join(comb))

        counter = Counter(candidates)
        if not counter :
            continue

        max_count = max(counter.values())
        
        for menu,value in counter.items() :
            if max_count >=2 :
                if value == max_count :
                    answer.append(menu)
        
            
                
            
        
    
    return sorted(answer)