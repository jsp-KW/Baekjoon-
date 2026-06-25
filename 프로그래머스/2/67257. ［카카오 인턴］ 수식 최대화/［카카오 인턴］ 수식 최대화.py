from itertools import permutations 

def solution(expression):
    answer = 0
    
    op_order= []
    nums =[]
    
    temp = ""
    for ch in expression :
        
        if ch in ['+','-','*'] :
            op_order.append(ch)
            nums.append(int(temp))
            temp =""
        else:
            temp+= ch
    
    nums.append(int (temp))
    # 숫자만 저장
    # 연산자만 저장
    
    candidates = []  # 연산자 후보
    op = list (set(op_order))
    
    for per in permutations (op):
        candidates.append(per)
    
    # answer = candidates 의 원소의 order 순서대로 계산해서 abs 값이 큰 놈
    # 연산자 우선순위 후보대로 계산해서 최대값 찾기
    
    for use_this_op in candidates :
 
        calc_result =0
        copy_nums = nums[:]
        copy_ops = op_order[:]
        # use_this_op 는 연산자 우선순위
        # op 배열에서 idx 를 찾아서, idx, idx+1 인 숫자들을 해당연산
       
        for target_op in use_this_op :
            process_cnt = copy_ops.count(target_op) #해당 연산자 개수
            num_idx =0
            while process_cnt >0 :
              
                if copy_ops[num_idx]  == target_op :# 같으면
                    num1 = copy_nums[num_idx]
                    num2 = copy_nums[num_idx+1]
                    if target_op == '+' :
                        res = num1+num2
                    
                    elif target_op =='-':
                        res = num1 - num2
                        
                    elif target_op =='*':
                        res = num1 * num2
                    
                    process_cnt -=1  # 계산횟수 감소
                    copy_nums[num_idx] =res #100 + 200 고 num_idx 가 0 이라면, 300을 num_idx 저장 300 200/num_idx+1 pop?
                    copy_nums.pop(num_idx+1) #오른쪽 제거
                    copy_ops.pop(num_idx)
                    
                    
                else:
                    num_idx+=1
        answer = max (answer, abs(copy_nums[0]))       
    
    return answer
