class Node:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def sarchNode(self,key):
        current = 
        targetKey = current.key
        if key > current.key:
            current = current.right
            sarchNode(current.key)
        elif key < current.key:
            current = current.left
            sarchNode(current.key)
        else:
            return current.value
    
    def addNode(self,key):
        current = self.root
        #targetKey = current.key
        if  key == current.key :
            pass
        elif key > current.key:
            if current.right == None:
                current.right = Node(key)
            else:
                current = current.right
        else: 
            if current.left == None:
                current.left = Node(key)
            else:
                addNode(key)

    def deleteNoede(self,key):
