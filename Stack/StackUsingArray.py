class GrowableStack():
    def __init__(self):
        self.size=0
        self.capacity=1
        self.stack=self.create_new_stack(self.capacity)
    
    #create new stack with new capacity
    def create_new_stack(self,new_cap):
        return []*new_cap
    
    #resize the array woth 2*size of the stack when the stack is full
    def resize(self,new_cap):
        new_arr=self.create_new_stack(new_cap)
        for i in range(0,len(self.stack)):
            new_arr.append(self.stack[i])
        self.stack=new_arr
        self.capacity=new_cap
        
    #stack is LIFO-Last in First Out-  append element to the last
    def push(self,element):
        if self.size==self.capacity:
            self.resize(2*self.size)
        self.stack.append(element)
        self.size+=1
    
    #Stack is LIFO- Sp when we peek, we get the last element added
    def peek(self):
        isempty=self.is_empty()
        if isempty==True:
            print("Stack is empty")
        else:
            print("Value "+str(self.stack[len(self.stack)-1]))
    
    #Check if the stack is empty and return True if empty
    def is_empty(self):
        emp=False
        if self.size==0:
            print("Stack is Empty")
            emp=True
        return emp
    
    #Popping an element from Stack will remove the last element in the stack
    def pop_element(self):
        isempty=self.is_empty()
        if isempty==True:
            print("Stack is empty")
        else:
            self.stack.pop()
            self.size-=1

    #Print Size, Capacity and element of the stack
    def print_stack(self):
        print("stack size :"+str(self.size))
        print("-------")
        print("stack capacity : "+str(self.capacity))
        print("-------")
        for i in range(0,len(self.stack)):
            print(str(self.stack[i]),end=" ")
            

if __name__=="__main__":
    s=GrowableStack()
    s.is_empty()
    s.pop_element()
    s.peek()
    s.push(2)
    s.push(4)
    s.push(6)
    s.push(8)
    s.push(10)
    s.print_stack()
    s.is_empty()
    s.pop_element()
    s.peek()
    s.print_stack()
    
    
    