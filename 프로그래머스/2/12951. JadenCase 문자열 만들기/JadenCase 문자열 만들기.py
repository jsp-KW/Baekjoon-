def solution(s):
    answer = ''
    
    
    # 모든 단어의 첫 문자가 대문자
    # 그 외는 소문자인 문자열
    # 첫문자가 알파벳이 아닐때 이어지는 알파벳은 소문자로
    
    
    words = s.split(" ")
    jump_space = 0
    
    for word in words : 
        if word  == "" :
            answer += ""
        elif not word[0].isalpha()  :
            answer+= word[0] 
            answer+= word[1:].lower()
        else:
            answer+= word[0].upper()
            answer+= word[1:].lower()
            
        if jump_space < len(words)-1  :
            answer += ' '
        
        jump_space +=1
    return answer