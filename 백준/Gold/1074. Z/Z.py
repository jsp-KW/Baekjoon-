#  2 x 2

# n =1
# x x
# x x

#  n =2
# x x x x
# x x x x
# x x x x
# x x x x


#  한줄 입력받는거
n, r, c = map (int, input().strip().split())

# 4등분해야하므로 섹터를 나눠야함..
# 4 x 4 인 경우를 보면
# 왼쪽 그리드 범위는  0~ 2^n  -1 이고
# 오른쪽 그리드 범위는 2^n-1 이상인 경우(열)
# 왼쪽 아래 그리드 범위 2^n-1 이상인 경우 (행)
# 오른쪽 아래 그리드 범위는 2^n-1 이상인 경우 행과 열 모두

def find(n, r, c) :

    # size 가 1인 경우
    if n ==0 :
        return  0
    
    half_size =  2**(n-1)

    #왼쪽 그리드 범위

    if r < half_size and c <half_size:
       return find(n-1, r, c)
    # 오른쪽 그리드 범위
    elif c >=half_size and r < half_size:
        return half_size*half_size + find(n-1, r, c-half_size)

    # 왼쪽 아래 범위

    elif r>=half_size and c < half_size:
        return  2 * (half_size*half_size) +  find (n-1, r-half_size, c)
     
    # 오른쪽 아래 범위
     
    else :
        return 3*(half_size*half_size) +  find (n-1, r-half_size, c- half_size)
    
print (find (n,r,c))


    
