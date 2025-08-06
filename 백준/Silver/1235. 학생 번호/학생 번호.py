import sys
students= []
N = int(sys.stdin.readline())

length = 0
for _ in range(N) :
    student_num = sys.stdin.readline().rstrip()
    students.append(student_num)

length = len(students[0])
for i in range (1,length+1) :
    check = set()

    for s in students :
        check.add(s[-i:])
    if len(check) == N :
        print(i)
        break