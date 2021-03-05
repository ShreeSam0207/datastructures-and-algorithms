class BubbleSort():
    def __init__(self,arr):
        if len(arr)>0:
            self._bubble_sort(arr)
            print(str(arr),end=" ")
        else:
            print("Nothing to sort as array is empty")
    
    def _bubble_sort(self,arr):
        for i in range(0,len(arr)):
            for j in range(i,len(arr)):
                if arr[j]<arr[i]:
                    tmp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=tmp
        return arr

if __name__=="__main__":
    b=BubbleSort([1,5,4,7,3,6])