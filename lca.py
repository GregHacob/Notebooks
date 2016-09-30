 # A recursive python program to find LCA of two nodes n1 and n2    
class LCA(object):
    def __init__(self, BST, n1, n2):
        self.BST = BST
        self.node1 = n1
        self.node2 = n2      
        
    def findLCA(self):
        # Base Case
        if self.BST.root is None:
           return None
        return self.findLCA_helper(self.BST.root)  
     
    def findLCA_helper(self, node):
        # If both n1 and n2 are smaller than root, then LCA
        # lies in left
        if(node.value > self.node1 and node.value > self.node2):
            return findLCA_helper(node.left)
     
        # If both n1 and n2 are greater than root, then LCA
        # lies in right 
        if(node.value < self.node1 and node.value < self.node2):
            return findLCA_helper(node.right)
     
        return node.value