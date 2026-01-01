import sys


N, L= map (int, sys.stdin.readline().split())

# 합이 N, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수리스트
# L 이 최대 100까지

# x, x+1 ,x+2 ,  ... x+k-1   (2x +k -1 ) k//2
# 2xk + k^2 -k /2  = N 
# 2N = KK -K +2KX
# 2N- K*K +K / 2K = X
# (2N-K*K +K) /2K = X
for k in range (L, 101) :
   numer = 2*N -k*k +k 
   denom = 2*k

   
   if numer < 0 :
      break
   
   if numer % denom  !=  0 :
      continue
   
   x = numer // denom

   print (*[x+ i for i in range (k)])
   sys.exit()

print (-1)




      