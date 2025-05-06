import random
import time

my_list = [random.randint(0, 100000) for _ in range(10000)]

def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n):
        
        for j in range(n - i - 1):
            
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

def selection_sort(arr):
    
    n = len(arr)
    for i in range(n):
        
        min_idx = i
        for j in range(i + 1, n):
            
            if arr[j] < arr[min_idx]:
                
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr
    
def timsort(arr):
    
    return sorted(arr)
    
def time_gegege(sort_fun, data):
    
    start_time = time.time()
    
    sort_fun(data.copy())

    
    end_time = time.time()
    
    raznitsa = end_time - start_time 
    
    return raznitsa

bubble_time = time_gegege(bubble_sort, my_list)
selection_time = time_gegege(selection_sort, my_list)
timsort_time = time_gegege(timsort, my_list)

print(f"бабле сорт: {bubble_time} секунд")
print(f"селектион сорт: {selection_time} секунд")
print(f"тим сорт: {timsort_time} секунд")
