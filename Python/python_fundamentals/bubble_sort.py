arr = [3,6,9,0,5,7,1,4,2,8]

def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
print(bubbleSort(arr))