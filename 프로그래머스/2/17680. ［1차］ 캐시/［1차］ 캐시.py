def solution(cacheSize, cities):
    answer = 0
    # 캐시 사이즈에 따른 실행시간 측정 프로그램 작성
    # 총 실행시간
    
    # LRU
    # A B C 
    # 가장 마지막에 사용한거 앞으로 빼고, 새로들어온건 뒤로 넣기
    
    # 대소문자 구문 없애기
    new_arr= []
    for city in cities: 
        new_arr.append(city.lower())
        
    
    def LRU(size, arr) :
        
        if size == 0 :
            return len(arr)*5
        
        buffer = []
        time = 0
        cnt = 0
        for city in arr :
            if city in buffer:  
                buffer.remove(city)
                buffer.append(city)
                time +=1
            else: # miss
                if len(buffer) == size : 
                    buffer = buffer[1:size]
                    buffer.append(city)
                else:
                    buffer.append(city)
                    
                time+=5
                
        return time
    
    answer = LRU(cacheSize,new_arr)
        
    return answer