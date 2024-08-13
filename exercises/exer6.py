# library management system with classes and objects

class Library():
    def __init__(self) -> None:
        self.noBooks = 0
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def show_info(self):
        print(f"The library has {self.noBooks} no. of books and the books are:")
        for book in self.books:
            print(book)


l1 = Library()
l1.add_books("harry potter")
l1.show_info()