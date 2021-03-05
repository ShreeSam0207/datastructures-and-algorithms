class Node():
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=next
        
class DoublyLinkedList():
    def __init__(self):
        self.head=None
        self.size=0
    
    def add_node(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            current_node=self.head
            while current_node and current_node.next!=None:
                current_node=current_node.next
            current_node.next=new_node
            new_node.prev=current_node
        self.size+=1
    
    def insert_node(self,index,data):
        new_node=Node(data)
        counter=0
        position=index-1
        current_node=self.head
        if self.head==None:
            self.head=new_node
            return
        if position>=0 and position<self.size:
            while current_node:
                if position!=counter:
                    current_node=current_node.next
                    counter+=1
                else:
                    if current_node.next!=None:
                        new_node.next=current_node.next
                        current_node.next.prev=new_node
                        current_node.next=new_node
                        new_node.prev=current_node
                        self.size+=1
                        break
                    else:
                        current_node.next=new_node
                        new_node.prev=current_node
                        self.size+=1
                        break
                    
        elif position ==-1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
            self.size+=1
        else:
            print("Node not reachable")
    
    def delete_node(self,data):
        index=self.get_index(data)
        counter=0
        if index!=None and index<self.size:
            if index>0:
                current_node=self.head
                while current_node:
                    if counter!=index:
                        current_node=current_node.next
                        counter+=1
                    else:
                        if current_node.next!=None:
                            current_node.prev.next=current_node.next
                            self.size-=1
                            break
                        else:
                            current_node.prev.next=None
                            current_node=None
                            self.size-=1
                            break
            else:
                self.head=self.head.next
                self.size-=1
        else:
            print("Index not reachable.Please check the value")
                            
                
    def get_index(self,data):
        counter=0
        current_node=self.head
        if self.head==None:
            return None
        else:
            while current_node:
                if current_node.data==data:
                    return counter
                current_node=current_node.next
                counter+=1
                   
    def print_dll(self):
        current_node=self.head
        nodelist=[]
        while current_node:
            nodelist.append(current_node.data)
            current_node=current_node.next
        print(str(nodelist),end=" ")

if __name__=="__main__":
    d=DoublyLinkedList()
    d.add_node("Monday")
    d.insert_node(0,"Sunday")
    d.insert_node(2,"Wednesday")
    d.insert_node(8,"Tuesday")
    d.delete_node("Sunday")
    print("---After Deletion Head-----")
    d.delete_node("Wednesday")
    print("---After Deletion Tail-----")
  
    d.insert_node(2,"Saturday")
    d.add_node("Friday")
    # d.print_dll()
    
    d.delete_node("Saturday")
    print("---After Deletion Middle Node-----")
    d.print_dll()
    
            
