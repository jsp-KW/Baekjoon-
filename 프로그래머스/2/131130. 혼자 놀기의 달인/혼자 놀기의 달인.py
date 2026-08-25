from collections import Counter
def solution(cards):
    answer = 1
    # 작거나 같은 숫자카드들을 준비
    # 준비한 카드 수만큼 상자를 만들어
    # 일렬로 나열, 순차적으로 증가하는 번호를 붙인다
    
    box_group = []
    box_visited = [-1] *(len(cards))
    box_num = 1
    
    for i in range (len(cards)) :
        
        if box_visited[i] != -1  :
            continue
            
        cur = i
        while True :
            if box_visited[cur] != -1 :
                break
            box_visited[cur] = box_num
            cur = cards[cur] -1
        
        box_num +=1
    
    counter = Counter(box_visited)
    
    temp_li = list(counter.values())
    temp_li.sort(reverse = True)
    
    if len(counter) <2:
        return 0
    
    answer = temp_li[0]* temp_li[1]
    return answer