class Book:
    def __init__(self, nazvanie, avtor, year_publications):
        self.nazvanie = nazvanie
        self.avtor = avtor
        self.year_publications = year_publications
    
    def vivodd(self):
        print('NAZVASNIE:', self.nazvanie)
        print('AVTOR:', self.avtor)
        print('GOD SOZDANIA:', self.year_publications)
        
        
    def get_info(self):
        return f"KNIGA: {self.nazvanie}, AVTOR: {self.avtor}, GOOD: {self.year_publications}"

        
book_book = Book('Prestuplenie i nakazanie', 'Dostoevske', 1866)
book_book2= Book('Ojzerelie', 'Gi de Mopasasn', 1884)
book_book3 = Book('Boloshie Nadejzdi', 'Dickens', 1861)

print(book_book.get_info())
print(book_book2.get_info())
print(book_book3.get_info())
