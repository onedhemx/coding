num = [1, 4 ,6 ,214, 66, 86, 2222]
print("до срот: ", num)
def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j + 1], arr[j]
    return arr
            
sart = buble_sort(num)
print('после сорт: ', sart)
