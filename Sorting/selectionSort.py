class SelectionSort():
    def __init__(self,arr):
        if len(arr)>0:
            for i in range(0,len(arr)-1):
               min_val,index=self._find_min(arr,i) 
               if arr[i]>min_val:
                   tmp=arr[index]
                   arr[index]=arr[i]
                   arr[i]=min_val
            print(str(arr),end=" ")
        else:
            print("Array is empty")
    
    def _find_min(self,arr,start):
        min=arr[start]
        index=start
        for i in range(start,len(arr)):
            if min>arr[i]:
                min=arr[i]
                index=i
        return min,index

if __name__=="__main__":
    s=SelectionSort([1,5,4,7,3,6])