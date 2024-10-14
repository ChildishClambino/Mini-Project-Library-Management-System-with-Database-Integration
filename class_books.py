class Def_Books():
    def __init__(self, title, author, genre, ISBN, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__ISBN = ISBN
        self.__publication_date = publication_date
        self.__availbility_status = "available"

    def borrow_book(self):
        if self.__availbility_status == "available":
            self.__availbility_status == "borrowed"
            return True
    
    def return_book(self):
        if self.__availbility_status == "borrowed":
            self.__availbility_status == "available"
            return True
        
    def __str__(self):
        return f"title: {self.__title}, author: {self.__author}, genre: {self.__genre} isbn: {self.__ISBN}, published: {self.__publication_date}, availibity: {self.__availbility_status}"
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_isbn(self):
        return self.__ISBN
    
    def get_published(self):
        return self.__publication_date
    
    def get_status(self):
        return self.__availbility_status
    
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_publish(self, publication_date):
        self.__publication_date = publication_date

    def set_status(self, availability_status):
        self.__availbility_status = availability_status