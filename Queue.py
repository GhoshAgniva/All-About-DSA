class Queue:
    def __init__(self):
        self.value = []
    def enqueue(self,x):
        self.value.append(x)
    def dequeue(self):
        front = self.value[0]
        self.value = self.value[1:]
        return front

#Inputs
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print(q.value)
q.dequeue()
print(q.value)
