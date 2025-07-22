import sys

T = int(sys.stdin.readline())

# cnt0 =0
# cnt1 =0

# def  fib (n) :
#     if n == 0 :
#         #print("0호출")
#         global cnt0
#         cnt0 +=1
#         return 0
#     elif n == 1 :
#         #print ("1호출")
#         global cnt1
#         cnt1+=1
#         return 1
#     else :
#         return fib(n-1) + fib(n-2)
# answer = []    
# for _ in range (T) :
    
#     test_num = int(sys.stdin.readline())
#     fib (test_num)
#     answer.append(cnt0)
#     answer.append(cnt1)
#     cnt0=0
#     cnt1=0

# for i in range(0,len(answer),2) :
#     print (answer[i], answer[i+1])

cnt0 = [0]*41
cnt1 = [0]*41

cnt0[0], cnt1[0] = 1 , 0
cnt0[1], cnt1[1] = 0,  1


answer = []
for i in range (2,41) :
    cnt0[i] = cnt0[i-1] +cnt0[i-2]
    cnt1[i] = cnt1[i-1] +cnt1[i-2]

for _ in range(T) :
    N = int(sys.stdin.readline())
    answer.append(cnt0[N])
    answer.append(cnt1[N])

for i in range(0, len(answer),2) :
    print(answer[i], answer[i+1])
    

