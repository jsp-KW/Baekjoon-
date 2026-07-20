def solution(msg):
    answer = []
    
    # L : 길이가 1인 모든 단어를 포함하도록 사전을 초기화
    # W : 현재 입력과 일치하는 가장 긴 문자열 W를 찾는다
    # C, W+C 에  해당하는 단어를 사전에 등록한다
    
    # KA는 27, -> 11출력
    # AK는 사전 X, A는 1 출력, AK 28 등록
    # KA 27 출력하고
    
    
    dic  = {'A': 1, 'B':2 ,'C':3, 'D': 4, 'E':5 ,'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11,
           
           'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20,'U':21,'V':22,
            'W':23, 'X':24,'Y':25,'Z':26
           }
    
    concat_check = True
    temp = ""
    idx = 27
    
    i=0
    while i< len(msg) :
        
        prev_temp = msg[i]
        
        for j in range (i+1, len(msg)) :
            check_ch = prev_temp + msg[j]
            if check_ch not in dic:
                answer.append(dic[check_ch[:len(check_ch)-1]])
                dic[check_ch] = idx 
                idx+=1
                break
            else:
                prev_temp += msg[j]
        
        else:
            answer.append(dic[prev_temp])
        i= i+ len(prev_temp)
        
    
    
   
        
    return answer