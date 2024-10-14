from book_operations import book_menu
from authors_operations import authors_menu
from genre_operations import genre_main
from users_operations import user_op_menu

from library_connection import connect_database

class LibraryManagement():

    def main(self):
        # Establish database connection
        db_connection = connect_database()

        while True:
            print("Welcome to the Library Management System! \nMenu")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Genre Operations")
            print("5. Quit")
            choice = input("Enter choice: ")

            if choice == '1':
                book_menu(db_connection)
            elif choice == '2':
                user_op_menu(db_connection)
            elif choice == '3':
                authors_menu(db_connection)
            elif choice == '4':
                genre_main(db_connection)
            elif choice == '5':
                print("Thank you for using the Library Management System! Goodbye.")
                break
            else:
                print("Please enter a valid number.")

if __name__ == "__main__": 
    library_management = LibraryManagement()
    library_management.main()