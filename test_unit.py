
class Vichisl:
    def __init__(self):
        
        n = int(input())

        factorial = 1

        for i in range(2, n+1):
            factorial *= i

        print(factorial)
        
        
    def __init__(self):
        a = float(input('введите основание '))
        b = float(input('введите показ степени'))
        
        res = a ** b
        
        print(F'{a} в степени {b} равно {res}')
        
    def __init__(self):
        
        Q = int(input('введите Q'))
        m = int(input('введите m'))
        t = int(input('введите t'))
        c = Q/(m * t)
        print(c)












        
a = Vichisl()
