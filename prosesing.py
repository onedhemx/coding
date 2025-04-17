def processing(text: str, boolevoe: bool, plavat: 10.0):
    if text == "":
            raise ValueError("Строка не должна быть пустой")
    for num in range(int(plavat)):
        if num == 4:
            continue
        if num == 9:
            print(f"Квадрат числа {num} больше 50")
            break
        print(f'chislo: {num}, kvadrat: {num **2}')
    print(f'Stroka: {str}')
    print(f'Bulevoe: {bool}')
    print(f'Floatovoe: {float}')

    try:
        processing('', False, 111)
    except ValueError as e:
    print(f"ValueError: {e}")
    
processing("primer stroki", True, 10.0)


