class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id =library_id
        self.__borrowed_books = []

    def get_name(self):
        return self.__name
    
    def get_library_id(self):
        return self.__library_id
    
    def get__borrowed_books(self):
        return self.__borrowed_books
    
    def borrow_book(self, book):
        self.__borrowed_books.append(book.get_title())
        book.borrow()
    
    def return_book(self, book):
        self.__borrowed_books.remove(book.get_title())
        book.return_book()
    
    def __str__(self):
        return f"User: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {self.__borrowed_books}"
    