def solution(message, spoiler_ranges):
    answer = 0
    # 단어는 공백으로 구분
    # 인덱스중 하나 이상이 스포방지구간에 포핟될 경우, 해당 단어는 스포일러 방지 단어
    # 스포 방지 단어
    # 스포 방지 구간이 아닌 구간에 등장한 적이 없어야함
    # 이전에 공개된 스포방지 단어와 중복 x
    # 
    n = len(message)
    spoiler = [False] *(n)
    
    
    for spo in spoiler_ranges :
        start, end= spo [0], spo[1]
        for i in range (start, end+1) :
            spoiler[i] = True 
    

    spoiler_words = set() # 스포 구간에 걸린 단어들을 담는다
    public_words = set() # 스포 구간이 아닌 곳에 나온 단어들을 담는다
    
    
    i=0
    while i< n :
        start = i
        
        # 공백 전 단어 끝 구간 찾기
        while i< n and message[i] != ' ' :
            i+=1 
        
        # 공백구간
        end = i
        is_spo = False  
        target_word = message[start:end]
        
        # spo 구간 하나라도 포함이면 
        for j in range (start, end):
            if spoiler[j]:
                is_spo= True
                break
                
        if is_spo :
            spoiler_words.add (target_word)
            
        else :
            public_words.add(target_word)
        
        i= end +1
        
        
    
    answer = len(spoiler_words - public_words)
    return answer