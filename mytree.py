# class Node:
#     def __init__(self, key):#,value):
#         self.key = key
#         #self.value = value
#         self.left = None
#         self.right = None

class Tree:
    # def __init__(self):
    #     self.root = None

    def __init__(self,key):
        self.key = key
        #self.value = value
        self.left = None
        self.right = None
    
    def sarchNode(self,key):
        if key > self.key:
            current = self.right
            self.sarchNode(current.key)
        elif key < self.key:
            current = self.left
            self.sarchNode(current.key)
        else:
            return self.key
    
    def addNode(self,key):
        #current = self.key
        #targetKey = current.key
        if  key == self.key :
            pass
        elif key > self.key:
            if self.right == None:
                self.right = Tree(key)
            else:
                current = self.right
                addNode(current.key)
        else: 
            if self.left == None:
                self.left = Tree(key)
            else:
                current = self.left
                addNode(current.key)


    # def sarchNode(self,key):
    #     current = self.root
    #     #targetKey = current.key

    #     while current.key != key:
    #         current.left.key 
    #         current.right.key
    #     return current.key

        # if key > current.key:
        #     current = current.right
        #     sarchNode(current.key)
        # elif key < current.key:
        #     current = current.left
        #     sarchNode(current.key)
        # else:
        #     return current.value
    
    # def addNode(self,key):
    #     current = self.root
    #     #targetKey = current.key
    #     if  key == current.key :
    #         pass
    #     elif key > current.key:
    #         if current.right == None:
    #             current.right = Node(key)
    #         else:
    #             current = current.right
    #     else: 
    #         if current.left == None:
    #             current.left = Node(key)
    #         else:
    #             current = current.left

    #def deleteNoede(self,key):

print("when 0")
tree = Tree(50)
tree.addNode(5)
tree.sarchNode(5)

