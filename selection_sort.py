class SelectionSort():
    def __init__(self) -> None:
        pass

    def sort(self,arr):
        n = len(arr)
        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if(arr[min_index]>arr[j]):
                    min_index = j
            arr[min_index],arr[i] = arr[i],arr[min_index]
        return arr
    
    def printArr(self,arr):
        for i in arr:
            print(i,end=" ")
        
if __name__ == "__main__":
    arr = [4,3,5,2,1]
    ss = SelectionSort()
    sorted_arr = ss.sort(arr)
    ss.printArr(sorted_arr)
