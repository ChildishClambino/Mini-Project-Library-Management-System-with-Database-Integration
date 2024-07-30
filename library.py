from book import Book
from user import User
from author import Author
from genre import Genre
from add_borrowed_books import add_borrowed_books

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def add_book(self, title, author, isbn, publication_date):
        self.books.append(Book(title, author, isbn, publication_date))
    
    def add_user(self, name, library_id):
        self.users.append(User(name, library_id))

    def add_author(self, name, biography):
        self.authors.append(Author(name, biography))

    def add_genre(self, name, description):
        self.genres.append(Genre(name, description))

    def display_books(self):
        for book in self.books:
            print(book)

    def display_users(self):
        for user in self.users:
            print(user)

    def display_authors(self):
        for author in self.authors:
            print(author)

    def display_genres(self):
        for genre in self.genres:
            print(genre)

    def search_book(self, identifier):
        for book in self.books:
            if book.get_isbn() == identifier or book.get_title().lower() == identifier.lower():
                return book
        return None
    
    def borrow_book(self, library_id, book_title):
        user = next((u for u in self.users if u.get_library_id() == library_id), None)
        book = self.search_book(book_title)
        if user and book:
            user.borrow_book(book)
            print(f"{user.get_name()} borrowed {book.get_title()}.")
            add_borrowed_books()

        else:
            print("User or Book not found.")

    def return_book(self, library_id, book_title):
        user = next((u for u in self.users if u.get_library_id() == library_id), None)
        book = self.search_book(book_title)
        if user and book:
            user.return_book(book)
            print(f"{user.get_name()} returned {book.get_title()}.")
        else:
            print("User or book not found")