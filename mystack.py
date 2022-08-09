class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        self.head = Node(value)
#        self.head = None

    def getStackLength(self):
        stack_length = 0
        if self.head==None:
            return stack_length

        stack_length +=1
        current = self.head
        if current.next == None:
        #    stack_length=1
            return stack_length
        while current.next != None:
            stack_length += 1
            current = current.next
        return stack_length

    def pushValue(self,value):
        if self.getStackLength()==0:
            self.head = Node(value)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(value)
    
    def popValue(self): 
        #if self.head == None:
        #    return
        if self.getStackLength()==1:
            element = self.head.value
            self.head = None
            #del self.head
            #self.head = Node(None)
        else :
            current = self.head 
            for i in range(self.getStackLength()-1):
                current = current.next
            element = current.next.value
            del current.next
            current.next = None
        return element

#getval
    def getValue(self):
        current = self.head
        if self.getStackLength()==0:
            return
        while current.next != None:
            current = current.next
        element = current.value
        return element

#origin list
print('When only one Node')
stack = Stack(0)
#print(stack.getStackLength())
print(stack.getValue())
print(stack.popValue())
#print(stack.head is None)
print(stack.getValue())
stack.pushValue(0)
#print(stack.head is None)
print(stack.getValue())
print(stack.getStackLength())
print('----')
for i in range(4):
    stack.pushValue(i+1)
    print(stack.getValue())
    #print(stack.getStackLength())
print('---')
print('get value expected 4')
print(stack.getValue())
print('push 10')
stack.pushValue(10)
print(stack.getValue())
print(stack.getStackLength())
print('popped value is expected 10 ')
print(stack.popValue())
print(stack.getStackLength())
print('last value after popped ')
print(stack.getValue())