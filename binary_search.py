class BS:
    def __init__(self) -> None:
        pass

    def binarySearch(self,arr,ele,low,high):
        if(low>high):
            return "element not found"
        mid = int((low+high)/2)
        if(arr[mid] == ele):
            return mid
        elif(arr[mid]< ele):
            low = mid + 1
            return self.binarySearch(arr,ele,low,high)
        return self.binarySearch(arr,ele,low,mid-1)
    
if __name__ == "__main__":
    arr = [2,5,8,10,15,20,30]
    bs = BS()
    print(bs.binarySearch(arr,21,0,len(arr)))
        