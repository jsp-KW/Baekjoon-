def solution(k, ranges):
    answer = []
    x= 0
    y = k
    
    cords = [(0, k)]
    
    def calc (num) :
        if num % 2 ==0 :
            return num//2
        else :
            num = num *3
            num+= 1
            return num
        
            
    
    while k != 1 :
        res_k = calc (k)
        x+=1
        cords.append((x, res_k))
        k = res_k
    
    #[a,b] -> x=a, x=b, y=0 으로 둘러쌓인 공간의 면적
    #
    
    # 11x + 5
    # 11/2x^2 +5x
    # 1,0  11/2 + 10/2  = 21/2 = 10.5
    
    areas=  []
    for i in range (0, len(cords)-1) :
        y1 = cords[i][1]
        y2 = cords[i+1][1]
        
        temp_s = (y2+y1)/2
        areas.append(temp_s)
    
    n = len(cords) -1
    
    for r in ranges : 
        first, second = r
        start = first
        end  = n+ second
        
        if start >end :
            answer.append(-1.0)
            continue
        
        answer.append (sum(areas[start:end]))
        
        
    return answer