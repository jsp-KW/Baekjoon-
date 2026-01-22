import sys

# 원소를 거꾸로 뒤집고, 오름차순 정렬
# 원소를 뒤집었을때 0이 앞에 선행되는 경우 0 생략


temp = sys.stdin.read().split()
n = int(temp[0])
data = temp[1:n+1]
answers = []


for target in data :
    rev = int(target[::-1])
    answers.append(rev)



answers.sort()
for ans in answers :
    print(ans)