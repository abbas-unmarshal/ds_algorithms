class QuickSort:

    def partition(self,arr,low,high):
        pivot_index = high
        i = low-1

        for j in range(low,high):
            if(arr[pivot_index]>arr[j]):
                i += 1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[pivot_index] = arr[pivot_index],arr[i+1]
        return i+1
    
    def sort(self,arr,low,high):
        if(low<high):
            partition = self.partition(arr,low,high)
            self.sort(arr,low,partition-1)
            self.sort(arr,partition+1,high)

    def printArr(self,arr):
        for i in arr:
            print(i,end = " ")

qs = QuickSort()
arr = [10,7,8,9,1,5]
qs.sort(arr,0,len(arr)-1)
qs.printArr(arr)