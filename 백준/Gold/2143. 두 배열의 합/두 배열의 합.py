import sys

T = int(sys.stdin.readline())
n= int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().split()))
m= int(sys.stdin.readline())
B= list(map(int,sys.stdin.readline().split()))

temp = 0
# 경우의수가 많은데, 이걸 어떻게 경우를 나누지?<- 여기서 막힘..
# 일단 모든 경우를 만듬
# 부분합을 만들자-> 길이가 1,2,3~n

# 이후, 투포인터를 이용해서
# 순서쌍갯수 구하기
# 부분합이 같은경우도 잇기때문에, 그 경우를 세줘야함

#투포인터 진행방향 왼쪽->오른쪽이 보편적

sub_a=[]

for i in range(n):
    sum =0
    for j in range(i,n):
        sum+=A[j]
        sub_a.append(sum)

sub_b =[]

for i in range(m):
    sum =0
    for j in range(i,m):
        sum+=B[j]
        sub_b.append(sum)


ptr_a,ptr_b=0,0
sub_a.sort()
sub_b.sort(reverse=True)
answer =0


temp = 0
while ptr_a < len(sub_a) and ptr_b < len(sub_b):

    s= sub_a[ptr_a]+ sub_b[ptr_b]

    if s ==T:
        a_value = sub_a[ptr_a]
        b_value = sub_b[ptr_b]
        a_cnt =0
        b_cnt =0

        while ptr_a<len(sub_a) and a_value== sub_a[ptr_a]:
            a_cnt+=1
            ptr_a+=1
        
        while ptr_b<len(sub_b) and b_value==sub_b[ptr_b]:
            b_cnt+=1
            ptr_b+=1

        answer+= (a_cnt*b_cnt)
        
    
    elif s<T :
        ptr_a+=1
    else:
        ptr_b+=1
print(answer)

            
