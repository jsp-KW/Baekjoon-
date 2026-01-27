def solution(number, k):
    answer = ''
    # 어떤숫자에서 k개의 수를 제거했을때, 얻을 수 있는 가장 큰 숫자를 구하자
    stack = []
    # 현재 수보다 크거나 같으면 넣고
    
    for num in number :
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k-=1
        stack.append(num)
        
    if k >0 :
        stack = stack [:k+1]
    for s in stack :
        answer+=s
    
    return answer