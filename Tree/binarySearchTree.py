class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
    
class BinarySearchTree():
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
        elif data<current_node.data:
            current_node.left=self._insert(current_node.left,data)
        elif data>current_node.data:
            current_node.right=self._insert(current_node.right,data)
        return current_node
    
    def print_tree(self):
        if self.root==None:
            print("Tree is empty")
        else:
            self._print(self.root)
    
    def _print(self,current_node):
        if current_node.left!=None:
            self._print(current_node.left)
        print(str(current_node.data),end= " ")
        if current_node.right!=None:
            self._print(current_node.right)
            

if __name__=="__main__":
    b=BinarySearchTree()
    b._insertion(10)
    b._insertion(5)
    b._insertion(15)
    b._insertion(2)
    b._insertion(6)
    b._insertion(18)
    b._insertion(12)
    b._insertion(24)
    b.print_tree()
                        