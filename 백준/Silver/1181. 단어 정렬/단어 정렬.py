N = int(input())

li = []
for i in range(N) :
    str = input()
    li.append(str)

li.sort(key=lambda x: (len(x), x))

result = []
for word in li:
    if word not in result :
        result.append(word)


for word in result:
    print(word)
