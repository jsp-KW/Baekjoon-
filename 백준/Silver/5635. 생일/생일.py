import sys

n = int(sys.stdin.readline())

students = []

for _ in range (n) :
    name, day, month, year = map(str,sys.stdin.readline().split())
    students.append((name, int(day), int(month), int(year)))


students.sort(key = lambda x : (x[3],x[2],x[1]))

print(students[n-1][0])
print(students[0][0])