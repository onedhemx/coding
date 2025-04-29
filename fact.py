def gegege(n):
    with open('file.txt', 'w') as f :
        if n == 1:
            return 1
        else:
            return n * gegege(n-1)
print(gegege(11)) 
