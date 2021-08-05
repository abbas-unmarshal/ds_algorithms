class MergeSort:
    def __init__(self,arr) -> None:
        self.arr = arr
    
    def sort(self,low,high):
        if(low<high):
            mid = int((low+high)/2)
            self.sort(low,mid)
            self.sort(mid+1,high)
            self.merge(low,mid,high)
    
    def merge(self,low,mid,high):
        temp = self.arr.copy()

        i = low
        j = mid+1
        k = low
        while(i<=mid and j<=high):
            if(temp[i]<=temp[j]):
                self.arr[k]=temp[i]
                i+=1
            else:
                self.arr[k] = temp[j]
                j+=1
            k+=1
        while(i<=mid):
            self.arr[k] = temp[i]
            k+=1
            i+=1
        while(j<=high):
            self.arr[k] = temp[j]
            k+=1
            j+=1
    
    def printArr(self):
        for i in self.arr:
            print(i,end = " ")

arr = [4,1,7,3]
ms = MergeSort(arr)
ms.sort(0,len(arr)-1)
ms.printArr()