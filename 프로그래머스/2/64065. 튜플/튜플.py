def solution(s):
    answer = []
    
    new_s = s[2:-2]
    
    groups =  new_s.split("},{")
    
    groups.sort(key = len)
    
    
    for sample in groups :
        if ',' in sample :
            temp = sample.split(',')
            for str_n in temp :
                if int(str_n) not in answer:
                    answer.append(int(str_n))
        else:
            if int(sample) not in answer:
                answer.append(int(sample))
    
    
        
    return answer