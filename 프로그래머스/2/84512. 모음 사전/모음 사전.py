def solution(word):
    
    # 입력 word 가 몇번째 단어인지 출력을 하기 위해선
    # 들어온 word 를 수식으로 
    
    # A 하나 고정할때, 길이가 1,2,3,4,5 일때 각 경우의수는 1+5+25+125+625 =781
    # AA 고정할때, 길이는 0,1,2,3 -> 1+ 5 +25 + 125 =  156 
    # AAA, -> 1+5+25 = 31
    # AAAA -> 1+5 = 6
    # AAAAA -> 1 
    answer = 0
    
    index = [781,156, 31, 6 ,1]
    alpha = ['A','E','I','O','U']
    
    #단어 하나를 꺼낸 후,
    #꺼낸 단어의 인덱스 값으로, index 배열에서의 값을 가져옴
    #그 값과 i값 즉, 길이값을 곱한후, +1
    inner_idx =0
    
    for w in word :
        for i in range (0,len (alpha)) :
            if alpha[i] == w  :
                answer += (index[inner_idx] * i) + 1
                break
        inner_idx+=1

    return answer