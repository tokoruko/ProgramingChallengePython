class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
#        self.head = None
    def getListLength(self):
        list_length = 0
        all_next = self.head
        while all_next.next != None:
            list_length += 1
            all_next = all_next.next

        return list_length
    
#    def judgeListPlace(self,place):
#        if place 

    # def showList(self):
    #     all_next = self.head
    #     all_values = []
    #     while all_next.next != None:
    #         all_values.append(all_next.value)
    #         all_next = all_next.next
    #     all_values.append(all_next.value)
    #     return all_values
       #print(self.head.value) 
    def enqueue(self,value):
        head_node=Node(value)
        head_node.next = self.head
        self.head = head_node
    
    def dequeue(self): #今回の実装だとpopにもなる
        all_next = self.head
        #while all_next.next != None:
        for i in range(self.getListLength()-1):
            all_next = all_next.next
        element = all_next.next.value
        all_next.next = None
        return element
        #del all_next
        #return value

    def pushNode(self,value):
        all_next = self.head 
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)

    def insertNode(self,place,value):
        all_next = self.head
        list_length = self.getListLength()
        node_inserting = Node(value)
        if place == 0 :
            node_inserting.next = all_next
            
            self.head = node_inserting

        elif (place < 0) or (place > list_length):
            for i in range(list_length):
                all_next = all_next.next
            all_next.next = node_inserting

        else:
            for i in range(place-1):
                all_next = all_next.next
            node_inserting.next = all_next.next  
            all_next.next = node_inserting

#途中
    def deleteNode(self,place):
        all_next = self.head
        for i in range(place-1):
            #node_connect = all_next
            all_next = all_next.next
        node = all_next.next
        node = node.next
        del all_next.next
        all_next.next = node
#        all_next.next = all_next.next.next
#メモリから削除したいけどどうやって渡せば？
#ループしてる        all_next.next = all_next
# 変数を消すだけになってる       node_connect = all_next.next
#        del all_next

#getval
    def getValue(self):
        all_next = self.head
        while all_next.next != None:
            all_next = all_next.next
        element = all_next.value
        return element
        
        
       # all_next

    def showList(self):
        all_next = self.head
        while all_next.next != None:
            print(all_next.value)
            all_next = all_next.next
        print(all_next.value)
        #print(self.head.value) 
'''
    def push(self,value):
        all_next = self.head
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)
                                        '''
#        self.head.next = Node(value)


#origin list
link = LinkedList(0)
for i in range(4):
    link.pushNode(i+1)
print(link.showList())
print(link.getListLength())
print('---')
# insert to 0
link.insertNode(2,1.5)
print(link.showList())
print(link.getListLength())
print('---')
#insert to last
link.insertNode(100,101)
print(link.showList())
print(link.getListLength())
print('---')
#insert to last
link.insertNode(-5,10)
print(link.showList())
print(link.getListLength())
print("---")
#link.deleteNode(2)
link.showList()
print("---")
print("enqueue 9")
link.enqueue(9)
link.showList()
print('dequeue\ndequed value')
print(link.dequeue())
print('list')
link.showList()
print("---\n" + "delete")
link.deleteNode(2)
link.showList()
print('get value expected 101')
print(link.getValue())
# #print(link.showList())
# #insert to last
# link.insertNode(100,8)
# print(link.showList())
# print('---')
# #insert to last
# link.insertNode(-5,12)
# print(link.showList())
# #print(link.showList())
