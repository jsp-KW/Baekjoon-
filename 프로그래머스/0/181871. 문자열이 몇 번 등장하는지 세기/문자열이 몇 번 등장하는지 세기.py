def solution(myString, pat):
    answer = 0
    

    for i in range(0, len(myString) - len(pat) +1) :
        check = myString[i:i+len(pat)]
        if check ==pat :
            answer+=1
            
    return answer