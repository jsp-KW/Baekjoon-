import sys

# 0~9 까지 한 세트
num_sets = [0]*(10)


inputs = sys.stdin.readline().rstrip("\n")

for n in inputs :
    num = int(n)
    num_sets [num] += 1

num_sets [6] = (num_sets[6] + num_sets[9]+1  ) //2
num_sets[9] = 0
print (max(num_sets))

  
