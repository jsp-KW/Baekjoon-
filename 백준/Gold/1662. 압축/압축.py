s = input().strip()
stack = []

for i in range(len(s)):
    if s[i] == '(':
        #123(12) 인 경우, stack= [1,1,1] 상태였는데
        #[1,1] 이 되고, 이후, [1,1,3], 그리고 [1,1,3,'(']이 됨

        stack.pop()
        stack.append(int(s[i - 1]))
        stack.append(s[i])


        # 이후 [1,1,3,'(',1,1]에서 ')' 을 만나게 된다.
    elif s[i] == ')':
      
        inside_len = 0
        while True:
            temp = stack.pop()
            if temp == '(':
                break
            inside_len += temp # 1,1 두개 즉 2가 저장
     
        repeat_count = stack.pop() # stack =[1,1,3] 에서 3이 pop 되어 저장
        stack.append(inside_len * repeat_count) #  stack = [1,1,6]

    else:
        # 일반 문자일 경우 스택에 1을 추가하기
        stack.append(1)

# 스택에 남아 있는 모든 값들을 더해서 결과 출력 
# stack =[1,1,6] 이므로, 1+1+6 =8 출력
total_length = sum(stack)
print(total_length)
