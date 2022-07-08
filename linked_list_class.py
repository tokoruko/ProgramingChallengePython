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
    
'''    def judgeListPlace(self,place):
        
        if place'''

    def showList(self):
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
#        self.head.next = Node(value)

    def insert(self,place,value):
        all_next = self.head
        while


link = LinkedList(10)
link.push(5)
link.push(12)
link.showList()
