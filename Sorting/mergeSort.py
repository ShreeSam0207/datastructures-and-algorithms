class MergeSort():
    def __init__(self,arr):
        if len(arr)>0:
            self.split_arr(arr)
            print(str(arr),end=" ")
        else:
            print("Array is empty")
    
    def split_arr(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            left_arr=arr[:mid]
            right_arr=arr[mid:]
            self.split_arr(left_arr)
            self.split_arr(right_arr)
            return self.merge_sort(arr,left_arr,right_arr)
            
    def merge_sort(self,arr,l,r):
        i=j=k=0
        while i < len(l) and j< len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        while i < len(l):
            arr[k]=l[i]
            k+=1
            i+=1
        while j <len(r):
            arr[k]=r[j]
            k+=1
            j+=1
        return arr

if __name__=="__main__":
    m=MergeSort([1,5,4,7,3,6])