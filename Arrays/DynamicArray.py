class DynamicArray():
    def __init__(self):
        self.size=0
        #1. Initalizing capacity with 1
        self.capacity=1
        #2. Create a new array with capacity 1 and size 0
        self.A=self.create_new_array(self.capacity)
    
    def create_new_array(self,new_cap): 
        # returns new array created with size of new_cap
        return []*new_cap
    
    def append_element(self,element): 
        #when size of my array = capacity, no elements can be added, hence we increase the capacity by twice the size
        if self.size==self.capacity:  
            self.resize_array(2*self.size)
        self.A.append(element) 
        #as and when we add elements, we increase the size of the array
        self.size+=1 
    
    def insert_element(self,index,element):
        if index > self.size or index < 0 :
            print("IndexError")
        else:
            #duplicate the last element of the array to next index, from the last index, 
            # loop down till index value and copy the current index vlaue to next index value
            self.append_element(self.A[len(self.A)-1])
            for i in range(len(self.A)-1,index,-1):
                self.A[i]=self.A[i-1]
            self.A[index]=element
    
    def delete_element(self,element):
        index=self.get_index(element)
        if index >=0:
            if index<self.size-1:
                #from the index of element to be deleted, 
                # copy the next value of element to be deleted to current index/value to be deleted
                for i in range(index,self.size-1,1):
                    self.A[i]=self.A[i+1]
                self.A=self.A[:-1]
                self.size-=1
            else:
                #deleting the last element of the array
                self.A=self.A[:index]
                self.size-=1
        else:
            print("element cannot be found")
    
    def get_index(self,element):
        for i in range(len(self.A)):
            if self.A[i]==element:
                return i
            
    def resize_array(self,new_cap): 
        #creates new array with two times the size of current capacity
        new_arr=self.create_new_array(new_cap)
        #copy the old array into new array which has more capacity
        for i in range(0,len(self.A)):
            new_arr.append(self.A[i]) 
        self.A=new_arr 
        self.capacity=new_cap 
    
    def print_array(self): 
        print("------Result------")
        print(str(self.A),end="\n")
        print("Size of the array "+str(self.size),end="\n")
        print("Capacity of the array: "+str(self.capacity))

if __name__=="__main__":
    d=DynamicArray()
    d.append_element(2)
    d.append_element(4)
    d.append_element(6)
    d.append_element(8)
    d.append_element(10)
    d.insert_element(3,5)
    d.insert_element(0,1)
    d.insert_element(7,11)
    d.insert_element(8,12)
    d.print_array()
    d.delete_element(12)
    d.print_array()
    d.delete_element(1)
    d.print_array()
    d.append_element(100)
    d.print_array()