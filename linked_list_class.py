class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def getListLength(self):
        list_length = 0
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
        all_values.append(all_next.value)
        return all_values
       #print(self.head.value) 

    def pushNode(self,value):
        all_next = self.head 
        while all_next.next != None:
            all_next = all_next.next
        all_next.next = Node(value)

    def insertNode(self,place,value):
        all_next = self.head
        list_length = self.getListLength()
        node_inserting = Node(value)
#        print(value)
#        print(node_inserting.value)
        if place == 0 :
            node_inserting.next = all_next
            
            self.head = node_inserting

        elif (place < 0) or (place > list_length):
            for i in range(list_length):
                print(all_next.value)
                all_next = all_next.next
            print(all_next.value)
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
            all_next = all_next.next
        all_next.next = all_next
        

    # def showList(self):
    #     all_next = self.head
    #     while all_next.next != None:
    #         print(all_next.value)
    #         all_next = all_next.next
    #     print(all_next.value)
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
link.insertNode(2,1)
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
# #print(link.showList())
# #insert to last
# link.insertNode(100,8)
# print(link.showList())
# print('---')
# #insert to last
# link.insertNode(-5,12)
# print(link.showList())
# #print(link.showList())
