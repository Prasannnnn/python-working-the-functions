'''
Problem 1: Library Management System
Create a Book class and a Library class to manage a collection of books.

Requirements:
Book class should have attributes: title, author, and ISBN.
Library class should have methods to:
Add a book.
Remove a book by ISBN.
Search for a book by title.
Display all books in the library.
'''

# class Book:
#     def __init__(self,title,author,isbn) -> None:
#         self.title = title
#         self.author = author
#         self.isbn = isbn

# class Library:
#     def __init__(self) -> None:
#         self.books = []

#     def add_book(self,book):
#         self.books.append(book)
#         print(f"Book{book.title} added to the library")

#     def remove_book(self,isbn):
#         for book in self.books:
#             if book.isbn == isbn:
#                 self.books.remove(book)
#                 print(f"Book with ISBN '{isbn}' removed from the library.")
#                 return
#         print(f"No book found with ISBN '{isbn}'.")

#     def search_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 return book
#         return None
    
#     def display_books(self):
#         if not self.books:
#             print("The library has no books.")
#         else:
#             print("Books in the library:")
#             for book in self.books:
#                 print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

# if __name__ == "__main__":
#     library = Library()
    
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
#     book2 = Book("1984", "George Orwell", "9780451524935")
#     book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    
#     library.add_book(book1)
#     library.add_book(book2)
#     library.add_book(book3)
    
#     library.display_books()
    
#     print("\nSearching for '1984':")
#     book = library.search_book("1984")
#     if book:
#         print(f"Found book: Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
#     else:
#         print("Book not found.")
    
#     print("\nRemoving book with ISBN '9780451524935':")
#     library.remove_book("9780451524935")
    
#     library.display_books()

    
class Book:
    def __init__(self,book,author,isbn) -> None:
        self.book = book
        self.author = author
        self.isbn = isbn
class Library:
    def __init__(self) -> None:
        self.books =[]

    def add_book(self,book):
        self.books.append(book)
        print(book)


book = Book("Haf Girlfirend","Chetan Bhagat","9876543210")
book1 = Book("Five points to do","Chetan Bhagat","321654987")
book2 = Book("Call Center","chetan Bhagat","789456123")

library=Library()
library.add_book(book)

