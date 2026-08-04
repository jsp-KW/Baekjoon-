def solution(cacheSize, cities):
    answer = 0
    # 캐시 사이즈에 따른 실행시간 측정 프로그램 작성
    # 총 실행시간
    
    # LRU
    # A B C 
    # 가장 마지막에 사용한거 앞으로 빼고, 새로들어온건 뒤로 넣기
    
    # 대소문자 구문 없애기

    
    # hit 일경우 1
    # miss 일 경우 5
    
    new_arr = []
    for city in cities:
        new_arr.append(city.lower())
        
    
    def LRU (size, arr) :
        
        total_time = 0
        buffer = []
        
        if size ==0 :
            return 5 * len(arr)
        
        for city in arr :
            if city in buffer :
                total_time += 1
                buffer.remove(city)
                buffer.append(city)
            else:
                total_time += 5
                if len(buffer) <size :
                    buffer.append(city)
                else:
                    buffer= buffer[1:]
                    buffer.append (city)
        
        return total_time
    
    answer=  LRU(cacheSize, new_arr)        
                
                
    return answer