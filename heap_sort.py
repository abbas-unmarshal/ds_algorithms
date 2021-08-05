class HeapSort:
    def __init__(self,arr) -> None:
        self.n = len(arr)-1
        self.arr = arr

    def sort(self):
        self.heapify()
        for i in range(self.n,0,-1):
            self.arr[0],self.arr[i] = self.arr[i],self.arr[0]
            self.n = self.n-1
            self.minHeap(0);
    
    def heapify(self):
        self.n = len(self.arr)-1
        for i in range(self.n//2,-1,-1):
            self.minHeap(i)

    def minHeap(self,i):
        left = i*2
        right = i*2 + 1
        min = i
        if left<=self.n and self.arr[left]<self.arr[i]:
            min = left
        if right<=self.n and self.arr[right]<self.arr[min]:
            min = right 
        if min != i:
            self.arr[i],self.arr[min] = self.arr[min],self.arr[i]
            self.minHeap(min)
        
    def printArr(self):
        for i in self.arr:
            print(i,end=" ")

arr = [6,10,3,8,2,5]
hs = HeapSort(arr)
hs.sort()
hs.printArr()