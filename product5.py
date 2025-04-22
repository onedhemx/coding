products = [("Хлеб", 40, 20), ("Молоко", 60, 15), ("Яблоки", 100, 50)]
for product in products:
    nazvan, tsena, kol = product
    print(f"Товар: {nazvan}, Цена: {tsena}")
    
def vivesti_products(products):
    for product in products:
        if product[1] < 80:
            print(product[0])

vivesti_products(products)

def vichislen(products):
    for product in products:
        sum = product[1] * product[2]
        print(f"{product[0]} - всего на {sum}")

vichislen(products)

def max_tovar(products):
    max_tsena = 0 
    mostdorogoiproduct = None
    for product in products:
        total_tsena = product[1] * product[2]
        
        if total_tsena > max_tsena:
            max_tsena = total_tsena
            
            max_nazv = ""
            
            for product in products:
                
                
    print(max_tsena)    
    
max_tovar(products)
