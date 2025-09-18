import sys

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = []
# x,x+d,x+2d,x+3d,x+4d 가 끝

#k=2 ->  x,x+d= 2x+d 
#k=3 -> x,x+d,x+2d = 3(x+d) : 3의 배수
#k=4 -> x,x+d,x+2d,x+3d = 4x +6d =2(2x+3d)  :짝수
#k=5 -> x,x+d,x+2d,x+3d,x+4d =5x+10d =5(x+2d) :5의 배수

# 위 식 일반화 -> kx +k(k-1)/2 *d

#k =2 -> 1,1 대입하면, 3
#k= 3 -> 1,1 대입, 6
#k= 4 -> 1,1 대입 10
#k= 5 -> 15
# 합의 최소값 -> 첫항이 1이고, 공차가 1인경우 -> k +k(k-1)/2

min_value = k + (k*(k-1))//2

# [1,n] 까지의 m의 배수 개수 -> n //m
# [start,n] 까지의 m의 배수 개수를 세고 싶으므로, [1,n] 구간의 m의 배수 개수 - [1,start-1]구간의 m의 배수개수를 빼준다

def counts(l,r,m,min_val) :
    start_count_val = max(l,min_val)
    if start_count_val>r :
        return 0
    return r//m - (start_count_val-1)//m

# max를 쓰는 이유 -> l이 최소 합 보다 작은 경우,
# 만약 최소합이 l보다 작으면, l부터 시작해야하므로
if k == 2:
    print(max(0, r - max(l, min_value) + 1)) # l부터 수 구하면 됨,0 이 나오는건 최소합보다 r이 작은경우
elif k == 3:
    print(counts(l, r, 3, min_value)) # 3의배수

elif k == 4:
    # k=4는 10,14,18에서 시작해 6씩 증가하는 세 가지 수열
    start = max(l, min_value)
    if start > r:
        print(0)
    else:
        cnt = 0
        for base in (10, 14, 18):
            if base > r:
                continue
            first = max(start, base)
            offset = (base - first) % 6
            first += offset
            if first <= r:
                cnt += (r - first)//6 + 1
        print(cnt)
elif k == 5:
    print(counts(l, r, 5, min_value)) #5의 배수