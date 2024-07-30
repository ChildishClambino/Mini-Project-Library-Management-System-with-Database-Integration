from library import Library
from add_authors_to_db import add_authors_to_db
from add_borrowed_books import add_borrowed_books
from add_book_to_db import add_book_to_db
from add_users_to_db import add_users_to_db
from add_genres_to_db import add_genres_to_db
from connection_to_db import connect_database

# Function checks if author exists using author id
def check_author_exists(author_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = " SELECT * FROM authors WHERE id = %s"
            cursor.execute(query, (author_id,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()

# Function checks to see if genre exists using genre id
def check_genre_exists(genre_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM genres WHERE id = %s"
            cursor.execute(query, (genre_id,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()
# Function checks if user exists using user_id
def check_if_user_exists(user_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()

# Function checks if book exists using book_id
def check_if_book_exists(book_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            result = cursor.fetchone()
            return result is not None
        finally:
            cursor.close()
            conn.close()   

# The starting point for the program
def main():
    library = Library()

    # Interface offering users different imputs that allow interaction with the program and SQL database
    while True:
        print("\nWelcome to the Library Management System!\nMain Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            print("\nBook Operations\n1. Add new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")    # Inputing 1 takes you to the "Book Operations Menu"
            book_choice = input("Select an option: ")

            # This choice allows you to add a book in the program on a list and to the database
            if book_choice == '1':                          
                title = input("Enter book title: ")
                author_id = input("Enter author id: ")
                genre_id = input("Enter the genre id: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                publication_date = input("Enter publication date: ")
                
                # Checking on the existence of the authro's id
                if not check_author_exists(author_id):                          
                    print(f"The Author ID {author_id} does not exist!")
                    continue

                if not check_genre_exists(genre_id):                            # Checking on the existence of the genre
                    print("The genre doesnt exists")
                    continue

                library.add_book(title, author, isbn, publication_date)
                availability = True
                add_book_to_db(title, author_id, genre_id, isbn, publication_date,availability)


                print("Book added successfully. ")
                

            elif book_choice == '2':                                                        # Function allowing you to borrow a book from the library
                library_id = input("Enter your library ID: ")
                book_title = input("Enter the title of the book you would like to borrow: ")
                user_id = input("Enter the user id: ")
                book_id = input("Enter the book id: ")
                borrow_date = input("What is that date you borrowed the book: ")
                return_date = input("When when is your return day: ")
                availability = True

                if not check_if_user_exists(user_id):                                      # Checks for the existence of a  user's id
                    print("User doesn't exist! ")
                    continue

                if not check_if_book_exists(book_id):     # Checking on the existence of a book using the book's id
                    print("Book doesn't exist! ")
                    continue  
            
                library.borrow_book(library_id, book_title)
                add_borrowed_books(user_id, book_id, borrow_date, return_date)  

            elif book_choice == '3':    # Allows a user to return a book that was borrowed
                library_id = input("Enter your library ID: ")
                book_title = input("Enter the title of the book to return: ")
                library.return_book(library_id, book_title)

            elif book_choice == '4':     # Searches for a specific book using the ISBN or Title of the book
                identifer = input("Enter book ISBN or title to search: ")
                book = library.search_book(identifer)
                if book:
                    print(book)
                else:
                    print("Book not found.")

            elif book_choice == '5':    # Dispplays all the books
                library.display_books()

        # This choice pulls up the "User Operations Menu"
        elif choice == '2':
            print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
            user_choice =input("Select an option: ")

            if user_choice == '1':  # This adds a new user
                name = input("Enter user name: ")
                library_id = input("Enter library ID: ")
                library.add_user(name, library_id)
                print("User added successfully.")
                add_users_to_db(name,library_id)

            elif user_choice == '2':
                library_id = input("Enter library ID: ")
                user = next((u for u in library.users if u.get_library_id() == library_id), None)
                if user:
                    print(user)
                else:
                    print("User not found.")

            elif user_choice == '3':    # Displays all users                    
                library.display_users()


        # This pulls up the "Author Operations Menu"
        elif choice == '3':
            print("\nAuthor Operations:\n1. Add new author\n2. View author details\n3. Display all authors")
            author_choice = input("Select an option: ")

            # Adds new author
            if author_choice == '1':
                name = input("Enter author name: ")
                biography = input("Enter author biography: ")
                library.add_author(name, biography)
                add_authors_to_db(name, biography)
                print("Author successfully added! ")

            # View details about an author
            elif author_choice == '2':
                name = input("Enter author name: ")
                author = next((a for a in library.authors if a.get_name() == name), None)
                if author:
                    print(author)
                else:
                    print("Author not found.")

            # View all authors
            elif choice == '3':
                library.display_authors()

        # Pulls up the Genre Operations Menu
        elif choice == '4':
            print("\nGenre Operations\n1. Add new genre\n2. View genre details\n3. Display all genres")
            genre_choice = input("Select an option: ")

            # Adds new genre
            if genre_choice == '1':
                name = input("Enter the genre name: ")
                description = input("Enter the genre description: ")
                library.add_genre(name, description)
                print("Genre has been added successfully! ")
                add_genres_to_db(name, description)

            # This allows you to view genre details
            elif genre_choice == '2':
                name = input("Enter genre name: ")    
                genre = next((g for g in library.genres if g.get_name() == name), None)
                if genre:
                    print(genre)
                else:
                    print("Genre not found.")

            # This allows you to view all the genres
            elif genre_choice =='3':
                library.display_genres()

        # This ends the program
        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
