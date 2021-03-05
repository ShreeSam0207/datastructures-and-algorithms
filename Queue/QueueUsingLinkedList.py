class Node():
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    
class QueueLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
    
    def remove(self,data):
        emp=self.is_empty()
        if emp==False:
            self.head.next.prev=None
            self.head=self.head.next
    
    def is_empty(self):
        if self.head==None:
            print("Queue is empty")
            return True
        else:
            return False
    
    def peek_front(self):
        emp=self.is_empty()
        if emp==False:
            print("Peeking front data "+str(self.head.data))
    
    def peek_tail(self):
        emp=self.is_empty()
        if emp==False:
            print("Rear data "+str(self.tail.data))
    
    def print_queue(self):
        nodelist=[]
        current_node=self.head
        while current_node:
            nodelist.append(current_node.data)
            current_node=current_node.next
        print(str(nodelist),end=" ")
        
if __name__=="__main__":          
    q=QueueLinkedList()
    q.peek_front()
    q.peek_tail
    q.is_empty() 
    q.add(0) 
    q.add(1) 
    q.add(2) 
    q.add(3) 
    q.add(4) 
    q.print_queue()
    q.peek_front()
    q.peek_tail()
    q.remove(0)
    q.peek_front()
    q.peek_tail()
    q.print_queue()