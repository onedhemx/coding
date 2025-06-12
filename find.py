mu_list = [10, 59, 67, 100, 49, 139]
el = 100

def indexx(pervi, obj): 
    for i in range(len(pervi)):
        if pervi[i] == obj:
            return i
    return -1

res = indexx(pervi, el)
print(f'элемент {el}: {res}")
