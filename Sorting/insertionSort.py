class InsertioNSort():
    def __init__(self,arr):
        if len(arr)>0:
            self.insertion_sort(arr)
            print(str(arr),end=" ")
        else:
            print("Array is empty")
    
    def insertion_sort(self,arr):
        for i in range(1,len(arr)):
            for j in range(i-1,-1,-1):
                if arr[j]>arr[i]:
                    tmp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=tmp
                    
        return arr

if __name__=="__main__":
    i=InsertioNSort([1,5,4,7,3,6])