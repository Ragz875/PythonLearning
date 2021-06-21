class Stack:
    def __init__(self):
        print('Stack Init is invoked')
        self.sarr=[]

    def push(self,item):
        self.sarr.append(item)

    def pop(self):
        if len(self.sarr) == 0 :
            print('Stack is empty, nothing is to delete')
            return
        del self.sarr[-1]
    def display(self):
        if len(self.sarr) > 0 :
            i=len(self.sarr)-1
            while i >= 0 :
                print(self.sarr[i])
                i-=1

s=Stack()
print(s.sarr)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.pop()
s.pop()
s.display()



