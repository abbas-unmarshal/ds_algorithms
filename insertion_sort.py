class InsertionSort:
    def __init__(self) -> None:
        pass

    def sort(self, arr):
        n = len(arr)
        for i in range(1,n):
            for j in range(i,0,-1):
                if(arr[j]<arr[j-1]):
                    arr[j],arr[j-1]=arr[j-1],arr[j]
        return arr
    
    def printArr(self, arr):
        for i in arr:
            print(i,end=" ")
        
if __name__ == "__main__":
    arr = [5,2,3,1,4]
    IS = InsertionSort()
    sorted_arr = IS.sort(arr)
    IS.printArr(sorted_arr)