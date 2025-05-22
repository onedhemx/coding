from abc import ABC, abstractmethod
class LibraryUser(ABC):
    
    name = ''
    user_id = 0
    
    # def __init__(name, user_id):
    #     self.name = name
    #     self.user_id = user_id
        
        @abstractmethod
    def borrow_book(self, book):

        pass
    
    @abstractmethod
    def return_book(self, book):

        pass
    
# 2

class Student(LibraryUser):
    # def __init__(name, user_id):
        # super().
        borrowed_books = []
        
    def borrow_book(title):
        # if len(borrow_books) <= 3:
        #     print(f'{self.name} может брать не более 3 книг одновременно')
            
        # else self.borrowed_books.append(book)
        #     print(f"{self.name} взял книгу: {book}")
            
        book = self.library.remove.book(title)    
        if book:
            borrowed_book.append(book)
            
class Teacher(LibraryUser):
    def __init__(name, user_id):
        super().borrowed_books = []
        
    def borrow_books(name, user_id):
        if len(borrow_books) <= 5:
            print(f'{self.name} может брать не более 5 книг одновременно')
            
        else self.borrowed_books.append(book)
            print(f"{self.name} взял книгу: {book}")
            
    def
    
        
# 3

class Book:
    def __init__(self, title, author, isbn, available= True):
        self.title = title
        self.author = author
        self.insbn = insbn
        self.available = available
        pass
    
class Library:
    def __init__(self, book):
        self.books = []
        
    def add_book(self, book):
        for  book in self.books:
            if book not in books:
                self.books.append(book)
                print(f"книга '{book.title}' добавлена в библиотеку")
                
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'книга {title} удалена')
            
    def find_book_by_title(self, title):
        found_books = []
        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)
        return found_books
        
            
            
    
            
            
    
    
    
    
