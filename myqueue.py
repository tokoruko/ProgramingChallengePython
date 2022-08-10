class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        self.head = Node(value)


    def getQueueLength(self):
        queue_length = 0
        if self.head==None:
            return queue_length

        queue_length +=1
        current = self.head
        if current.next == None:
        #    queue_length=1
            return queue_length
        while current.next != None:
            queue_length += 1
            current = current.next
        return queue_length
    
    def enqueueValue(self,value):
        head_node=Node(value)
        head_node.next = self.head
        self.head = head_node
    
    def dequeue(self):
        if self.getQueueLength()==1:
            element = self.head.value
            self.head = None
        else :
            current = self.head 
            for i in range(self.getQueueLength()-2):
                current = current.next
            element = current.next.value
            
            del current.next
            current.next = None
        return element

    def getValue(self):
        current = self.head
        if self.getQueueLength()==0:
            return
        while current.next != None:
            current = current.next
        element = current.value
        return element
print("when only one element")
queue = Queue(0)
print("get value 0")
print(queue.getValue())
print("dequed element is none")
queue.dequeue()
print(queue.getValue())
print("enqueue when element is none")
for i in range(4):
    queue.enqueueValue(i+1)
print(queue.getValue())
print('---')
print("enqueueValue 10")
queue.enqueueValue(10)
print(queue.getValue())
print('dequeue\ndequed value is expected 1')
print(queue.dequeue())
print('get value expected 2')
print(queue.getValue())

