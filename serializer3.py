

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def get_info(self):
        print(f'{self.name}, {self.author}, {self.year}')
        
        
    def to_dict(self):
        return {
            "name": self.name,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["author"], data["year"])
        
class Library:

    def __init__(self, filename):
            self.books = []
            self.load()
            self.filename = filename
            
    def append_book(self, book):
        self.app_book.append(book)
        self.save()
        
    def remove_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
                self.save()
                
                
    def show_books(self):
        for book in self.books:
            book.get_info()
            
    def load(self):
        with open(filename, "r") as f:
            data = json.load(f)
        self.books = []
        for item in data:
            book = Book.from_dict(item)
            self.books.append(book)
    
    def save(self):
        data = []
        
        for book in self.books:
            data.append(book.to_dict())
        with open(filename, "w") as f:
            json.dump(data, f)
            
