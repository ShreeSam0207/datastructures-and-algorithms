class Node():
    def __init__(self,data=None,right=None,left=None):
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
        elif data < current_node.data:
            current_node.left=self._insert(current_node.left,data)
        elif data > current_node.data:
            current_node.right=self._insert(current_node.right,data)
        return current_node

    def _delete_root(self):
        if self.root==None:
            print("Tree is empty")
        else:
            self.root=None
    
    def _deletion(self,data):
        if self.root==None:
            print("Tree is empty")
        else:
            self._delete(self.root,data)
    
    def _delete(self,current_node,data):
        if data < current_node.data:
            current_node.left=self._delete(current_node.left,data)
        elif data > current_node.data:
            current_node.right=self._delete(current_node.right,data)
        elif current_node.data==data:
            if current_node.left !=None and current_node.right==None:
                current_node=current_node.left
            elif current_node.right !=None and current_node.left==None:
                current_node=current_node.right
            elif current_node.left!=None and current_node.right!=None:
                max_node=self.find_right_tree_min(current_node.right)
                current_node.data=max_node.data
                self._delete_max_node(current_node.right,max_node)
            else:
                current_node=None
        return current_node
    
    def find_right_tree_min(self,current_node):
        if current_node.left:
            while current_node.left !=None:
               current_node=current_node.left
            return current_node
        else:
            return current_node
    
    def _delete_max_node(self,current_node,max_node):
        if current_node.data==max_node.data:
            current_node=None
        else:
            current_node.left=self._delete_max_node(current_node.left,max_node)
        return current_node

    def print_tree(self):
        if self.root==None:
            print("tree is empty")
        else:
            self._print(self.root)
    
    def _print(self,current_node):
        if current_node.left!=None:
            self._print(current_node.left)
        print(str(current_node.data),end=" ")
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
    b._deletion(2)
    # b._delete_root()
    b.print_tree()
                      
        
        