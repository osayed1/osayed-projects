
class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def info(self):
        return f"{self.title} by {self.author} ({self.copies} copies)"

class Library:
    def __init__(self):
        self.books = []   

    def add_book(self, book):
        self.books.append(book)
        print("Book added.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

    def search(self, title):
        for book in self.books:
            if book.title == title:
                print("Book found:", book.info())
                return
        print("Book not found.")

    def show_all(self):
        print("\n--- All Books ---")
        for b in self.books:
            print(b.info())
        print("-----------------")



lib = Library()

lib.add_book(Book("Moza", "Ahmad", 4))
lib.add_book(Book("Rose", "Soso", 2))

lib.search("Rose")

lib.remove_book("Moza")

lib.show_all()
