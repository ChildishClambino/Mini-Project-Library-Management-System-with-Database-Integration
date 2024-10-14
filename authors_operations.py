from class_authors import Authors_Class

author_class = Authors_Class

authors = []

from library_connection import connect_database

conn = connect_database()


def authors_menu(db_connection):
    cursor = db_connection.cursor(dictionary=True)
    while True:
        print("Author Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Back to main menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_author(cursor, db_connection)
        elif choice == '2':
            view_author_details(cursor)
        elif choice == '3':
            display_all_authors(cursor)
        elif choice == '4':
            break
        else:
            print("Please enter a valid number.")
    cursor.close()

def add_author(cursor, db_connection):
    name = input("Enter author name: ")
    biography = input("Enter author biography: ")

    # Validate author name
    if not name.replace(" ", "").isalpha():
        print("Author name must contain only alphabetic characters.")
        return

    # Validate biography
    if not isinstance(biography, str):
        print("Biography must be text.")
        return

    cursor.execute("INSERT INTO authors (name, biography) VALUES (%s, %s)", (name, biography))
    db_connection.commit()
    print("Author added successfully.")

def view_author_details(cursor):
    author_id = input("Enter author ID: ")
    cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
    author = cursor.fetchone()
    if author:
        print(author)
    else:
        print("Author not found.")

def display_all_authors(cursor):
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    for author in authors:
        print(author)