#Stack Using List
class Stack:
    def __init__(self):
        self.value = []
    def push(self,x):
        self.value = [x] + self.value
    def pop(self):
        return self.value.pop(0)

#Inputs

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.value)
s.pop()
print(s.value)