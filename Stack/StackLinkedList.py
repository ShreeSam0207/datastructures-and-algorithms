class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class StackLinkedList():
    def __init__(self):
        self.head=None
        
    #Stack is LIFO -Last In First Out-Hence the newly added/appended element will become the head
    def push(self,element):
        new_node=Node(element)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    
    #Whenever pop function is called, the node next to the current head becomes the new head of the stack
    def pop(self):
        isempty=self.is_empty()
        if isempty==True:
            print("Stack is empty")
        else:
            self.head=self.head.next
            
    def is_empty(self):
        emp=False
        if self.head==None:
            emp=True
        return emp
    
    #Peek function returns the head data 
    def peek(self):
        isempty=self.is_empty()
        if isempty==True:
            print("Stack is empty")
        else:
            print(self.head.data)
    
    def print_stack(self):
        stack=[]
        isempty=self.is_empty()
        if isempty==True:
            print("Stack is empty")
        else:
            current_node=self.head
            while current_node:
                stack.append(current_node.data)
                current_node=current_node.next
            print(str(stack),end=" ")

if __name__=="__main__":
    s=StackLinkedList()
    s.pop()
    s.peek()
    s.is_empty()
    s.push("Monday")
    s.push("Tuesday")
    s.push("Wednesday")
    s.push("Thursday")
    s.print_stack()
    s.peek()
    s.pop()
    s.print_stack()
        