class Node():
    def __init__(self,data=None,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
class BinaryTree():
    def __init__(self):
        self.root=None
    
    def _insertion(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._insert(self.root,data)
    
    def _insert(self,current_node,data):
        q=[]
        new_node=Node(data)
        q.append(current_node)
        while q:
            p=q.pop(0)
            if p.left:
                q.append(p.left)
            else:
                p.left=new_node
                break
            if p.right:
                q.append(p.right)
            else:
                p.right=new_node
                break
       
    
    def print_tree(self):
        if self.root==None:
            print("tree is empty")
        else:
            self._print(self.root)
    
    def _print(self,current_node):
        if current_node.left!=None:
            self._print(current_node.left)
        print(str(current_node.data),end=" "),
        if current_node.right!=None:
            self._print(current_node.right)

if __name__=="__main__":
    b=BinaryTree()
    b._insertion(5)
    b._insertion(1)
    b._insertion(2)
    b._insertion(3)
    b._insertion(4)
    b._insertion(6)
    b.print_tree()
            
                    
                    