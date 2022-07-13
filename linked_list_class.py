class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def getListLength(self):
        self.list_length = 0
        all_next = self.head
        while all_next.next != None:
            list_length += 1
            all_next = all_next.next

        return list_length
    
#    def judgeListPlace(self,place):
#        if place 

    def showList(self):
        all_next = self.head
        all_values = []
        while all_next.next != None:
            all_values.append(all_next.value)
            all_next = all_next.next
        return all_values
        #print(self.head.value) 

    def pushNode(self,value):
        all_next = self.head
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)

    def insertNode(self,place,value):
        all_next = self.head
        node_inserted = Node(value)
        for i in range(place-1):
            all_next = all_next.next
        node_inserted.next = all_next.next
        all_next.next = node_inserted
    
    def deleteNode(self,place):
        all_next = self.head
        for i in range(place-1):
            all_next = all_next.next
        

'''    def showList(self):
        all_next = self.head
        while all_next.next != None:
            print(all_next.value)
            all_next = all_next.next
        print(all_next.value)
        #print(self.head.value) 

    def push(self,value):
        all_next = self.head
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)
                                        '''
#        self.head.next = Node(value)



link = LinkedList(0)
for i in range(4):
    link.pushNode(i+1)
print(link.showList())
print('---')
link.insertNode(0,1.5)
print(link.showList())
