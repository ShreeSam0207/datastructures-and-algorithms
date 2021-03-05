class Node():
    def __init__(self,data=None,right=None,left=None):
        self.data=data
        self.right=right
        self.left=left
class BinaryTree():
    def __init__(self):
        self.root=None
        
    def _insertion(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
        else:
            q=[]
            q.append(self.root)
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
    
    def _deletion(self,data):
        if self.root==None:
            print("Tree is empty")
        else:
            max_data=self.find_max_depth()
            self._delete(max_data,self.root,data)
            self._delete_max_node(max_data)

    
    def _delete(self,max_data,current_node,data):
            if current_node.data==data:
                current_node.data=max_data
                return 
            if current_node.left!=None:
                self._delete(max_data,current_node.left,data)
            if current_node.right!=None:
                self._delete(max_data,current_node.right,data)
            
            
    def _delete_max_node(self,max_data):
        current_node=self.root
        q=[]
        q.append(self.root)
        child='left'
        while q:
            p=q.pop(0)
            if p.left:
                q.append(p.left)
                child='left'
            if p.right:
                q.append(p.right)
                child='right'
            else:
                if child=='left':
                    p.left=None
                else:
                    p.right=None
                
                 
    def find_max_depth(self):
        q=[]
        q.append(self.root)
        max_node=self.root
        while q:
            p=q.pop(0)
            if p.left:
                max_node=p.left
                q.append(p.left)
            if p.right:
                max_node=p.right
                q.append(p.right)
            else:
                return max_node.data
            
    def print_tree(self):
        if self.root==None:print("tree is empty")
        else: self._print(self.root)
    def _print(self,current_node):
        if current_node.left!=None:
            self._print(current_node.left)
        print(str(current_node.data),end=" ")
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
    b._deletion(5)
    b.print_tree()