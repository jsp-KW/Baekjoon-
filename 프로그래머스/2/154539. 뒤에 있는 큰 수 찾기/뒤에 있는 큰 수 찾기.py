def solution(numbers) :
    answer = [-1] *(len(numbers))
    stack = []
    
    # 현재 스택에 자기보다 작거나 같은 숫자는 pop
    # 스택에 원소가 있다면 마지막 원소가 해당 인덱스 숫자의 가장 큰 숫자
    # 스택에 추가
    
    
    
    for i in range (len(numbers) -1, -1, -1) :
        while stack and stack[-1] <= numbers[i] :
            stack.pop()
        
        if stack :
            answer[i] = stack[-1]
        
        stack.append(numbers[i])
        
    return answer
        
    