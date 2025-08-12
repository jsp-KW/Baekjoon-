import sys

class Queue:
    
    def __init__ (self) :
        self.arr = []
    
    def push (self,x) :
        self.arr.append(x)

    
    def pop(self) :
        if self.empty() ==1 :
            return -1
        else: return self.arr.pop(0)
        

    def empty(self) :
        if len(self.arr) ==0 :
            return 1
        else: return 0

    def front(self):
        if self.empty()==1:
            return -1
        else: return self.arr[0]
    
    def back(self):

        if self.empty()==1:
            return -1
        else: return self.arr[-1]

    def size(self) :
        if self.empty() ==1 : return 0
        else: return len(self.arr)


N = int(sys.stdin.readline())

operations = []
for _ in range(N) :
    operation = sys.stdin.readline().rstrip()
    operations.append(operation)

q = Queue()
for op in operations:
    if "push" in op:
        temp = op.split(" ")
        item =int(temp[1])
       
        q.push(item)

    elif op =="front" :
       print(q.front())

    elif op == "back":
        print(q.back())
    
    elif op =="pop" :
       print(q.pop())

    elif op =="empty" :
        print (q.empty())

    elif op =="size" :
        print(q.size())
