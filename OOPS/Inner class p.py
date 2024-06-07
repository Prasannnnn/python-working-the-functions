
class Library:
    def __init__(self):
        self.books = []
        
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn

        def __str__(self):
            return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}'

    def add_book(self, title, author, isbn):
        new_book = self.Book(title, author, isbn)
        self.books.append(new_book)
        print(f'Book added: {new_book}')

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book removed: {book}')
                return
        print(f'Book with title "{title}" not found.')

    def list_books(self):
        if not self.books:
            print('No books in the library.')
        else:
            print('Listing all books:')
            for book in self.books:
                print(book)

# Example usage
library = Library()
library.add_book('Five Points to have', 'chetan Bhagat', '123')
library.add_book('Two states', 'chetan chagat', '456')
library.list_books()
library.remove_book('Two states')
library.list_books()
