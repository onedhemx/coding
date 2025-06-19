class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')
        
class Library:

    def __init__(self):
            books = []
            
    def append_book(self, book):
        self.app_book.append(book)
        
    def remove_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                
    def show_books(self):
        for book in self.books:
            book.get_info()





#3

books = []
while True:
    deistvie = input(' выберете какое то действие: добавить, удалить, вывести список книг ')
    if deistvie == ' добавить ':
        title = input(' название книги ')
        books.append(title)
        
    elif deistvie == ' удалить ':
        title = input(' название книги ')
        if title in books:
            books.remove(title)
        
    elif deistvie == ' вывести список книг':
        print(books)

