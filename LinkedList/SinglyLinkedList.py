class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList():
    def __init__(self):
        self.head=None
        self.size=0
        
    def add_node(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.size+=1
        else:
            current_node=self.head
            while current_node and current_node.next!=None:
                current_node=current_node.next
            current_node.next=new_node
            self.size+=1
            
    def insert_node(self,add_before_index,data):
        new_node=Node(data)
        #three conditions: 
        #1. adding to head
        #2. adding in the middle
        #3. adding to the end
        
        if self.head==None:
            self.head=new_node
        else:
            current_head=self.head
            counter=0
            #add a node after the position, if add_before_index =1, then I add the node after 0 and before 1
            position=add_before_index-1
            #1. adding in th middle and adding at the end
            if position>=0 and position<self.size:
                while current_head!=None:
                    #loop to find the right node
                    if counter!=position:
                        current_head=current_head.next
                        counter+=1
                    else:
                        #adding in the middle
                        if current_head.next!=None:
                            new_node.next=current_head.next
                            current_head.next=new_node
                            self.size+=1
                            break
                        else:
                            #adding in the tail
                            current_head.next=new_node
                            self.size+=1
                            break
            #adding at the head and change the head
            elif position==-1 and position<self.size:
                new_node.next=self.head
                self.head=new_node
                self.size+=1
            else:
                print("index value not applicable")
    
    def delete_node(self,value_to_delete):
        index=self.get_index(value_to_delete)
        if index!=None:
            counter=0
            current_node=self.head
            #three conditions
            #1. Deleting head
            #2 Deleting middle of the node
            #3. Deleting the tail
            
            #deleting the head
            if index==0:
                self.head=self.head.next
                self.size-=1
            else:
                while current_node:
                    #loop over to get the right node
                    if counter!=index:
                        prev_node=current_node
                        current_node=current_node.next
                        counter+=1
                    else:
                        #deleting the tail node
                        if current_node.next==None:
                            prev_node.next=None
                            self.size-=1
                            break
                        else:
                            #deleting the middle node
                            prev_node.next=current_node.next
                            self.size-=1
                            break
        else:
            print("Value cannot be found. Please enter another value")
    
    def get_index(self,val):
        current_node=self.head
        counter=0
        while current_node:
            if current_node.data==val:
                return counter
            current_node=current_node.next
            counter+=1
            
    def get_size(self):
        print("Size of Linked list :" +str(self.size))
    
    def clear_linked_list(self):
        #setting head of linked list to none will clear the linked list
        self.head=None
        
    def get_value(self,index):
        counter=0
        if self.head==None:
            print("Linked List is empty")
        else:
            current_node=self.head
            if index<self.size:
                while current_node:
                    if counter==index:
                        print("Value in this node is "+str(current_node.data))
                        break
                    else:
                        current_node=current_node.next
                        counter+=1
            else:
                print("Index out of bound")
            
    def print_linked_list(self):
        nodelist=[]
        current_node=self.head
        while current_node:
            nodelist.append(current_node.data)
            current_node=current_node.next
        print(str(nodelist),end=" ")      
              
if __name__=="__main__": 
    sl=SinglyLinkedList()
    sl.add_node("Tuesday") 
    sl.insert_node(0,"Monday")
    sl.insert_node(2,"Wednesday")  
    sl.insert_node(2,"Add after 1")   
    sl.insert_node(5,"throw error")   
    sl.print_linked_list()
    sl.get_size()
    sl.delete_node("Monday")
    print("---After Deletion1----")
    sl.print_linked_list()

    
    sl.delete_node("Add after 1")
    print("---After Deletion2----")
    sl.print_linked_list()
    
    sl.delete_node("Wednesday")
    print("---After Deletion3----")
    sl.print_linked_list()
    
    sl.delete_node("Sunday")
    print("---Throw error----")
    sl.print_linked_list()
    
    sl.get_size()
    sl.get_value(1)
    
    
        