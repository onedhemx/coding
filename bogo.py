import random

def is_sorted(lst):

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def bogosort(lst):

    while not is_sorted(lst):
        random.shuffle(lst)
    return lst

unsorted_list = [3, 1, 2, 4]
sorted_list = bogosort(unsorted_list.copy())
print("Исходный список:", unsorted_list)
print("Отсортированный список:", sorted_list)
