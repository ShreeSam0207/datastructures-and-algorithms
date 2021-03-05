class Node():
    def __init__(self,data=None,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
class BinarySearchTreeTraversal():
    def __init__(self):
        self.root=None
    
    def _insertion(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
    
    def _insert(self,current_node,data):
        new_node=Node(data)
        if current_node==None:
            current_node=new_node
        elif data < current_node.data:
            current_node.left=self._insert(current_node.left,data)
        elif data > current_node.data:
            current_node.right=self._insert(current_node.right,data)
        return current_node

    def inorder_traversal(self):
        if self.root==None:
            print("Tree is emoty")
        else:
            self._inorder_print(self.root)
            
    def _inorder_print(self,current_node):
        if current_node.left!=None: 
            self._inorder_print(current_node.left)
        print(str(current_node.data),end=" ")
        if current_node.right!=None:
            self._inorder_print(current_node.right)
    
    def preorder_traversal(self):
        if self.root==None:
            print("Tree is emoty")
        else:
            self._preorder_print(self.root)
    
    def _preorder_print(self,current_node):
        print(str(current_node.data),end=" ")
        if current_node.left!=None:
            self._preorder_print(current_node.left)
        if current_node.right!=None:
            self._preorder_print(current_node.right)
            
    def postorder_traversal(self):
        if self.root==None:
            print("Tree is emoty")
        else:
            self._postorder_print(self.root)
    
    def _postorder_print(self,current_node):
        if current_node.left!=None:
            self._postorder_print(current_node.left)
        if current_node.right!=None:
            self._postorder_print(current_node.right)
        print(str(current_node.data),end=" ")
        
if __name__=="__main__":
    b=BinarySearchTreeTraversal()
    b._insertion(10)
    b._insertion(5)
    b._insertion(15)
    b._insertion(2)
    b._insertion(6)
    b._insertion(18)
    b._insertion(12)
    b._insertion(24)
    print("-----In order traversal")
    b.inorder_traversal()
    print("\n")
    print("-----Pre order traversal")
    b.preorder_traversal()
    print("\n")
    print("-----Post order traversal")
    b.postorder_traversal()