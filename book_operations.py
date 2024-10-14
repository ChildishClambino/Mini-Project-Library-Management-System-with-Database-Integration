from class_books import Def_Books

from library_connection import connect_database

conn = connect_database()

books_def = Def_Books

books = []
genres = []
authors = []

def book_menu(db_connection):
    cursor = db_connection.cursor(dictionary=True)
    while True:
        print("Book Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Back to main menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_book(cursor, db_connection)
        elif choice == '2':
            borrow_book(cursor, db_connection)
        elif choice == '3':
            return_book(cursor, db_connection)
        elif choice == '4':
            search_book(cursor)
        elif choice == '5':
            display_all_books(cursor)
        elif choice == '6':
            break
        else:
            print("Please enter a valid number.")
    cursor.close()

def add_book(cursor, db_connection):
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    isbn = input("Enter ISBN: ")
    publication_date = input("Enter publication date (YYYY-MM-DD): ")

    # Check if the author exists
    cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
    author = cursor.fetchone()
    if author:
        cursor.execute(
            "INSERT INTO books (title, author_id, isbn, publication_date) VALUES (%s, %s, %s, %s)",
            (title, author_id, isbn, publication_date)
        )
        db_connection.commit()
        print("Book added successfully.")
    else:
        print("Author does not exist.")

def borrow_book(cursor, db_connection):
    user_id = input("Enter user ID: ")
    book_id = input("Enter book ID: ")
    borrow_date = input("Enter borrow date (YYYY-MM-DD): ")

    # Check if the book exists and is available
    cursor.execute("SELECT * FROM books WHERE id = %s AND availability = 1", (book_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)",
                       (user_id, book_id, borrow_date))
        cursor.execute("UPDATE books SET availability = 0 WHERE id = %s", (book_id,))
        db_connection.commit()
        print("Book borrowed successfully.")
    else:
        print("Book not available or does not exist.")

def return_book(cursor, db_connection):
    borrow_id = input("Enter borrow ID: ")
    return_date = input("Enter return date (YYYY-MM-DD): ")
    cursor.execute("UPDATE borrowed_books SET return_date = %s WHERE id = %s", (return_date, borrow_id))
    cursor.execute("UPDATE books SET availability = 1 WHERE id = (SELECT book_id FROM borrowed_books WHERE id = %s)", (borrow_id,))
    db_connection.commit()
    print("Book returned successfully.")

def search_book(cursor):
    title = input("Enter book title to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE %s", ('%' + title + '%',))
    books = cursor.fetchall()
    for book in books:
        print(book)

def display_all_books(cursor):
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)