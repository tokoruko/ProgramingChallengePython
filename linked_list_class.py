class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def show_list(self):
        all_next = self.head
        while all_next.next != None:
            print(all_next.value)
            all_next = all_next.next
        print(all_next.value)
        #print(self.head.value)

    def insert(self,value):
        all_next = self.head
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)
#        self.head.next = Node(value)

link = LinkedList(10)
link.insert(5)
link.insert(12)
link.show_list()
