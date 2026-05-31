def solution(files):
    answer = []
    
    # head 부분으로 먼저 정렬 대소문자 구분 x
    # 숫자부분 차이로
    # 숫자마저도 같으면 원래 입력에 주어진 순서를 유지
    answer=[]
    order_idx = 0
    numbers =[]
    for f in files :
        for i in range (0, len(f)) :
            if f[i].isdigit() : #숫자부분 찾기
                head = f[:i]
                
                number = ""
                for j in range (i, len(f)):
                    if f[j].isdigit() :
                        number+= f[j]
                    else:
                        break
                numbers.append((head.lower(), int(number), order_idx, f))
                order_idx +=1
                break

    numbers.sort(key = lambda x: (x[0],x[1],x[2]))
    
    for tup in numbers :
        answer.append(tup[3])
    return answer