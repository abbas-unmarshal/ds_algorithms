class BubbleSort():
    def __init__(self) -> None:
        pass

    def sort(self,arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if(arr[j+1]<arr[j]):
                    arr[j+1],arr[j] = arr[j],arr[j+1]
        return arr
    
    def printArr(self,arr):
        for i in arr:
            print('{} '.format(i),end="")

if __name__ == "__main__":
    bs = BubbleSort()
    arr = [10,2,4,8,11,15]
    sorted_arr = bs.sort(arr)
    bs.printArr(arr)