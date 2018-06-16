arr = [50,22,2,45,19,11,67,0]
print(arr)

def selectionSort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            print("i =", i)
            print("j =", j)
            print("arr[j] =", arr[j])
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            print("arr[i] =", arr[i])
            print("arr[min] =", arr[min])
        print(arr)
    return arr
print(selectionSort(arr))
