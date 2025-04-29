import os
def procht():
    try:
         with open('file.txt') as f:
            if os.path.exists("file.txt"): 
                print("файл существ")
            else:
                print('не сущ')
                
    except FileNotFoundError as e :
        print('файл не найден')
