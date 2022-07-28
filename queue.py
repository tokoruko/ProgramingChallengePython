class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        self.head = Node(value)


    def getQueueLength(self):
        list_length = 0
        current = self.head
        while current.next != None:
            list_length += 1
            current = current.next

        return list_length
    
    def enqueueValue(self,value):
        head_node=Node(value)
        head_node.next = self.head
        self.head = head_node
    
    def dequeue(self):
        current = self.head
        for i in range(self.getQueueLength()-1):
            current = current.next
        element = current.next.value
        del current.next
        current.next = None
        return element

    def getValue(self):
        current = self.head
        while current.next != None:
            current = current.next
        element = current.value
        return element

queue = Queue(0)
for i in range(4):
    queue.enqueueValue(i+1)
print(queue.getValue())
print('---')
print("enqueueValue 10")
queue.enqueueValue(10)
print(queue.getValue())
print('dequeue\ndequed value is expected 0')
print(queue.dequeue())
print('get value expected 1')
print(queue.getValue())

