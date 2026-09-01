def solution(myString, pat):
    answer = ''
    
    for i in range (0, len(myString)- len(pat) +1) :
        target = myString[i:i+len(pat)]
        if target == pat :
            answer = myString[0 : i + len(pat)]     
    return answer