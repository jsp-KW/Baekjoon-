def solution(s):
    answer = 0
    
    # (), {},[]
    # 0 ~ s의 길이-1 씩 옮기면서 따진다
    # 올바른 괄호 문자열일 경우 개수 +1
    
    cnt = len(s)
    
    put = ["(", "[", "{"]
    get = [")","]","}"]
    
    def check_right (target) :
        stack = []
        for ch in target :
            if ch in put :
                stack.append(ch)
            else:
                if stack and stack[-1] == put[get.index(ch)] :
                    stack.pop()
                else:
                    return False
        
        if not stack :
            return True
        else :
            return False
        
    
    for i in range (cnt) :
        left= s[0:i]
        right = s[i:]
        temp = right + left
        check_res = check_right (temp)
        if not check_res :
            continue
        else:
            answer +=1


    return answer