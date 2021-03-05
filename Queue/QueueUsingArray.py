class queue():
    def __init__(self):
        self.queue=[]
        self.size=0
        self.capacity=7
    
    #Adding to the queue = appending to the end of the array
    def add(self,element):
        cap=self.check_capacity()
        if cap==True:
            print("Queue is full, cannot add element,the current queue size is "+str(self.size) +" and capacity is "+str(self.capacity))
        else:
            self.queue.append(element)
            self.size+=1
    
    #Check queue size if equal to capacity to avoid overflow condition
    def check_capacity(self):
        if self.size==self.capacity:
            return True
        else:
            return False
    
    #check if queue is empty
    def is_empty(self):
        if self.size==0:
            print("queue is empty, the size of queue is "+str(self.size))
            return True
        else:
            return False
    
    #Queue is FIFO-First in First Out, so peeking front is peeking the first element in the array
    #while peeking first in Stack is peeking the last element in the array
    def peek_front(self):
        emp=self.is_empty()
        if emp==False:
            print("First element in queue is "+str(self.queue[0]))
            
    #print the elements in the queue
    def print_queue(self):
        emp=self.is_empty()
        if emp==False:
            for i in range(0,len(self.queue)):
                print(str(self.queue[i]),end= " ")
    
    #removing an element from the queue is removing the first element of the array
    def remove(self):
        emp=self.is_empty()
        if emp==False:
            self.queue.pop(0)
            self.size-=1
    
if __name__=="__main__":
    q=queue()
    q.peek_front()
    q.is_empty()
    q.add(0)
    q.add(1)
    q.add(3)
    q.add(4)
    q.add(5)
    q.add(6)
    q.add(7)
    q.add(2)
    q.print_queue() 
    q.peek_front()
    q.is_empty()
    q.remove()
    q.peek_front()
    q.print_queue() 
    