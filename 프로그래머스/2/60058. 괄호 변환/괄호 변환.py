def solution(p):
    temp = ''
    
    # () 의 개수만 맞으면 균형 잡힌 괄호 괄호
    # () 개수 + 짝이 맞으면 올바른 괄호
    
    def split_uv (s) :
        left =0
        right =0
        
        for i in range (len(s)):
            if s[i] == '(' :
                left +=1
            else :
                right +=1
            if left == right :
                u = s[:i+1] # 균형 잡힌 괄호 문자
                v = s[i+1:]
                return u,v
    def check(s) :
        stack = []
        
        for ch in s :
            if ch == '(' :
                stack.append(ch)
            else :
                if not stack :
                    return False
                stack.pop()
        
        return len(stack) == 0
    
    
    def convert(s) :
        if not s :
            return ""
        
        u,v = split_uv(s)
        
        # 3단계 올바른 괄호 문자열인지 검사
        if check(u) :
            return u + convert(v)
        else:
            temp = "("
            temp += convert(v)
            temp += ")"
            
            for ch in u[1:-1] :
                if ch == ')' :
                    temp += '('
                else :
                    temp += ')'
            return temp
        
    return convert(p)

