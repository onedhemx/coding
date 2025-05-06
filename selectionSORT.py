num = [2134, 5634, 666, 99999, 1, 34, 42, 0, 78, 90]
print(num)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j 
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return arr

sorte_num = selection_sort(num)
print(sorte_num)
