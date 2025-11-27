import sys

sentence  = list(sys.stdin.readline().rstrip()) # list로 바꾸고


skip = 0
# slice 대입은 우측이 iterable
# skip을 이용하여 이미 처리한 부분을 건너띔
# 0 부터 시작이므로 인덱스는, skip 값 초기화시 -1 해서 설정
for i in range(len(sentence)) :

    if skip >0 :
        skip -= 1
        continue
    
    inner_len = 0
    for idx in range(i, len(sentence)):
        if sentence[idx] == 'X':
            inner_len+=1

        else:
            break

    if inner_len == 0:
        continue
    
    if inner_len ==4 :
        sentence[i:i+4] = list('AAAA')
        skip = 3
        continue
  
    elif inner_len ==2 :
    
        sentence[i:i+2] = list('BB')
        skip =1
    
    elif inner_len %2==1 :
        print (-1)
        exit()
    else :
        A_size = inner_len // 4
        B_size = (inner_len%4)//2
        replace = 'AAAA' * A_size + 'BB' * B_size
       
        sentence[i:i+inner_len] = list(replace)
        skip = inner_len -1
    
    

print(''.join(sentence)) # list ->str로 변환

    