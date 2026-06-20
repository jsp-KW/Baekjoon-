def solution(s):
    answer = 0
    
    # (), {},[]
    # 0 ~ s의 길이-1 씩 옮기면서 따진다
    # 올바른 괄호 문자열일 경우 개수 +1
    
    cnt = len(s)

    # 첫번째 경우 체크
    
    put = ['{', '[', '(']
    get = ['}', ']', ')']
    
    
    def check (target) :
        stack = [] 

        for t in target :
            if t in put :
                stack.append(t)

            else:
                if t in get and stack :
                    if stack[-1] == put[get.index(t)] :
                        stack.pop()
                    else :
                        stack.append(t)
                else :
                    stack.append(t)

        if not stack :
            return True

    

    # 두번째부터 끝까지 체크
    for i in range (0, cnt) :
        target = s[i:] + s[:i]
        if check(target) :
            answer +=1

    return answer