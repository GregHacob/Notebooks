from binarytree import BinaryTree, Node

class BST(BinaryTree):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False
        
    def populateBSTfromMatrix(self, T):
        self.T = T
        if len(T) > 1:
         self.addNode(self.root.value)
    
    def addNode(self, r):
        for i in range(len(self.T[r])):
         if self.T[r][i] == 1:
          node = Node(i)
          self.insert(node.value)
          self.addNode(i)
          
    
        