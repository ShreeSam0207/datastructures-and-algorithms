class HeapSort():
    def __init__(self):
        self.heap=[]
        
    def insert(self,data):
        if len(self.heap)==0:
            self.heap.append(data)
        else:
           self.heap.append(data)
           self.heapify_heap(data,len(self.heap)-1)
    
    def heapify_heap(self,data,index):
        parent_index=int(abs(index-1)//2)
        parent_data=self.heap[parent_index]
        if parent_data > self.heap[index]:
            tmp=self.heap[parent_index]
            self.heap[parent_index]=self.heap[index]
            self.heap[index]=tmp
            self.heapify_heap(data,parent_index)
        return self.heap
    
    def heap_sort(self):
        sorted_array=[]
        initial_value=self.heap[0]  
        final_value=self.heap[len(self.heap)-1]
        n=len(self.heap)
        for i in range(0,n,1):
            if self.heap[0]!=initial_value:
            self.heap[0],self.heap[n-1]=self.heap[n-1],self.heap[0]
            self.heapify_sort(self.heap,i)
            self.print_heap()
            
    def heapify_sort(self,heap,index):
        l=(2*index)+1
        r=(2*index)+2
        largest=index
        if l<len(heap) and heap[l]<heap[largest]:
            largest=l
        if r<len(heap) and heap[r]<heap[largest]:
            largest=r
        if largest!=index:
            tmp=self.heap[index]
            self.heap[index]=self.heap[largest]
            self.heap[largest]=tmp
            # index+=1
            self.heapify_sort(self.heap,largest)
        return self.heap
    
    def print_heap(self):
        print(str(self.heap),end=" ")
        
    
if __name__=="__main__":
    h=HeapSort()
    h.insert(5)
    h.insert(11)
    h.insert(6)
    h.insert(9)
    h.insert(3)
    h.insert(7)
    h.insert(8)
    h.insert(15)
    h.heap_sort()
    h.print_heap()

        